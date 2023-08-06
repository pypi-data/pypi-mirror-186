# AGONS
# %%
"""Class for AGONS"""

#Author: Christopher W. Smith
#Date: 01/17/2023

#Data processing
import numpy as np
import pandas as pd
from IPython.display import display
#Data plotting
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import ipympl
import seaborn as sns
sns.set_style('ticks')
#Modeling and Scoring
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, Normalizer, StandardScaler
from AGONS_nano.Custom_Transformers import RowStandardScaler, RowMinMaxScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, LeaveOneOut, RepeatedStratifiedKFold
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA 
from sklearn.model_selection import RandomizedSearchCV as rscv
import time
from sklearn.model_selection import cross_val_score
class AGONS:
    """Class for AGONS modeling nanosensor array data"""
    def __init__(self, k_max = 10, cv_method = 'Stratified K Fold' , 
                cv_fold = 5, random_state = None, rep_fold = 5):
        
        """Set initial parameters to run AGONS.

        Parameters
        ----------
        k_max: int or (pandas DataFrame.shape[1] + 1). Defines the maximum k value for feature selection to run. For sensor design it is reccommended to use the total number of sensors to trial all ranked important sensors.
        cv_method = 'Stratified K Fold' (default),'Repeated Stratified K Fold', 'Leave One Out' or 'Custom Value'. Choice between different methods of cross-validation see https://scikit-learn.org/stable/modules/cross_validation.html for further details. 'Custom Value' does not use a specific method to cross-validate and instead only cross-validates based on the RandomizedSearchCV algorithm. Note, Stratified K Fold is fastest.
        cv_fold = 5 (default), int. The total number of folds performed in cross-validation.
        random_state = None or int. Sets a reproducible state for data. Recommended to obtain reproducible results.
        rep_fold = 5 (default), int. Used on for repeating stratified K Fold, where each cross-validation fold is repeated n number of times
        """

        self.k_max = k_max
        self.cv_method = cv_method
        self.cv_fold = cv_fold
        self.random_state = random_state
        self.rep_fold = rep_fold
    
    def activate(self, xtrain, ytrain, xval, yval):
        """Fits AGONS modeling on training then will predict on validation.

        Parameters
        ----------
        xtrain : {array-like, sparse matrix} of shape (n_samples, n_features) or \
                (n_samples, n_samples) if metric='precomputed'
            training data.
        ytrain : {array-like, sparse matrix} of shape (n_samples,) or \
                (n_samples, n_outputs)
            validation target values.
        xval : {array-like, sparse matrix} of shape (n_samples, n_features) or \
                (n_samples, n_samples) if metric='precomputed'
            validation data.
        yval : {array-like, sparse matrix} of shape (n_samples,) or \
                (n_samples, n_outputs)
            validation target values."""
        
        self.xtrain = xtrain
        self.ytrain = ytrain
        self.xval = xval
        self.yval = yval

        #Pipeline for classifer involves a feature_selection, scaler, PCA and SVM
        pipe = Pipeline([
                ('anova', SelectKBest(f_classif)),
                ('scaler', MinMaxScaler()),
                ('pca', PCA()), 
                ('svm', SVC(probability=True))
                ])
    
        #Setting Randomized Search parameters for pipe.
        ran_pam= {  
            'scaler': [MinMaxScaler(), Normalizer(), StandardScaler(), RowMinMaxScaler(), RowStandardScaler()],
            'anova__k': list(np.arange(3, self.k_max)), 
            'pca__n_components': list(np.arange(2, 10,1)),
            'pca__svd_solver': ['full'],
            'pca__whiten': [True, False],
            'svm__C': np.arange(0.01, 2, 0.01),
            'svm__gamma':  np.arange(0, 1, 0.01),
            "svm__kernel": ["rbf","linear","poly","sigmoid"],
            "svm__random_state": [self.random_state]}
        
        #Cross-validator selector
        cv_dict = {'Stratified K Fold': StratifiedKFold(n_splits=self.cv_fold),
           'Repeated Stratified K Fold': RepeatedStratifiedKFold(n_splits=self.cv_fold, n_repeats = self.rep_fold, random_state= self.random_state),
           'Leave One Out':LeaveOneOut(),
           'Custom Value': self.cv_fold}
        cv_inner = cv_dict[self.cv_method]

        #Setting Randomized search.
        search = rscv(
            estimator=pipe,
            param_distributions=ran_pam,
            n_iter=1000,
            n_jobs=-1,
            cv=cv_inner,
            verbose=2,
            random_state=self.random_state,
            return_train_score=True,
            error_score=0)

        #Pre-fit confirmation and CV-Check
        print('Modeling Initiated')

        #Fitting data
        print('Fitting Data')
        search.fit(self.xtrain, self.ytrain)

        #Puts code to sleep for 5 seconds to delay print
        time.sleep(5)

        #Results
        print('*****'*10)
        print('The best model score is {}'.format(search.best_score_*100))  
    
        #Generation of selected parameter table
        dfparameters = pd.DataFrame(search.cv_results_['params']) 
        dfTr_meanscores = pd.DataFrame(search.cv_results_['mean_train_score'], 
                               columns=['Train Accuracy'])
        dfTr_stdscores = pd.DataFrame(search.cv_results_['std_train_score'], 
                              columns=['Train Standard Dev'])
        dfTe_meanscores = pd.DataFrame(search.cv_results_['mean_test_score'], 
                               columns=['Cross-Validation Accuracy'])
        dfTe_stdscores = pd.DataFrame(search.cv_results_['std_test_score'], 
                              columns=['Cross-Validation Standard Dev'])
        modelscores = pd.concat([dfparameters, dfTr_meanscores, dfTr_stdscores, 
                              dfTe_meanscores, dfTe_stdscores], axis=1)
        modelscores = modelscores[modelscores['svm__gamma']>0.0]#Filters out    gamma<=0.0
        modelscores = modelscores[modelscores['Train Accuracy']>0.8]#Filters out poor trainers
        modelscores = modelscores[modelscores['Cross-Validation Accuracy']>0.90]#Filters out poor trainers

        #Re-index topscores for further use
        top_score = modelscores.sort_values(by=['Cross-Validation Accuracy', 'anova__k','pca__n_components'], 
                                    ascending=[False, True, True])

        top_score = top_score.reset_index() #Resets index for ease of selection
        top_score = top_score.drop(['index'], axis=1)
        print('Validate Top Selected Parameters at minimal 80% Train Accuracy')
        print('Initiate Validation data step')

        #Extracting Parameters from top_score
        name=top_score.columns[0:9]
        select=[]
        for i in top_score.columns[0:9]:
            select.append(top_score[i])#[0:100])
        
        #Setting list for cross-validation score on validation data
        scores=[]

        #Outer Cross validation
        cv_outer = cv_inner
        #Processing parameters through algorithm for best validation score.
        for i in range(0,(top_score.shape[0]), 1):
            pipe_assess = Pipeline([
                ('anova', SelectKBest(f_classif,k=select[8][i])),
                ('scaler', select[4][i]),
                ('pca', PCA(n_components=select[7][i], svd_solver=select[6][i],
                            whiten=select[5][i])),
                ('svm', SVC(C=select[3][i], gamma=select[2][i], 
                            kernel=select[1][i],probability=True,
                            random_state=select[0][i]))
                ])
            modeling=pipe_assess.fit(self.xtrain, self.ytrain)
            scores.append(modeling.score(self.xval, self.yval))

        #Adding validation score to table
        top_score['Validation Accuracy']=scores

        #Reorganizing output
        top_score=top_score.sort_values(by=['Validation Accuracy',
                                    'Train Accuracy',
                                    'anova__k',
                                    'Cross-Validation Accuracy',
                                    'pca__n_components'], 
                                     ascending = [False, False, True, False, False]) #False
        
        top_score = top_score[top_score['Validation Accuracy'] > 0.85]
        top_score = top_score.reset_index(drop = True)
        #top_score=top_score.drop('index', axis=1)
        print('Max Validation Accuracy', top_score['Validation Accuracy'].max()*100)
        
        self.top_score = top_score
        display(self.top_score)
        #Returns pandas DataFrame of all parameters
        return self
        
    
    def parameter_table(self,):

        return self.top_score

    def featuredisplay(self, toggle_interactive = False):
        """Displays ranking and scores for all features.
        
        Parameters:
        -----------
        toggle_interactive : True (default), boolean. Controls whether or not to activate matplotlib interactive window."""
        
        if toggle_interactive == True:
                get_ipython().run_line_magic('matplotlib', 'qt')
        else:
                get_ipython().run_line_magic('matplotlib', 'inline')

        self.score_table = self.top_score
        #self.xtrain = xtrain
        #self.ytrain = ytrain

        print('Total Nanosensor Frequency is: \n', 
        self.score_table['anova__k'].value_counts()/self.score_table.shape[0]   *100)

        #Visualizing most important sensors
        #Feature Selection
        bestfeatures = SelectKBest(score_func=f_classif, k='all')
        fit = bestfeatures.fit(self.xtrain, self.ytrain)
        dfscores = pd.DataFrame(fit.scores_)
        dfcolumns = pd.DataFrame(self.xtrain.columns)
        
        #concat two dataframes for better visualization 
        featureScores = pd.concat([dfcolumns,dfscores],axis=1)
        featureScores.columns = ['Sensor','Score']  #naming the dataframe columns
        display(featureScores.sort_values(by='Score', ascending=False))
        
        #Saving Feature Scores
        self.featureScores = featureScores

        #Plotting Feature Ranks
        fig, ax = plt.subplots()

        #Color palette form
        color_palette = "Greens_r" #@param ["viridis", "rocket", "mako", "crest", "light:seagreen", "light:seagreen_r", "light:b", "light:b_r", "dark:salmon", "dark:salmon_r", "Blues", "Blues_r", "YlOrBr", "tab10"] {allow-input: true}

        #plotting feature selection
        bar=sns.barplot(data=featureScores.sort_values('Score', ascending=False), x='Sensor', y='Score', palette=color_palette,
                linewidth=1.5,edgecolor=".1", saturation=1)

        ax.tick_params(direction='out', length=4, width=2, colors='k',
               grid_color='k', grid_alpha=1,grid_linewidth=2)

        #Setting Plot Spines Function
        def spines(top=True, right=True, bottom=True, left=True):
            """ If a value is True then the plot will have a spine
            in the respective position as defined by the function"""
            ax.spines['top'].set_visible(top)
            ax.spines['top'].set_color('k')
            ax.spines['top'].set_linewidth(2)
            ax.spines['right'].set_visible(right)
            ax.spines['right'].set_color('k')
            ax.spines['right'].set_linewidth(2)
            ax.spines['bottom'].set_visible(bottom)
            ax.spines['bottom'].set_color('k')
            ax.spines['bottom'].set_linewidth(2)
            ax.spines['left'].set_visible(left)
            ax.spines['left'].set_color('k')
            ax.spines['left'].set_linewidth(2)

        self.spines = spines(top=False,right=False)
        self.spines
        plt.ylim(-1, featureScores['Score'].max() + 10)
        plt.xlabel('nanosensors', fontsize=12, fontweight=False, color='k')
        plt.ylabel('importance score', fontsize=12, fontweight=False, color='k')
        plt.xticks(fontsize=12, fontweight=False, rotation=90)
        plt.yticks(fontsize=12, fontweight=False)
        plt.show()

        return self
    
    def featureselect(self, toggle_interactive = False):
        """Step wise breakdown for the selected features.
        
        Parameters:
        -----------

        toggle_interactive : True (default), boolean. Controls whether or not to activate matplotlib interactive window."""
        
        if toggle_interactive == True:
                get_ipython().run_line_magic('matplotlib', 'qt')
        else:
                get_ipython().run_line_magic('matplotlib', 'inline')

        fet_select=list(self.featureScores.sort_values(by=['Score'], 
        ascending=[False])[0:self.score_table['anova__k'][0]]['Sensor'])

        print('Selected Nanosensors are:', fet_select)
        self.fet_select = fet_select
        #Feature Conversion
        X_train_fet = self.xtrain[self.fet_select]
        X_val_fet = self.xval[self.fet_select]

        self.xtrainfet = X_train_fet
        self.xvalfet = X_val_fet
        
        def heatmap(x, y):
            df = x
            df['Label'] = y
            re = df.groupby('Label')[list(df.columns[0:])].mean()

            sns.set_style("whitegrid")
            plt.figure(figsize=(5, 5))
            sns.set(font_scale=1.05)
            color_bar_orientation = "horizontal" #@param ["vertical", "horizontal"]
            ax=sns.heatmap(re, cmap="Greens", linecolor='black',
               linewidths=1, cbar_kws={'label':r'$\Delta$F (a.u)',
                                             "orientation": color_bar_orientation,
                                             "aspect":20,
                                             'pad':0.005,
                                             }) 
            ax.xaxis.tick_top() # x axis on top
            ax.xaxis.set_label_position('top')
            ax.yaxis.tick_left()
            ax.yaxis.set_label_position('left')


            fontsize = 12 #@param {type:"slider", min:2, max:20, step:1}
            x_rotation =  45#@param {type:"number"}
            y_rotation =  0#@param {type:"number"}
            x_label = '' #@param {type:"string"}
            y_label = '' #@param {type:"string"}
            plt.xlabel(x_label, fontsize=fontsize,) #color='black',)
            plt.ylabel(y_label, fontsize=fontsize,)# color='black' )
            plt.xticks(fontsize=fontsize, rotation=x_rotation,)# color='black')
            plt.yticks(fontsize=fontsize, rotation=y_rotation,)# color='black')
            plt.show()
        #In order to use heatmap, copies of self must
        #be made or else the function merges the primary
        #self instances
        self.x = self.xtrainfet.copy()
        self.y = self.ytrain.copy()
        heatmap(self.x, self.y)
        return 

    def pca_transform(self):
        """Function for scaling the data and transforming through PCA determined by AGONS modeling."""
        #Setting Transformer for Scaling
        scaler=self.score_table['scaler'][0]
        self.scaler = scaler
        
        #Scaling data by top parameter
        xtrains = self.scaler.fit_transform(self.xtrainfet)
        xvals = self.scaler.transform(self.xvalfet)

        self.xtrains = xtrains
        self.xvals = xvals

        #Setting PCA
        pca = PCA(n_components=self.score_table['pca__n_components'][0],
                  svd_solver=self.score_table['pca__svd_solver'][0], 
                  whiten=self.score_table['pca__whiten'][0])
        self.pca = pca

        #Tranforming by PCA
        self.xtrainpca = self.pca.fit_transform(self.xtrains)
        self.xvalpca = self.pca.transform(self.xvals)

        #Setting up dataframes
        n = self.score_table['pca__n_components'][0]
        number_list = list(np.arange(1, n+1, 1))
        pca_list = []
        for n in number_list:
            pca_list.append('PCA: {}'.format(n))

        self.pcatrain=pd.DataFrame(self.xtrainpca, columns=pca_list).reset_index(drop = True)
        self.pcatrain['Label']=self.ytrain.reset_index(drop = True)
        self.pcatrain = self.pcatrain.sort_values(by='Label', ascending=True)

        self.pcaval=pd.DataFrame(self.xvalpca, columns=pca_list).reset_index(drop = True)
        self.pcaval['Label']=self.yval.reset_index(drop=True)
        self.pcaval = self.pcaval.sort_values(by='Label', ascending=True)
    
        return self
    
    def pca_diagnostic(self, toggle_interactive = False):
        """
        Function for plotting the cumalitive explained variance for each number of PCA components.

        Parameters
        ----------
        toggle_interactive : False (default), boolean. Controls whether or not to activate matplotlib interactive window."""
        if toggle_interactive == True:
                get_ipython().run_line_magic('matplotlib', 'qt')
        else:
                get_ipython().run_line_magic('matplotlib', 'inline')

        sns.set_style('ticks')
        self.pca_diag=PCA(whiten=self.score_table['pca__whiten'][0]).fit(self.xtrains)
        fig, ax = plt.subplots()
        sns.lineplot(x=np.arange(1, len(np.cumsum(self.pca_diag.explained_variance_ratio_))+1, 1), 
        y=np.cumsum(self.pca_diag.explained_variance_ratio_)*100, color='k', linewidth=2.5)

        ax.tick_params(direction='out', length=5, width=3, colors='k',
               grid_color='k', grid_alpha=1,grid_linewidth=2)
        plt.xticks(fontsize=12, fontweight=None)
        plt.yticks(fontsize=12, fontweight=None)

        plt.xlabel('number of components', fontsize=12, 
                    fontweight=None, color='k')
        plt.ylabel('cumulative explained variance (%)', 
                    fontsize=12, fontweight=None, color='k')
        print('PCA cumulative explained variance values',
                    np.cumsum(self.pca_diag.explained_variance_ratio_))

        self.spines
        plt.show()
        return self
    
    def pca2D(self, loadings = False, toggle_interactive = False):

        """Visualize PCA sepration at 2D for training data.
        
        Parameters
        ----------
        loadings : False (default), boolean. Controls whether to show how each feature controls the PCA directionality and correlation.
        
        toggle_interactive : False (default), boolean. Controls whether or not to activate matplotlib interactive window.
        """

        self.loadings = loadings
        self.pca1=self.pca_diag.explained_variance_ratio_[0]
        self.pca2=self.pca_diag.explained_variance_ratio_[1]

        if toggle_interactive == True:
                get_ipython().run_line_magic('matplotlib', 'qt')
        else:
                get_ipython().run_line_magic('matplotlib', 'inline')

        def myplot(score, vector, loadings = False, pca1 = self.pca1, 
                    pca2 = self.pca2, fet_col = self.xtrainfet):
    
            xvector = self.pca.components_[0] 
            yvector = self.pca.components_[1]
            xs = score['PCA: 1']
            ys = score['PCA: 2']

            fig, ax = plt.subplots()
            sns.scatterplot(x='PCA: 1', y='PCA: 2', hue='Label',
                palette=sns.color_palette('bright', score['Label'].nunique()),   
                data=score,
                linewidth=0,
                s=75,
                legend='full')

            if loadings ==True:
                for i in range(len(xvector)):
            # arrows project features (ie columns from csv) as vectors onto PC axes
                    plt.arrow(0, 0, xvector[i]*max(xs), yvector[i]*max(ys),
                        color='k', width=0.0005, head_width=0.0025)
                    plt.text(xvector[i]*max(xs)*1.2, yvector[i]*max(ys)*1.2,
                        list(fet_col.columns)[i], color='k')
            else:
                pass

            #Set labels
            plt.xlim(score['PCA: 1'].min() + (score['PCA: 1'].min()*.25), score['PCA: 1'].max() + (score['PCA: 1'].max()*.25))
            plt.ylim(score['PCA: 2'].min() + (score['PCA: 2'].min()*.25), score['PCA: 2'].max() + (score['PCA: 2'].max()*.25))
            round_pca1 = 3 #@param {type:"integer"}
            round_pca2 = 3 #@param {type:"integer"}
            plt.xlabel("PC1 {}%".format(round(pca1, round_pca1)*100),
               fontsize=12,color='k', fontweight= False)
            plt.ylabel("PC2 {}%".format(round(pca2, round_pca2)*100),
               fontsize=12,color='k', fontweight= False)
            #Set ticks
            plt.xticks(fontsize=12,color='k', fontweight=False)
            plt.yticks(fontsize=12,color='k', fontweight=False)
            plt.legend(fontsize='medium',bbox_to_anchor=(1.00, 1), loc='upper left')
            plt.axvline(0, color='k',linestyle='dashed')
            plt.axhline(0, color='k',linestyle='dashed')
    
                #Call the function. Use only the 2 PCs.
        myplot(self.pcatrain, np.transpose(self.pca.components_[0:2, :]),
                loadings = self.loadings, pca1 = self.pca1, pca2 = self.pca2, fet_col = self.xtrainfet)
        plt.show()
        return self

    def pca3D(self, toggle_interactive =True):
    
        """Function for plotting a 3D PCA plot if
           PCA components are greater than or equal
           to three.
           
           Parameters
           ----------
           toggle_interactive : True (default), boolean. Controls whether or not to activate matplotlib interactive window."""

        if self.pcatrain.shape[1] >= 3:
            if toggle_interactive == True:
                get_ipython().run_line_magic('matplotlib', 'qt')
            else:
                pass

            #Variables for plot loop
            pca_lab = list(self.pcatrain['Label'].unique())
            markers = ['o', '^', 'v', 'D', 's', 'X', 'p', '+', 'X', '8', '<', '>']
            coloring= ['blue', 'red', 'lime', 'purple', 'yellow', 'hotpink', 
                     'black', 'darkorange', 'cyan']

            #Grouping and plotting loop
            fig=plt.figure(figsize=(7,7))
            axes = plt.subplot(111, projection='3d')
            for i, j, h in zip(pca_lab, markers, coloring):
              grouper = self.pcatrain.groupby('Label')
              setter = grouper.get_group(i)
              x=setter['PCA: 1']
              y=setter['PCA: 2']
              z=setter['PCA: 3']
              axes.scatter(x, y, z, label=i, marker=j, c=h, 
                        s=40, edgecolors='black', alpha=1)

            #Dashed 0 line z axis
            xz=[0, 0]
            yz=[0, 0]
            zz=[self.pcatrain['PCA: 3'].min(), self.pcatrain['PCA: 3'].max()]
            axes.plot(xz, yz, zz, c='black', linestyle='dashed')
            #Dashed 0 line x axis
            xx=[self.pcatrain['PCA: 1'].min(),self.pcatrain['PCA: 1'].max()]
            yx=[0,0]
            zx=[0,0]
            axes.plot(xx, yx, zx, c='black', linestyle='dashed')
            #Dashed 0 line y axis
            xy=[0,0]
            yy=[self.pcatrain['PCA: 2'].min(),self.pcatrain['PCA: 2'].max()]
            zy=[0,0]
            axes.plot(xy, yy, zy, c='black', linestyle='dashed')

            #Setting background panes
            axes.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
            axes.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
            axes.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

            #setting grid line color #RGB Scale
            axes.xaxis._axinfo["grid"]['color'] = (1,1,1,1) 
            axes.yaxis._axinfo["grid"]['color'] = (1,1,1,1)
            axes.zaxis._axinfo["grid"]['color'] = (1,1,1,1)

            #Setting plot limits
            axes.set_xlim3d(round(self.pcatrain['PCA: 1'].min(),1), 
                          round(self.pcatrain['PCA: 1'].max(),1))
            axes.set_ylim3d(round(self.pcatrain['PCA: 2'].min(),1), 
                          round(self.pcatrain['PCA: 2'].max(),1))
            axes.set_zlim3d(round(self.pcatrain['PCA: 3'].min(),1), 
                          round(self.pcatrain['PCA: 3'].max(),1))

            #Setting Labels
            self.pca3=self.pca_diag.explained_variance_ratio_[2]

            round_pca1 = 3 #@param {type:"integer"}
            round_pca2 = 3 #@param {type:"integer"}
            round_pca3 = 3 #@param {type:"integer"}
            axes.set_xlabel("PC1 {}%".format(round((self.pca1*100), round_pca1)),#pca.       explained_variance_ratio_[0],2)*100),
                         fontsize=12,color='k', fontweight= False, labelpad=5)
            axes.set_ylabel("PC2 {}%".format(round((self.pca2*100), round_pca2)),
                         fontsize=12,color='k', fontweight= False, labelpad=7)
            axes.set_zlabel("PC3 {}%".format(round((self.pca3*100), round_pca3)),
                         fontsize=12,color='k', fontweight= False, labelpad=7)
            #Set legend
            horizontal = 0.5 #@param {type:"number"}
            vertical =  -0.4#@param {type:"number"}
            plt.legend(loc="best", bbox_to_anchor=(horizontal, vertical,1,1))
            plt.show()
            return

    def set_final_model(self, model_params = 'best', x_fit = None, y_fit = None):
        """ Fit the model to be used for unknown prediction.
        Parameters:
        -----------
        model_params : str or dict, if 'best' uses the top performing model selected by AGONS from parameter_table attribute. Else, insert a dict using parameter_table attribute .iloc[row, 0:9].to_dict() to select a different parameter subset.
        
        x_fit : DataFrame or numpy array, used to fit the final decided model.y_fit : DataFrame, series or numpy array, used to fit the final decided model."""

        self.model_params = model_params
        self.x_fit = x_fit
        self.y_fit = y_fit

        if self.model_params == 'best':

            self.model_params = self.top_score.iloc[0, 0:9].to_dict()
        
        else:
            pass


        pipe = Pipeline([
                ('anova', SelectKBest(f_classif)),
                ('scaler', MinMaxScaler()),
                ('pca', PCA()),
                ('svm', SVC(probability=True))
                ])
        
        self.final_model = pipe.set_params(**self.model_params)
        self.final_model = self.final_model.fit(self.x_fit, self.y_fit)

    def predict(self, xtest, ytest):

        self.xtest = xtest
        self.ytest = ytest

        self.ypred = self.final_model.predict(xtest)

        return self.ypred
    
    def predict_probe(self, xtest, ytest):

        self.xtest = xtest
        self.ytest = ytest

        self.ypred_prob = self.final_model.predict_proba(xtest)

        return self.ypred_prob


# %%
