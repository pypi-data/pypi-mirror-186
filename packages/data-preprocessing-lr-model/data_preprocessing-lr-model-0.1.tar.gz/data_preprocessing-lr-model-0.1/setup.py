from setuptools import setup

setup(name = "data_preprocessing-lr-model", version = "0.1", description="Deleting categorical variables, standardizing variables,"
    " checking multicolinearity and then building linear regression model (or ridge, lasso, elasticnet) and"
    " making predictions on her", packages=['data_preprocessing_lr_model'], zip_safe = False)