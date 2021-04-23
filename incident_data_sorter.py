import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression

base_df = pd.read_csv('NYPD_Shooting_Incident_Data__Historic_Cleaned.csv')

# Boro
boro_df = base_df['BORO']
boro_counts = boro_df.value_counts()
boro_counts_df = boro_counts.to_frame()
boro_counts_df.columns = ['Shooting Counts']
boro_counts_bar_plot = boro_counts_df.plot.bar(y = 'Shooting Counts', rot=0)
plt.show()

# Perpetrator age
perp_age_group_df = base_df['PERP_AGE_GROUP']
perp_age_group_counts = perp_age_group_df.value_counts()
perp_age_group_counts_df = perp_age_group_counts.to_frame()
perp_age_group_counts_df.columns = ["Perpetrator Age Groups"]
perp_age_group_bar_plot = perp_age_group_counts_df.plot.bar(y = 'Perpetrator Age Groups', rot=0)
plt.show()

# Perpetrator race
perp_race_df = base_df['PERP_RACE']
perp_race_counts = perp_race_df.value_counts()
perp_race_counts_df = perp_race_counts.to_frame()
perp_race_counts_df.columns = ["Perpetrators Race"]
perp_race_bar_plot = perp_race_counts_df.plot.bar(y = 'Perpetrators Race', rot=15)
plt.show()

# Perpetrator sex
perp_sex_df = base_df['PERP_SEX']
perp_sex_counts = perp_sex_df.value_counts()
perp_sex_counts_df = perp_sex_counts.to_frame()
perp_sex_counts_df.columns = ["Perpetrators Sex"]
perp_sex_bar_plot = perp_sex_counts_df.plot.bar(y = 'Perpetrators Sex', rot=0, title='Crimes by Sex')
plt.show()

# Murders by year
murder_flag_counts_group_by = base_df.groupby(['OCCUR_YEAR', 'STATISTICAL_MURDER_FLAG']).size().unstack(fill_value=0)
murder_flag_counts_group_by.plot.bar()
plt.show()

# Shootings by year
base_df.rename(columns={'OCCUR_YEAR':'Occurrence Year'}, inplace=True)
crimes_counts_group_by = base_df.groupby('Occurrence Year').size()
crimes_counts_group_by.plot.bar(title='Crimes by Year')
plt.show()

# Shootings by year with prediction
crime_counts_by_year_df = pd.DataFrame({'Year':crimes_counts_group_by.index, 'Counts':crimes_counts_group_by.values})
x = np.unique(np.array(crime_counts_by_year_df['Year'])).reshape((-1, 1))
y = np.array(crime_counts_by_year_df['Counts'])
model = LinearRegression().fit(x, y)
year_to_predict = 2020
prediction = model.intercept_ + model.coef_ * year_to_predict
prediction_value = int(math.ceil(prediction[0]))
crime_counts_by_year_df.loc[len(crime_counts_by_year_df.index)] = [prediction_value, year_to_predict]
print(crime_counts_by_year_df)
crime_counts_by_year_df.plot.bar(y = 'Counts', x = 'Year', title='Crimes by Year Prediction')
plt.show()