# Topic: Introduction to Statistics in Python
# Source: DataCamp - Introduction to Statistics
# Date: May 2026
# Note: Datasets are from DataCamp environment


# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30
# Import uniform from scipy.stats
from scipy.stats import uniform 

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5,0,30)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1-uniform.cdf(5,0,30)
print(prob_greater_than_5)
# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20,0,30)-\
uniform.cdf(10,0,30)
print(prob_between_10_and_20)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()

#BINOMIAL DISTRIBUTION
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 1 week of 3 deals
print(binom.rvs(3,0.3,size=1))
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3,0.3,size=52)
#n,p,size

# Print mean deals won per week
print(deals.mean())

# What's the probability that Amir closes all 3 deals in a week? 
# Save this as prob_3.

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3,3,0.3) 
#binom.pmf(k,n,p)
# k=how many success we want(3)
# n=total trial numbers(3 deals)
# p=success possibility for every trial(0.3)
print(prob_3)


#What's the probability that Amir closes 1 or fewer deals in a week?
#Save this as prob_less_than_or_equal_1.

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1,3,0.3) 

print(prob_less_than_or_equal_1)


# What's the probability that Amir closes more than 1 deal? 
# Save this as prob_greater_than_1.
# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1-binom.cdf(1,3,0.3)

print(prob_greater_than_1)

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3*0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3*0.35
print(won_35pct)

#NORMAL DISTRIBUTION
# Probability of deal < 7500
# What's the probability of Amir closing a deal worth less than $7500?
prob_less_7500 = norm.cdf(7500,5000,2000)

print(prob_less_7500)

#What's the probability of Amir closing a deal worth more than $1000?
# Probability of deal > 1000
prob_over_1000 = 1-norm.cdf(1000,5000,2000)

print(prob_over_1000)

#What's the probability of Amir closing a deal worth between $3000 and $7000?
# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000,5000,2000)-norm.cdf(3000,5000,2000)

print(prob_3000_to_7000)

#What amount will 25% of Amir's sales be less than?
# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25,5000,2000)

print(pct_25)

# Calculate new average amount
new_mean = 5000+5000*0.20

# Calculate new standard deviation
new_sd = 2000+2000*0.30

# Simulate 36 new sales
new_sales = norm.rvs(new_mean,new_sd,size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()

#CLT- central limit theorem
# Set seed to 104
np.random.seed(104)

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()

# Set seed to 321
np.random.seed(321)
sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals["num_users"].sample(20,replace=True)
  # Take mean of cur_sample
  cur_mean = cur_sample.mean()
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(amir_deals["num_users"].mean())

#POISSON DISTRIBUTION
# Import poisson from scipy.stats and 
# calculate the probability that Amir responds to 5 leads in a day,
# given that he responds to an average of 4.
## Import poisson from scipy.stats
from scipy.stats  import poisson 

# Probability of 5 responses
prob_5 = poisson.pmf(5,4)

print(prob_5)

#Amir's coworker responds to an average of 5.5 leads per day. 
# What is the probability that she answers 5 leads in a day?
# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_coworker = poisson.pmf(5,5.5)

print(prob_coworker)

#EXPONENTIAL 

# Import expon from scipy.stats.
# What's the probability it takes Amir less
#  than an hour to respond to a lead?
# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

#What's the probability it takes Amir 
# more than 4 hours to respond to a lead?
# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes 3-4 hours
print((expon.cdf(4,scale=2.5)) - (expon.cdf(3,scale=2.5)))

import seaborn as sns

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

print(cor)
# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap']=np.log(world_happiness['gdp_per_cap'])
# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap',y='happiness_score',data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)