def index():
    print("""

Link: https://bit.ly/ricpract2022

1a) Write a program for obtaining descriptive statistics of data
1b) Import data from different data sources (from Excel, csv, mysql, sql server, oracle to R/Python/Excel)

3a) Perform Testing of Hypothesis using one sample t-test
3b) Perform Testing of Hypothesis using two sample t-test
3c) Perform Testing of Hypothesis using paired sample t-test

4b) Perform Testing of Hypothesis using chi-squared test of independence

5) Perform Testing of Hypothesis using z-test

6a) Perform Testing of Hypothesis using one-way ANOVA
6b) Perform Testing of Hypothesis using two-way ANOVA
6c) Perform Testing of Hypothesis using multivariate ANOVA(MANOVA)

7b) Perform the Stratified sampling for the given data and analyse it

8) Compute different types of correlation

9a) Perform linear regression for prediction
9b) Perfrom Polynomial regression for prediction

          """)
          



def prog(num):
    if(num=="1a"):
        print(""" 

import pandas as pd
import pandas as pd
df = pd.DataFrame({'Age':[25,26,25,23,30,29,23,34,40,30,51,46] ,
                   'Rating':[4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65]})
print(df)

print ("Sum",df.sum())
print ("Mean",df.mean())
print ("Standard Deviation",df.std())

print('############ Descriptive Statistics ########## ')
print ("Descriptive Statistics",df.describe())

              """) 

        
    elif(num=="1b"):
        print("""

#SQLite

import sqlite3 as sq
import pandas as pd

sDatabaseName='vermeulen.db'
conn = sq.connect(sDatabaseName)

sFileName='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve_IP_DATA.csv'
print('Loading :',sFileName)

IP_DATA_ALL_FIX=pd.read_csv(sFileName,
                            header=0,
                            low_memory=False)
IP_DATA_ALL_FIX.index.names = ['RowIDCSV']

sDatabaseName='vermeulen.db'
sTable='IP_DATA_ALL'
print('Storing :',sDatabaseName,' Table:',sTable)
IP_DATA_ALL_FIX.to_sql(sTable, conn, if_exists="replace")
print('Loading :',sDatabaseName,' Table:',sTable)

TestData=pd.read_sql_query("select * from IP_DATA_ALL;", conn)
print('################')
print('## Data Values')
print('################')
print(TestData)
print('################')
print('## Data Profile')
print('################')
print('Rows :',TestData.shape[0])
print('Columns :',TestData.shape[1])
print('################')
print('### Done!! ############################################')



#MySQL

################ Connection With MySQL ######################
import mysql.connector
conn = mysql.connector.connect(host='localhost',
database='DataScience',
user='root',
password='root')
conn.connect
if(conn.is_connected):
    print('###### Connection With MySql Established Successfullly ##### ')
else:
    print('Not Connected -- Check Connection Properites')



#Excel

import pandas as pd

sFileDir='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python'

CurrencyRawData = pd.read_excel('C:/VKHCG/01-Vermeulen/00-RawData/Country_Currency.xlsx')
sColumns = ['Country or territory', 'Currency', 'ISO-4217']
CurrencyData = CurrencyRawData[sColumns]
CurrencyData.rename(columns={'Country or territory': 'Country', 
                             'ISO-4217':'CurrencyCode'}, 
                    inplace=True)
CurrencyData.dropna(subset=['Currency'],inplace=True)
CurrencyData['Country'] = CurrencyData['Country'].map(lambda x: x.strip())
CurrencyData['Currency'] = CurrencyData['Currency'].map(lambda x: x.strip())
CurrencyData['CurrencyCode'] = CurrencyData['CurrencyCode'].map(lambda x: x.strip())
print(CurrencyData)
print('~~ Data from Excel Sheet Retrived Successfully ~~~ ')

sFileName='C:/VKHCG/01-Vermeulen/01-Retrieve/01-EDS/02-Python/Retrieve-Country-Currency.csv'
CurrencyData.to_csv(sFileName, index = False)

                """)
        

    elif(num=="3a"):
        print("""

from scipy.stats import ttest_1samp
import numpy as np
ages = np.genfromtxt('ages.csv')
print(ages)

ages_mean = np.mean(ages)
print(ages_mean)
tset, pval = ttest_1samp(ages, 30)
print('p-values - ',pval)

if pval < 0.05: 
  print("we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")


                """)


    elif(num=="3b"):
        print("""

import numpy as np
from scipy import stats
from numpy.random import randn
N = 20
#a = [35,40,12,15,21,14,46,10,28,48,16,30, 32,48,31,22,12,39,19,25]
#b = [2,27,31,38,1,19,1,34,3,1,2,1,3,1,2,1,3,29,37,2]

a = 5 * randn(100) + 50
b = 5 * randn(100) + 51
var_a = a.var(ddof=1)
var_b = b.var(ddof=1)
s = np.sqrt((var_a + var_b)/2)
t = (a.mean() - b.mean())/(s*np.sqrt(2/N))
df = 2*N - 2

#p-value after comparison with the t
p = 1 - stats.t.cdf(t,df=df)
print("t = " + str(t))
print("p = " + str(2*p))

if t> p : 
  print('Mean of two distribution are differnt and significant')
else:
  print('Mean of two distribution are same and not significant')


                """)


    elif(num=="3c"):
        print("""

from scipy import stats
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv("/content/blood_pressure.csv")

print(df[['bp_before','bp_after']].describe())

#First let’s check for any significant outliers in #each of the variables.
df[['bp_before', 'bp_after']].plot(kind='box') 

# This saves the plot as a png file 
plt.savefig('boxplot_outliers.png')

# make a histogram to differences between the two scores. 
df['bp_difference'] = df['bp_before'] - df['bp_after']
df['bp_difference'].plot(kind='hist', title= 'Blood Pressure Difference Histogram')

#Again, this saves the plot as a png file
plt.savefig('blood pressure difference histogram.png') 
stats.probplot(df['bp_difference'], plot= plt) 
plt.title('Blood pressure Difference Q-Q Plot')

from scipy import stats
import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv("blood_pressure.csv")

print(df[['bp_before','bp_after']].describe())

#First let's check for any significant outliers in #each of the variables.
df[['bp_before', 'bp_after']].plot(kind='box') 

# This saves the plot as a png file 
plt.savefig('boxplot_outliers.png')

# make a histogram to differences between the two scores. 
df['bp_difference'] = df['bp_before'] - df['bp_after']
df['bp_difference'].plot(kind='hist', title= 'Blood Pressure Difference Histogram')

#Again, this saves the plot as a png file
plt.savefig('blood pressure difference histogram.png')

stats.probplot(df['bp_difference'], plot= plt) 
plt.title('Blood pressure Difference Q-Q Plot')
plt.savefig('Blood pressure Difference Q-Q Plot.png')

tset, pval = stats.ttest_rel(df['bp_before'], df['bp_after'])
print('p-value: ',pval)

if pval < 0.05: 
  print("we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

                """)



    elif(num=="4b"):
        print("""

import numpy as np 
import pandas as pd 
import scipy.stats as stats

np.random.seed(10)
stud_grade = np.random.choice(a=["O","A","B","C","D"], p=[0.20, 0.20 ,0.20, 0.20, 0.20], size=100)
stud_gen = np.random.choice(a=["Male","Female"], p=[0.5, 0.5], size=100) 

mscpart1 = pd.DataFrame({"Grades":stud_grade, "Gender":stud_gen}) 
print(mscpart1)

stud_tab = pd.crosstab(mscpart1.Grades, mscpart1.Gender, margins=True) 
stud_tab.columns = ["Male", "Female", "row_totals"]

stud_tab.index = ["O", "A", "B", "C", "D", "col_totals"] 
observed = stud_tab.iloc[0:5, 0:2 ]
print(observed)

expected = np.outer(stud_tab["row_totals"][0:5], stud_tab.loc["col_totals"][0:2]) / 100 
print(expected)

chi_squared_stat = (((observed-expected)**2)/expected).sum().sum() 
print('Calculated : ',chi_squared_stat)

crit = stats.chi2.ppf(q=0.95, df=4) 
print('Table Value : ',crit)

if chi_squared_stat>= crit: 
  print('H0 is Accepted ')
else:
  print('H0 is Rejected ')

                """)



    elif(num=="5"):
        print("""

#Install this: python -m pip install statsmodels if error

###one-sample Z test.###
import statsmodels.stats.weightstats as stests
import pandas as pd

df = pd.read_csv("blood_pressure.csv")
df[['bp_before','bp_after']].describe()
print(df)

ztest ,pval = stests.ztest(df['bp_before'], 
                           x2=None, 
                           value=156)
print(float(pval))

if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")


####Two-sample Z test###
import statsmodels.stats.weightstats as stests
import pandas as pd

df = pd.read_csv("blood_pressure.csv")
df[['bp_before','bp_after']].describe()
print(df)

ztest ,pval = stests.ztest(df['bp_before'], 
                           x2=df['bp_after'], 
                           value=0,
                           alternative='two-sided')
print(float(pval))

if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")




                """)



    elif(num=="6a"):
        print("""

#Run this code in spyder


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
data = pd.read_csv("scores.csv")
data.head()
data['Borough'].value_counts()
data['total_score'] = data['Average Score (SAT Reading)'] + \
data['Average Score (SAT Math)'] + \
data['Average Score (SAT Writing)']
data = data[['Borough', 'total_score']].dropna()
x = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
district_dict = {}
#Assigns each test score series to a dictionary key
for district in x: 
  district_dict[district] = data[data['Borough'] == district]['total_score']
y = []
yerror = []
#Assigns the mean score and 95% confidence limit to each district
for district in x:
  y.append(district_dict[district].mean())
  yerror.append(1.96*district_dict[district].std()/np.sqrt(district_dict[district].shape[0]))
print(district + '_std : {}'.format(district_dict[district].std()))
sns.set(font_scale=1.8)
fig = plt.figure(figsize=(10,5))
ax = sns.barplot(x, y, yerr=yerror)
ax.set_ylabel('Average Total SAT Score')
plt.show()
print(stats.f_oneway(
district_dict['Brooklyn'], district_dict['Bronx'], \
district_dict['Manhattan'], district_dict['Queens'], \
district_dict['Staten Island']))
districts = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
ss_b = 0
for d in districts:
  ss_b += district_dict[d].shape[0] * \
  np.sum((district_dict[d].mean() - data['total_score'].mean())**2)
ss_w = 0
for d in districts:
  ss_w += np.sum((district_dict[d] - district_dict[d].mean())**2)
msb = ss_b/4
msw = ss_w/(len(data)-5)
f=msb/msw
print('F_statistic: {}'.format(f))
ss_t = np.sum((data['total_score']-data['total_score'].mean())**2)
eta_squared = ss_b/ss_t
print('eta_squared: {}'.format(eta_squared))     


                """)



    elif(num=="6b"):
        print("""

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
from scipy import stats
def eta_squared(aov):
 aov['eta_sq'] = 'NaN'
 aov['eta_sq'] = aov[:-1]['sum_sq']/sum(aov['sum_sq'])
 return aov
def omega_squared(aov):
 mse = aov['sum_sq'][-1]/aov['df'][-1]
 aov['omega_sq'] = 'NaN'
 aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*mse))/(sum(aov['sum_sq'])+mse)
 return aov
datafile = "ToothGrowth.csv"
data = pd.read_csv(datafile)
fig = interaction_plot(data.dose, data.supp, data.len, colors=['red','blue'], markers=['D','^'], ms=10)
N = len(data.len)
df_a = len(data.supp.unique()) - 1
df_b = len(data.dose.unique()) - 1
df_axb = df_a*df_b
df_w = N - (len(data.supp.unique())*len(data.dose.unique()))
grand_mean = data['len'].mean()
#Sum of Squares A – supp
ssq_a = sum([(data[data.supp ==l].len.mean()-grand_mean)**2 for l in data.supp])
#Sum of Squares B – supp
ssq_b = sum([(data[data.dose ==l].len.mean()-grand_mean)**2 for l in data.dose])
#Sum of Squares Total
ssq_t = sum((data.len - grand_mean)**2)
vc = data[data.supp == 'VC']
oj = data[data.supp == 'OJ']
vc_dose_means = [vc[vc.dose == d].len.mean() for d in vc.dose]
oj_dose_means = [oj[oj.dose == d].len.mean() for d in oj.dose]
ssq_w = sum((oj.len - oj_dose_means)**2) +sum((vc.len - vc_dose_means)**2)
ssq_axb = ssq_t-ssq_a-ssq_b-ssq_w
ms_a = ssq_a/df_a #Mean Square A
ms_b = ssq_b/df_b #Mean Square B
ms_axb = ssq_axb/df_axb #Mean Square AXB
ms_w = ssq_w/df_w
f_a = ms_a/ms_w
f_b = ms_b/ms_w
f_axb = ms_axb/ms_w
p_a = stats.f.sf(f_a, df_a, df_w)
p_b = stats.f.sf(f_b, df_b, df_w)
p_axb = stats.f.sf(f_axb, df_axb, df_w)
results = {'sum_sq':[ssq_a, ssq_b, ssq_axb, ssq_w],
 'df':[df_a, df_b, df_axb, df_w],
 'F':[f_a, f_b, f_axb, 'NaN'],
 'PR(>F)':[p_a, p_b, p_axb, 'NaN']}
columns=['sum_sq', 'df', 'F', 'PR(>F)']
aov_table1 = pd.DataFrame(results, columns=columns,
 index=['supp', 'dose', 'supp:dose', 'Residual'])
formula = 'len ~ C(supp) + C(dose) + C(supp):C(dose)'
model = ols(formula, data).fit()
aov_table = anova_lm(model, typ=2)
eta_squared(aov_table)
omega_squared(aov_table)
print(aov_table.round(4))
res = model.resid
fig = sm.qqplot(res, line='s')
plt.show()


                """)



    elif(num=="6c"):
        print("""
#Execute one line at a time in Spyder
              
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
df = pd.read_csv("iris.csv", index_col=0)
df.columns = df.columns.str.replace(".", "_")
df.head()
print('~~~~~~~~ Data Set ~~~~~~~~')
print(df)
maov = MANOVA.from_formula('Sepal_Length + Sepal_Width + Petal_Length + Petal_Width ~ Species', data=df)
print('~~~~~~~~ MANOVA Test Result ~~~~~~~~')
print(maov.mv_test())



                """)




    elif(num=="7b"):
        print("""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')

housing =pd.read_csv("housing.csv")
print(housing.head())
print(housing.info())
correlation_matrix = housing.corr()
plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, center=0, annot=True, linewidths=.3)
corr =housing.corr()
print(corr['median_house_value'].sort_values(ascending=False))
sns.displot(housing.median_income)
plt.show()


                """)





    elif(num=="8"):
        print("""


#Positive correlation

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
# Positive Correlation with some noise
y = x + np.random.normal(0, 5, 1000)
np.corrcoef(x, y)
plt.style.use('ggplot')
plt.scatter(x, y)
plt.show()

#Negative correlation

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
# Negative Correlation with some noise
y = 100 - x + np.random.normal(0, 5, 1000)
np.corrcoef(x, y)
plt.scatter(x, y)
plt.show()

#No/Weak Correlation

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)
np.corrcoef(x, y)
plt.scatter(x, y)
plt.show()


                """)




    elif(num=="9a"):
        print("""

#pip3 install -U scikit-learn scipy matplotlib
#if sklearn doesn't work

import quandl, math
import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
style.use('ggplot')
df = quandl.get("WIKI/GOOGL")
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
 next_date = datetime.datetime.fromtimestamp(next_unix)
 next_unix += 86400
 df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


                """)





    elif(num=="9b"):
        print("""

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
  # number of observations/points
  n = np.size(x)

  # mean of x and y vector
  m_x, m_y = np.mean(x), np.mean(y)

  # calculating cross-deviation and deviation about x
  SS_xy = np.sum(y*x) - n*m_y*m_x
  SS_xx = np.sum(x*x) - n*m_x*m_x

  # calculating regression coefficients
  b_1 = SS_xy / SS_xx
  b_0 = m_y - b_1*m_x

  return(b_0, b_1)

def plot_regression_line(x, y, b):
  # plotting the actual points as scatter plot
  plt.scatter(x, y, color = "m",
  marker = "o", s = 30)

  # predicted response vector
  y_pred = b[0] + b[1]*x

  # plotting the regression line
  plt.plot(x, y_pred, color = "g")

  # putting labels
  plt.xlabel('x')
  plt.ylabel('y')

  # function to show plot

  plt.show()

def main():
  # observations
  x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
  # estimating coefficients
  b = estimate_coef(x, y)
  print("Estimated coefficients:b_0 = {} b_1 = {}".format(b[0], b[1]))
  # plotting regression line
  plot_regression_line(x, y, b)

if __name__ == "__main__":
   main()


                """)


    else:
        print("invalid input")



