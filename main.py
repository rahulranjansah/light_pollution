from datetime import datetime
import pandas as pd

# df = pd.read_csv("data.csv")

# adjusting datetime to datetimedf and reading the csv file
d_parser = lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
df = pd.read_csv("data.csv", parse_dates = ["UT_datetime"], date_parser = d_parser)


# print(df[" Site description"].unique().tolist())

# check head and column names properly
# print(df.head())
# print(df.columns)

# groupby Site Description

df_sitegroup = df.groupby(" Site description")
df_wyoming = df_sitegroup.get_group(" Wyoming  OH")
df_crestone = df_sitegroup.get_group(" Crestone  Colorado")
df_filtered = pd.concat([df_wyoming, df_crestone])

# print(df_filtered)

# data cleaning of cloud conditions

df_filtered[" Conditions"].replace([' ', ' 100% cloud cover', ' 70% cloud cover', ' 50% cloud cover',
 ' 40% cloud cover', ' 20% cloud cover', ' 60% cloud cover',
 ' 80% cloud cover', ' 30% cloud cover', ' 10% cloud cover',
 ' 90% cloud cover', ' partly cloudy 40% cloud cover',
 ' overcast 100% cloud cover', ' partly cloudy 60% cloud cover', ' clear '], 
 ['0%', '100%', '70%', '50%','40%', '20%', '60%','80%', '30%', '10%','90%', '40%', '100%', '60%', "0%"], inplace=True)

# print(df_filtered[' Conditions'].unique())
print(df_filtered["UT_datetime"])

df_filtered.to_csv("filtered_data.csv", index=False)

