import numpy as np
import pandas as pd
import pandas_profiling
import statsmodels.stats.outliers_influence as oi
from sklearn.linear_model import LinearRegression, ElasticNet, ElasticNetCV, Lasso, LassoCV, Ridge, RidgeCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class DataPreprocessingLrModel:

    '''This module standardizing the data and checking multicolinearity and then building linear model
    and making predictions based on a given set of parameters such as url of dataset, name of column values of
    which we want to predict and index column of a dataset'''

    def __init__(self, dataset_url, y_name, index_col_):
        self.origin_df = pd.read_csv(dataset_url, index_col = index_col_)
        self.df = self.origin_df.copy()
        self.y_name = y_name
        self.y = self.df[y_name]
        self.regr = None
        self.x_test = None
        self.x_train = None
        self.y_test = None
        self.y_train = None
        self.dropped_col_multicol = []
        self.dropped_col_cat = []
        self.scaler = None

    def remove_categorial_columns(self):
        '''removing categorical columns of a given dataset'''
        num_cols = self.df._get_numeric_data().columns
        categorial_cols = list(set(self.df.columns) - set(num_cols))
        self.df.drop(columns = categorial_cols, inplace = True)
        self.dropped_col_cat.extend(categorial_cols)

    def handle_missing_values(self):
        '''replacing missing data by mean of a column'''
        missing_val_col = self.df.columns[self.df.isnull().any()].tolist()
        for i in missing_val_col:
            self.df[i] = self.df[i].fillna(self.df[i].mean())

    def standartization(self):
        '''standartization of a dataset columns without y'''
        scaler = StandardScaler()
        x = self.df.drop(columns = self.y_name)
        arr = scaler.fit_transform(x)
        x_ = pd.DataFrame(arr, columns = x.columns)
        self.scaler = scaler
        return arr,x_

    def multicolinearity_check(self, arr, x):
        '''checking multicolinearity based on variance inflation factor
        and removing columns which are multicolinear'''
        vif = [oi.variance_inflation_factor(arr,i) for i in range(arr.shape[1])]
        for i,col in zip(vif,x.columns):
            if i > 10:
                x.drop(columns = col, inplace = True)
                self.dropped_col_multicol.append(col)
        return x

    def process_data(self):
        self.remove_categorial_columns()
        self.handle_missing_values()
        arr, x = self.standartization()
        x_ = self.multicolinearity_check(arr, x)
        return x_,self.y

    def build_regression(self, train_size_=0.2, random_state_=100, type = 'linear', cv_ = 5, max_iter_ = 2000000):
        x, y = self.process_data()
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_size_, random_state=random_state_)
        if type == "linear":
            regr = LinearRegression()
            regr.fit(x_train,y_train)
        elif type == "lasso":
            lassocv = LassoCV(alphas=None, cv=cv_, max_iter=max_iter_)
            lassocv.fit(x_train, y_train)
            regr = Lasso(alpha=lassocv.alpha_)
            regr.fit(x_train,y_train)
        elif type == "ridge":
            ridgecv = RidgeCV(alphas = np.random.uniform(0,10,50), cv = cv_)
            ridgecv.fit(x_train, y_train)
            regr = Ridge(alpha = ridgecv.alpha_)
            regr.fit(x_train, y_train)
        elif type == "elasticnet":
            elasticnetcv = ElasticNetCV(alphas = None, cv=cv_)
            elasticnetcv.fit(x_train, y_train)
            regr = ElasticNet(alpha=elasticnetcv.alpha_, l1_ratio=elasticnetcv.l1_ratio_)
            regr.fit(x_train, y_train)
        self.regr = regr
        self.x_train = x_train
        self.x_test = x_test
        self.y_test = y_test
        self.y_train = y_train

    def regression_score(self):
        return self.regr.score(self.x_test, self.y_test)

    def get_profile_report(self):
        pr = pandas_profiling.ProfileReport(df = self.origin_df)
        pr.to_file('profile.html')

    def predict(self, test_data):
        if self.regr is not None:
            x = self.origin_df.drop(columns = self.y_name)
            d = dict(zip(x.columns,test_data))
            for i in self.dropped_col_cat:
               del d[i]
            test_data = self.scaler.transform([list(d.values())])
            i = 0
            for k in d.keys():
                d[k] = test_data[0][i]
                i+=1
            for i in self.dropped_col_multicol:
                del d[i]
            return self.regr.predict([list(d.values())])
        else:
            return "Create firstly linear regression model"


