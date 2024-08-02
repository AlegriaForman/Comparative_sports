# coding: utf-8

# # Hypothesis Testing
#
# You are a data analyst for a basketball team and have access to a large set of historical data that you can use to
# analyze performance patterns. The coach of the team and your management have requested that you perform
# several hypothesis tests to statistically validate claims about your team's performance. This analysis will provide
# evidence for these claims and help make key decisions to improve the performance of the team. You will use the
# Python programming language to perform the statistical analyses and then prepare a report of your findings for the
# team’s management. Since the managers are not data analysts, you will need to interpret your findings and
# describe their practical implications.
#
# The ELO rating, represented by the variable **elo_n**, is used as a measure of the relative skill of a team. This
# measure is inferred based on the final score of a game, the game location, and the outcome of the game relative to
# the probability of that outcome. The higher the number, the higher the relative skill of a team.
#
#
# In addition to studying data on your own team, your management has also assigned you a second team so that
# you can compare its performance with your own team's.
#
# ## Step 1: Data Preparation & the Assigned Team
# This step uploads the data set from a CSV file. It also selects the Assigned Team for this analysis.
#
# 1. The **Assigned Team** is <font color='blue'><strong>Chicago Bulls</strong></font> from the years <font
# color='blue'><strong>1996 - 1998</strong></font>
#
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

nba_orig_df = pd.read_csv('nbaallelo.csv')
nba_orig_df = nba_orig_df[(nba_orig_df['lg_id']=='NBA') & (nba_orig_df['is_playoffs']==0)]
columns_to_keep = ['game_id','year_id','fran_id','pts','opp_pts','elo_n','opp_elo_n', 'game_location', 'game_result']
nba_orig_df = nba_orig_df[columns_to_keep]

# The dataframe for the assigned team is called assigned_team_df.
# The assigned team is the Bulls from 1996-1998.
assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

display(HTML(assigned_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(assigned_team_df))

# ## Step 2: Pick Your Team
# In this step, you will pick your team. The range of years that you will study for your team is <font
# color='blue'><strong>2013-2015</strong></font>.
#
# 1. <font color='red'> Replace <strong>??TEAM??</strong> with your choice of team from one of the following
# team names. </font>
# <font color='blue'>*Bucks, Bulls, Cavaliers, Celtics, Clippers, Grizzlies, Hawks, Heat, Jazz, Kings, Knicks, Lakers,
# Magic, Mavericks, Nets, Nuggets, Pacers, Pelicans, Pistons, Raptors, Rockets, Sixers, Spurs, Suns, Thunder,
# Timberwolves, Trailblazers, Warriors, Wizards*</font>
#
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML
# Range of years: 2013-2015 (Note: The line below selects all teams within the three-year period 2013-2015. This is
# not your team's dataframe.
your_years_leagues_df = nba_orig_df[(nba_orig_df['year_id'].between(2013, 2015))]

# The dataframe for your team is called your_team_df.
#
your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']=="Heat")]
your_team_df = your_team_df.reset_index(drop=True)

display(HTML(your_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(your_team_df))

# ## Step 3: Hypothesis Test for the Population Mean (I)
# A relative skill level of 1340 represents a critically low skill level in the league. The management of your team has
# hypothesized that the average relative skill level of your team in the years 2013-2015 is greater than 1340. Test this
# claim using a 5% level of significance. For this test, assume that the population standard deviation for relative skill
# level is unknown.
#
# 1. <font color='red'> Replace <strong>??DATAFRAME_YOUR_TEAM??</strong> with the name of your team's
# dataframe. </font>
#
# 2. <font color='red'> Replace <strong>??RELATIVE_SKILL??</strong> with the name of the variable for relative
# skill.</font>
#
# 3. <font color='red'> Replace <strong>??NULL_HYPOTHESIS_VALUE??</strong> with the mean value of the
# relative skill under the null hypothesis. </font>
#
import scipy.stats as st

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015 =", round(mean_elo_your_team,2))

# Hypothesis Test
#
test_statistic, p_value = st.ttest_1samp(your_team_df['elo_n'], mean_elo_your_team)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2))
print("P-value =", round(p_value,4))

# ## Step 4: Hypothesis Test for the Population Mean (II)
#
# A team averaging 106 points is likely to do very well during the regular season. The coach of your team has
# hypothesized that your team scored at an average of less than 106 points in the years 2013-2015. Test this claim at
# a 1% level of significance. For this test, assume that the population standard deviation for relative skill level is
# unknown.
#
# 1. <font color='red'> The dataframe for your team is called your_team_df. </font>
# 2. <font color='red'> The variable 'pts' represents the points scored by your team. </font>
# 3. <font color='red'> Calculate and print the mean points scored by your team during the years you picked.
# </font>
# 4. <font color='red'> Identify the mean score under the null hypothesis. You only have to identify this value and
# do not have to print it. </font>
# 5. <font color='red'> Assuming that the population standard deviation is unknown, use Python methods to carry
# out the hypothesis test. </font>
# 6. <font color='red'> Calculate and print the test statistic rounded to two decimal places. </font>
# 7. <font color='red'> Calculate and print the P-value rounded to four decimal places. </font>
#

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

nba_orig_df = pd.read_csv('nbaallelo.csv')
nba_orig_df = nba_orig_df[(nba_orig_df['lg_id']=='NBA') & (nba_orig_df['is_playoffs']==0)]
columns_to_keep = ['game_id','year_id','fran_id','pts','opp_pts','elo_n','opp_elo_n', 'game_location', 'game_result']
nba_orig_df = nba_orig_df[columns_to_keep]

#1.The dataframe for your team is called your_team_df.
your_years_leagues_df = nba_orig_df[(nba_orig_df['year_id'].between(2013, 2015))]
your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']=='Heat')]
your_team_df = your_team_df.reset_index(drop=True)

#2.The variable 'pts' represents the points scored by your team.
#3.Calculate and print the mean points scored by your team during the years you picked.
# mean_pts_your_team = your_team_df['pts'].mean()

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015 =", round(mean_elo_your_team,2))

# Hypothesis Test
#
test_statistic, p_value = st.ttest_1samp(your_team_df['elo_n'], mean_elo_your_team)

print("Hypothesis Test for the Population Mean")
#6.Calculate and print the test statistic rounded to two decimal places.
print("Test Statistic =", round(test_statistic,2))
#7.Calculate and print the P-value rounded to four decimal places.
print("P-value =", round(p_value,4))

# ## Step 5: Hypothesis Test for the Population Proportion
# Suppose the management claims that the proportion of games that your team wins when scoring 102 or more
# points is 0.90. Test this claim using a 5% level of significance.
#
# 1. <font color='red'> Replace <strong>??COUNT_VAR??</strong> with the variable name that represents the
# number of games won when your team scores over 102 points. </font>
#
# 2. <font color='red'> Replace <strong>??NOBS_VAR??</strong> with the variable name that represents the total
# number of games when your team scores over 102 points. </font>
#
# 3. <font color='red'> Replace <strong>??NULL_HYPOTHESIS_VALUE??</strong> with the proportion under the
# null hypothesis. </font>
#

from statsmodels.stats.proportion import proportions_ztest

your_team_gt_102_df = your_team_df[(your_team_df['pts'] > 102)]

# Number of games won when your team scores over 102 points
counts = (your_team_gt_102_df['game_result'] == 'W').sum()

# Total number of games when your team scores over 102 points
nobs = len(your_team_gt_102_df['game_result'])

p = counts*1.0/nobs
print("Proportion of games won by your team when scoring more than 102 points in the years 2013 to 2015 =",
round(p,4))

# Hypothesis Test
#
test_statistic, p_value = proportions_ztest(counts, nobs, 102, prop_var=102)

print("Hypothesis Test for the Population Proportion")
print("Test Statistic =", round(test_statistic,2))
print("P-value =", round(p_value,4))

# ## Step 6: Hypothesis Test for the Difference Between Two Population Means
# The management of your team wants to compare the team with the assigned team (the Bulls in 1996-1998). They
claim that the skill level of your team in 2013-2015 is the same as the skill level of the Bulls in 1996 to 1998. In
other words, the mean relative skill level of your team in 2013 to 2015 is the same as the mean relative skill level of
the Bulls in 1996-1998. Test this claim using a 1% level of significance. Assume that the population standard
deviation is unknown.
#
# 1. <font color='red'> Replace <strong>??DATAFRAME_ASSIGNED_TEAM??</strong> with the name of assigned
# team's dataframe. </font> See Step 1 for the name of assigned team's dataframe.
#
#
# 2. <font color='red'> Replace <strong>??DATAFRAME_YOUR_TEAM??</strong> with the name of your team's
# dataframe. </font> See Step 2 for the name of your team's dataframe.
#
#
# 3. <font color='red'> Replace <strong>??RELATIVE_SKILL??</strong> with the name of the variable for relative
# skill.</font>
#
import scipy.stats as st

assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

mean_elo_n_project_team = assigned_team_df['elo_n'].mean()
print("Mean Relative Skill of the assigned team in the years 1996 to 1998 =", round(mean_elo_n_project_team,2))

mean_elo_n_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015 =", round(mean_elo_n_your_team,2))

# Hypothesis Test
#
test_statistic, p_value = st.ttest_ind(assigned_team_df['elo_n'], your_team_df['elo_n'])

print("Hypothesis Test for the Difference Between Two Population Means")
print("Test Statistic =", round(test_statistic,2))
print("P-value =", round(p_value,4))
