# coding: utf-8

# # Simple Linear Regression and Multiple Regression
# 
# This notebook contains step-by-step directions for Project Three. It is very important to run through the steps in order. Some steps depend on the outputs of earlier steps. Once you have completed the steps in this notebook, be sure to write your summary report. 
# 
# You are a data analyst for a basketball team and have access to a large set of historical data that you can use to analyze performance patterns. The coach of the team and your management have requested that you come up with regression models that predict the total number of wins for a team in the regular season based on key performance metrics. Although the data set is the same that you used in the previous projects, the data set used here has been aggregated to study the total number of wins in a regular season based on performance metrics shown in the table below. These regression models will help make key decisions to improve the performance of the team. You will use the Python programming language to perform the statistical analyses and then prepare a report of your findings to present for the team’s management. Since the managers are not data analysts, you will need to interpret your findings and describe their practical implications. 
#  
# ## Step 1: Data Preparation
# This step uploads the data set from a CSV file and transforms the data into a form that will be used to create regression models. The data will be aggregated to calculate the number of wins for teams in a basketball regular season between the years 1995 and 2015. 
# 

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# dataframe for this project
nba_wins_df = pd.read_csv('nba_wins_data.csv')

display(HTML(nba_wins_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(nba_wins_df))

# ## Step 2: Scatterplot and Correlation for the Total Number of Wins and Average Relative Skill
# Your coach expects teams to win more games in a regular season if they have a higher average relative skill compared to their opponents. This is because the chances of winning are higher if a team can maintain high average relative skill. Therefore, it is expected that the total number of wins and the average relative skill are correlated. Calculate the Pearson correlation coefficient and its P-value. 
# 1. <font color='red'> Replace <strong>??DATAFRAME_NAME??</strong> with the name of the dataframe used in this project. </font> See Step 1 for the name of dataframe used in this project. 
# 
# 2. <font color='red'> Replace <strong>??RELATIVE_SKILL??</strong> with the name of the variable for average relative skill.</font> 
# 
# 3. <font color='red'> Replace <strong>??WINS??</strong> with the name of the variable for the total number of wins in a regular season. Remember to enclose the variable in single quotes.</font> 
#
import scipy.stats as st

plt.plot(??DATAFRAME_NAME??[??RELATIVE_SKILL??], ??DATAFRAME_NAME??[??WINS??], 'o')

plt.title('Total Number of Wins by Average Relative Skill', fontsize=20)
plt.xlabel('Average Relative Skill')
plt.ylabel('Total Number of Wins')
plt.show()

correlation_coefficient, p_value = st.pearsonr(??DATAFRAME_NAME??[??RELATIVE_SKILL??], ??DATAFRAME_NAME??[??WINS??])

print("Correlation between Average Relative Skill and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", round(p_value,4))


# ## Step 3: Simple Linear Regression: Predicting the Total Number of Wins using Average Relative Skill
# 
# The coach of your team suggests a simple linear regression model with the total number of wins as the response variable and the average relative skill as the predictor variable. He expects a team to have more wins in a season if it maintains a high average relative skill during that season. This regression model will help your coach predict how many games your team might win in a regular season. 
# 
# 1. <font color='red'> Replace <strong>??RESPONSE_VARIABLE??</strong> with the variable name that is being predicted. </font> 
# 
# 2. <font color='red'> Replace <strong>??PREDICTOR_VARIABLE??</strong> with the variable name that is the predictor. </font> 
# 
# For example, if the variable names are **var1** for the response variable and **var2** for the predictor variable, then the expression in the code block below should be:
# model = smf.ols('var1 ~ var2', nba_wins_df).fit()
# 

import statsmodels.formula.api as smf

# Simple Linear Regression
# 
model1 = smf.ols('??RESPONSE_VARIABLE?? ~ ??PREDICTOR_VARIABLE??', nba_wins_df).fit()
print(model1.summary())
#  

# ## Step 4: Scatterplot and Correlation for the Total Number of Wins and Average Points Scored
# Your coach expects teams to win more games in a regular season if they score more points on average during the season. This is because the chances of winning are higher if a team maintains high average points scored. Therefore, it is expected that the total number of wins and the average points scored are correlated. Calculate the Pearson correlation coefficient and its P-value. 
# 1. <font color='red'> Replace <strong>??DATAFRAME_NAME??</strong> with the name of the dataframe used in this project. </font> See Step 1 for the name of dataframe used in this project. 
# 
# 2. <font color='red'> Replace <strong>??POINTS??</strong> with the name of the variable for average points scored in a regular season.</font> 
# 
# 3. <font color='red'> Replace <strong>??WINS??</strong> with the name of the variable for the total number of wins in a regular season. 
# 

import scipy.stats as st

plt.plot(??DATAFRAME_NAME??[??POINTS??], ??DATAFRAME_NAME??[??WINS??], 'o')

plt.title('Total Number of Wins by Average Points Scored', fontsize=20)
plt.xlabel('Average Points Scored')
plt.ylabel('Total Number of Wins')
plt.show()

correlation_coefficient, p_value = st.pearsonr(??DATAFRAME_NAME??[??POINTS??], ??DATAFRAME_NAME??[??WINS??])

print("Correlation between Average Points Scored and the Total Number of Wins ")
print("Pearson Correlation Coefficient =",  round(correlation_coefficient,4))
print("P-value =", round(p_value,4))

#  

# ## Step 5: Multiple Regression: Predicting the Total Number of Wins using Average Points Scored and Average Relative Skill
# 
# Instead of presenting a simple linear regression model to the coach, you can suggest a multiple regression model with the total number of wins as the response variable and the average points scored and the average relative skill as predictor variables. This regression model will help your coach predict how many games your team might win in a regular season based on metrics like the average points scored and average relative skill. This model is more practical because you expect more than one performance metric to determine the total number of wins in a regular season. Create this multiple regression model. 
# 1. <font color='red'> Replace <strong>??RESPONSE_VARIABLE??</strong> with the variable name that is being predicted. </font> 
# 
# 2. <font color='red'> Replace <strong>??PREDICTOR_VARIABLE_1??</strong> with the variable name for average points scored. </font> 
# 
# 
# 2. <font color='red'> Replace <strong>??PREDICTOR_VARIABLE_2??</strong> with the variable name for average relative skill. </font> 
# 
# model = smf.ols('var0 ~ var1 + var2', nba_wins_df).fit()
# 

import statsmodels.formula.api as smf

# Multiple Regression

model2 = smf.ols('??RESPONSE_VARIABLE?? ~ ??PREDICTOR_VARIABLE_1?? + ??PREDICTOR_VARIABLE_2??', nba_wins_df).fit()
print(model2.summary())

#  
# ## Step 6: Multiple Regression: Predicting the Total Number of Wins using Average Points Scored, Average Relative Skill, Average Points Differential and Average Relative Skill Differential
# 
# The coach also wants you to consider the average points differential and average relative skill differential as predictor variables in the multiple regression model. Create a multiple regression model with the total number of wins as the response variable, and average points scored, average relative skill, average points differential and average relative skill differential as predictor variables. This regression model will help your coach predict how many games your team might win in a regular season based on metrics like the average score, average relative skill, average points differential and average relative skill differential between the team and their opponents. 
# 
# 1. <font color='red'> The dataframe used in this project is called nba_wins_df. </font>
# 2. <font color='red'> The variable **avg_pts** represents average points scored by each team in a regular season. </font>
# 3. <font color='red'> The variable **avg_elo_n** represents average relative skill of each team in a regular season. </font>
# 4. <font color='red'> The variable **avg_pts_differential** represents average points differential between each team and their opponents in a regular season. </font>
# 5. <font color='red'> The variable **avg_elo_differential** represents average relative skill differential between each team and their opponents in a regular season. </font>
# 6. <font color='red'> Print the model summary. </font>
# 
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML
import statsmodels.formula.api as smf

# dataframe for this project
nba_wins_df = pd.read_csv('nba_wins_data.csv')

model_3 = smf.ols('total_wins ~ avg_pts + avg_elo_n + avg_pts_differential + avg_elo_differential', nba_wins_df).fit()
print(model_3.summary())
