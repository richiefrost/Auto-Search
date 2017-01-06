import pandas as pd
import numpy as np

# Using multivariate regression
def getAlpha(X, y):
	return y * np.matrix.transpose(X)*np.linalg.inv((X * np.matrix.transpose(X)))

def fromAlphas(alphas, xarr):
	return alphas[0,0] + alphas[0,1] * xarr[0] + alphas[0,2] * xarr[1]

# Try to predict how much to charge for our BMW
data = pd.read_json('ksl_auto/bmw3.json')
year = data['year']
mileage = data['mileage']
price = data['price']

X = np.matrix([[1 for i in range(len(year))], year, mileage])
Y = np.matrix(price)

alphas = getAlpha(X, Y)
print(alphas)
my_year = 2003
my_mileage = 124000

my_price = fromAlphas(alphas, [my_year, my_mileage])
#print(my_price)
print("We should charge {0}".format('{:0.2f}'.format(my_price)))
