import pandas as pd
import matplotlib.pyplot as plt

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
perp_sex_bar_plot = perp_sex_counts_df.plot.bar(y = 'Perpetrators Sex', rot=0)
plt.show()

# Murders by year
murder_flag_counts_group_by = base_df.groupby(['OCCUR_YEAR', 'STATISTICAL_MURDER_FLAG']).size().unstack(fill_value=0)
murder_flag_counts_group_by.plot.bar()
plt.show()

