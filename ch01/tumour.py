import pandas as pd
df_train=pd.read_csv('D:/breast-cancer-train.csv')
df_test=pd.read_csv('D:/breast-cancer-test.csv')
df_test_negative=df_test.loc[df_test['Type']==0][['Clump Thickness','Cell Size']]
df_test_positive=df_test.loc[df_test['Type']==0][['Clump Thickness','Cell Size']]

import matplotlib.pyplot as plt
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],maker='o',s=200,c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_negative['Cell Size'],maker='x',s=150,c='black')

plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()

import numpy as np
intercept=np.random.random([1])
coef=np.random.random([2])
lx=np.arange(0,12)
ly=(-intercept-lx*coef[0])/coef[1]
plt.plot(lx,ly,c='yellow')

plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],marker='o',s=200,c='red')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'],marker='x',s=150,c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()




