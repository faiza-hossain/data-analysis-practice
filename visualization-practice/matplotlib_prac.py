
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[7,8,9,10]
plt.plot(x,y)
print(plt.show())

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg(['var','std']))

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category']=='beef']['co2_emission'].hist()
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
plt.figure()
food_consumption[food_consumption['food_category']=='eggs']['co2_emission'].hist()
plt.show()

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]))

# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=[2,3,4,5,6])
plt.show()

