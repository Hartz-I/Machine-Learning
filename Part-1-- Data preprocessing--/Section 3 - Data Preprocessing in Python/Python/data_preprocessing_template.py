#importing the libraries

import numpy as np #use mathematics
import matplotlib.pyplot as plt #plot nice charts
import pandas as pd #to import and manage datasets

#import a dataset
#navigate to working directory in the right side
#this python file has to be into the file where dataset is

dataset=pd.read_csv('Data.csv')

#now we create the independent variable matrix with vectors
#matrix of features
x=dataset.iloc[:, :-1].values #left is all the lines. right is all the columns execpt -1!
y=dataset.iloc[:, -1] #or we could have put 3. as index of 4th column is 3

#Taking care of the missing data!
#replacing them with mean!
from sklearn.preprocessing import Imputer #allow us to take care of the missing data. 
#dklearn is sikick learn