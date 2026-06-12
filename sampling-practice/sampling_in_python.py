# Topic: Sampling in Python
# Source: DataCamp - Sampling in Python
# Date: May 2026~June 2026
# Note: Datasets are from DataCamp environment

import numpy as np
import pandas as pd

# # Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(n=1000)

# Print the sample
print(spotify_sample)

# Calculate the mean duration in mins from spotify_population
mean_dur_pop = spotify_population['duration_minutes'].mean()

# Calculate the mean duration in mins from spotify_sample
mean_dur_samp = spotify_sample['duration_minutes'].mean()

# Print the means
print(mean_dur_pop)
print(mean_dur_samp)
# Simple sampling and calculating with NumPy
# Create a pandas Series from the loudness column of spotify_population
loudness_pop = spotify_population['loudness']

# Sample 100 values of loudness_pop
loudness_samp = loudness_pop.sample(n=100)

# Calculate the mean of loudness_pop
mean_loudness_pop = np.mean(loudness_pop)

# Calculate the mean of loudness_samp
mean_loudness_samp = np.mean(loudness_samp)

print(mean_loudness_pop)
print(mean_loudness_samp)
##CONVENIENCE SAMPLING
# Visualize the distribution of acousticness with a histogram
spotify_population['acousticness'].hist(bins=np.arange(0,1.01,0.01)) #arange not arrange
plt.show()
##PSEUDO Random Number generation
#Generate 5000 numbers from a uniform distribution,
# setting the parameters low to -3 and high to 3.
uniforms = np.random.uniform(-3,3,5000)
# Print uniforms
print(uniforms)
# Generate 5000 numbers from a normal distribution, 
# setting the parameters loc to 5 and scale to 2.
normals = np.random.normal(loc=5,scale=2,size=5000)

# Print normals
print(normals)
# Plot a histogram of uniforms with 
# bins of width of 0.25 from -3 to 3 using plt.hist().
uniforms = np.random.uniform(low=-3, high=3, size=5000)
plt.hist(uniforms,bins=np.arange(-3,3.25,0.25))
plt.show()

# Plot a histogram of normals with 
# bins of width of 0.5 from -2 to 13 using plt.hist()
normals = np.random.normal(loc=5, scale=2, size=5000)
plt.hist(normals,bins=np.arange(-2,13.5,0.5))
plt.show()

# to generate five pseudo-random numbers from the normal distribution with a mean of 0 and 
# a standard deviation of 1, and make the process reproducible, you would use:
import numpy as np
np.random.seed(42)  # Sets the seed
random_numbers = np.random.normal(loc=0, scale=1, size=5)

# Simple random sampling(SRS)

# Sample 70 rows using simple random sampling and set the seed
attrition_samp = attrition_pop.sample(n=70,random_state=18900217)
print(attrition_samp)

# Systematic sampling

# Set the sample size to 70
sample_size = 70
# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)
# Calculate the interval
interval = pop_size // sample_size
# Systematically sample 70 rows
attrition_sys_samp = attrition_pop.iloc[::interval]
# Print the sample
print(attrition_sys_samp)

#Is systematic sampling OK?
# Add an index column to attrition_pop
attrition_pop_id = attrition_pop.reset_index()
# Plot YearsAtCompany vs. index for attrition_pop_id
attrition_pop_id.plot(x='index',y='YearsAtCompany',kind='scatter')
plt.show()
# Shuffle the rows of attrition_pop
attrition_shuffled = attrition_pop.sample(frac=1)
# Reset the row indexes and create an index column
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()
# Plot YearsAtCompany vs. index for attrition_shuffled
attrition_shuffled.plot(x='index',y='YearsAtCompany',kind='scatter')
plt.show()

# Proportional stratified sampling
# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education')\
	.sample(frac=0.4, random_state=2022)

# Calculate the Education level proportions from attrition_strat
education_counts_strat = attrition_strat["Education"].value_counts(normalize=True)

# Print education_counts_strat
print(education_counts_strat)

# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education')\
	.sample(n=30, random_state=2022)      

# Get the proportions from attrition_eq
education_counts_eq = attrition_eq['Education'].value_counts(normalize=True)

# Print the results
print(education_counts_eq)

# Weighted sampling
# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

# Plot YearsAtCompany from attrition_weight as a histogram
attrition_weight['YearsAtCompany'].hist(bins=np.arange(0,41,1)) #bins of width 1 from 0 to 40
plt.show()

# cluster sampling

# Create a list of unique JobRole values
job_roles_pop = list(attrition_pop['JobRole'].unique())
# Randomly sample four JobRole values
job_roles_samp = random.sample(job_roles_pop, k=4)
# Filter for rows where JobRole is in job_roles_samp
jobrole_condition = attrition_pop['JobRole'].isin(job_roles_samp)
attrition_filtered = attrition_pop[jobrole_condition]
# Remove categories with no rows
attrition_filtered['JobRole'] = attrition_filtered['JobRole'].cat.remove_unused_categories()
# Randomly sample 10 employees from each sampled job role
attrition_clust =attrition_filtered.groupby("JobRole").sample(n=10,random_state=2022)
# Print the sample
print(attrition_clust)
# ----------------
# Perform simple random sampling to get 0.25 of the population
attrition_srs = attrition_pop.sample(frac=1/4,random_state=2022)

# Perform stratified sampling to get 0.25 of each relationship group
attrition_strat = attrition_pop.groupby('RelationshipSatisfaction').sample(frac=0.25,random_state=2022)

# Create a list of unique RelationshipSatisfaction values
satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())

# Randomly sample 2 unique satisfaction values
satisfaction_samp = random.sample(satisfaction_unique,k=2)

# Filter for satisfaction_samp and clear unused categories from RelationshipSatisfaction
satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()

# Perform cluster sampling on the selected group, getting 0.25 of attrition_pop
attrition_clust = attrition_clust_prep.groupby('RelationshipSatisfaction').sample(n=len(attrition_pop) // 4, random_state=2022)
# ------------------

#SUMMARY STATISTICS
# Mean Attrition by RelationshipSatisfaction group
mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_pop)
# Calculate the same thing for the simple random sample 
mean_attrition_srs = attrition_srs.groupby('RelationshipSatisfaction')['Attrition'].mean()

# Print the result
print(mean_attrition_srs)
# Calculate the same thing for the stratified sample 
mean_attrition_strat = attrition_strat.groupby("RelationshipSatisfaction")['Attrition'].mean()

# Print the result
print(mean_attrition_strat)
# Calculate the same thing for the cluster sample 
mean_attrition_clust = attrition_clust.groupby("RelationshipSatisfaction")['Attrition'].mean()


# Print the result
print(mean_attrition_clust)
                                        #   --------------
#Calculating relative errors
# Generate a simple random sample of 50 rows, with seed 2022
attrition_srs50 = attrition_pop.sample(n=50,random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()

# Calculate the relative error percentage
rel_error_pct50 = 100*abs(mean_attrition_pop-mean_attrition_srs50)/mean_attrition_pop

# Print rel_error_pct50
print(rel_error_pct50)

# Generate a simple random sample of 100 rows, with seed 2022
attrition_srs100 = attrition_pop.sample(n=100,random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs100 = attrition_srs100['Attrition'].mean()

# Calculate the relative error percentage
rel_error_pct100 = 100*abs(mean_attrition_pop-mean_attrition_srs100)/mean_attrition_pop

# Print rel_error_pct100
print(rel_error_pct100)
                    #  ---------------------
#Replicating samples
# Create an empty list
mean_attritions = []
# Loop 500 times to create 500 sample means
for i in range(500):
	mean_attritions.append(
    	attrition_pop.sample(n=60)['Attrition'].mean()
	)
# Create a histogram of the 500 sample means
plt.hist(mean_attritions, bins=16)
plt.show()
						# ------------------------
# Exact sampling distribution
# Expand a grid representing five 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] + 
                     dice['die3'] + dice['die4'] + 
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort=False).plot(kind='bar')
plt.show()
                        # --------------------
# approximate sampling distribution

# Sample one to eight, five times, with replacement
five_rolls = np.random.choice(list(range(1,8)),size=5,replace=True)
# Print the mean of five_rolls
print(five_rolls.mean())
# Replicate the sampling code 1000 times
sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(
  		np.random.choice(list(range(1, 9)), size=5, replace=True).mean()
    )
# Draw a histogram of sample_means_1000 with 20 bins
plt.hist(sample_means_1000,bins=20)
plt.show()


# Population & sampling distribution means
# Calculate the mean of the mean attritions for each sampling distribution
mean_of_means_5 = np.mean(sampling_distribution_5)
mean_of_means_50 = np.mean(sampling_distribution_50)
mean_of_means_500 = np.mean(sampling_distribution_500)

# Print the results
print(mean_of_means_5)
print(mean_of_means_50)
print(mean_of_means_500)
# Population & sampling distribution variation
# Calculate the std. dev. of the mean attritions for each sampling distribution
sd_of_means_5 = np.std(sampling_distribution_5,ddof=1)
sd_of_means_50 = np.std(sampling_distribution_50,ddof=1)
sd_of_means_500 = np.std(sampling_distribution_500,ddof=1)

# Print the results
print(sd_of_means_5)
print(sd_of_means_50)
print(sd_of_means_500)
                                              # *******************
                
#BOOTSTRAPPING
# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(frac=1, replace=True)

# Calculate of the danceability column of spotify_1_resample
mean_danceability_1 = np.mean(spotify_1_resample['danceability'])

# Print the result
print(mean_danceability_1)
# Replicate this 1000 times
mean_danceability_1000 = []
for i in range(1000):
	mean_danceability_1000.append(
        np.mean(spotify_sample.sample(frac=1, replace=True)['danceability'])
	)

# Draw a histogram of the resample means
plt.hist(mean_danceability_1000)
plt.show()
mean_popularity_2000_samp = []

# Sampling distribution vs. bootstrap distribution

# Generate a sampling distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_samp.append(
    	# Sample 500 rows and calculate the mean popularity 
    	np.mean(spotify_population.sample(n=500,replace=False)['popularity'])
    )

# Print the sampling distribution results
print(mean_popularity_2000_samp)
mean_popularity_2000_boot = []

# Generate a bootstrap distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_boot.append(
    	# Resample 500 rows and calculate the mean popularity     
    	np.mean(spotify_population.sample(n=500,replace=True)['popularity'])
    )

# Print the bootstrap distribution results
print(mean_popularity_2000_boot)
# Calculate the population mean popularity
pop_mean = np.mean(spotify_population['popularity'])

# Calculate the original sample mean popularity
samp_mean = np.mean(spotify_sample['popularity'])

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)

# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])
# Calculate the population std dev popularity
pop_sd = spotify_population['popularity'].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample['popularity'].std(ddof=1)

# Calculate the sampling dist'n estimate of std dev popularity
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)
# Calculate the bootstrap dist'n estimate of std dev popularity
boot_distn_sd = np.std(bootstrap_distribution,ddof=1)*np.sqrt(5000)

# Print the standard deviations
print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])
                    # ------------------confidence intervals------------

# Generate a 95% confidence interval using the quantile method
from scipy.stats import norm
lower_quant = np.quantile(bootstrap_distribution,0.025)
upper_quant = np.quantile(bootstrap_distribution,0.975)

# Print quantile method confidence interval
print((lower_quant, upper_quant))

# Find the mean and std dev of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution,ddof=1)

# Find the lower limit of the confidence interval
lower_se = norm.ppf(0.025,loc=point_estimate,scale=standard_error)

# Find the upper limit of the confidence interval
upper_se = norm.ppf(0.975,loc=point_estimate,scale=standard_error)

# Print standard error method confidence interval
print((lower_se, upper_se))