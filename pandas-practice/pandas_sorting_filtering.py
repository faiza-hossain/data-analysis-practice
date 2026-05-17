# Topic: Pandas Sorting and Filtering
# Source: DataCamp - Data Manipulation with pandas
# Date: May 2026
# Note: Datasets are from DataCamp environment
import pandas as pd
dogs.sort_values("weight")#from low to big it will sort the rows as per weight column
dogs.sort_values("weight",ascending = False)#from big to low
dogs.sort_values(["weight","height"])#sort first by weight then height
dogs.sort_values(["weight","height"],ascending=[True, False])
dogs["name"]#to select/print one column
dogs[["breed","height"]]#to select/subset multiple multiple
is_black_or_brown=dogs["color"].isin(["black","brown"])
dogs[is_black_or_brown]#prints those who are black or brown only