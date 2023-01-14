#%%

# cols not in db starting 2020 so removed
#cols_not_needed = ["tripduration","gender","birthyear"]
col_to_use =["trip_id", "bikeid", "start_time" , "end_time",
           "from_station_name", "from_station_id",
           "to_station_name","to_station_id", "usertype"]
col_names = ["ride_id" ,"rideable_type" ,"started_at" ,
        "ended_at" ,"start_station_name","start_station_id" ,
        "end_station_name" ,"end_station_id" ,"member_casual"]
col_to_use_2019Q2 = [
        "01 - Rental Details Rental ID"
        ,"01 - Rental Details Bike ID"                    
        ,"01 - Rental Details Local Start Time"            
        ,"01 - Rental Details Local End Time"
        ,"03 - Rental Start Station Name"   
        ,"03 - Rental Start Station ID"                    
        ,"02 - Rental End Station Name"                
        ,"02 - Rental End Station ID"                      
        ,"User Type"                                       
    ]

# %%
import pandas as pd
df1 = pd.read_csv("Divvy_Trips_2020_Q1.csv",usecols=col_names)[col_names]
df2 = pd.read_csv("Divvy_Trips_2019_Q2.csv",usecols=col_to_use_2019Q2)[col_to_use_2019Q2]

df3 = pd.read_csv("Divvy_Trips_2019_Q3.csv",usecols=col_to_use)[col_to_use]

df4 = pd.read_csv("Divvy_Trips_2019_Q4.csv",usecols=col_to_use)[col_to_use]
#%%
# change col name to make it easy to append
df2.columns = col_names
df3.columns = col_names
df4.columns = col_names
#%%
# change some col type
change_col_dtype = ["ride_id", "rideable_type"]
df2[change_col_dtype] = df2[change_col_dtype].astype(object)
df3[change_col_dtype] = df3[change_col_dtype].astype(object)
df4[change_col_dtype] = df4[change_col_dtype].astype(object)
#df1["end_station_id"] = df1["end_station_id"].astype(int)

# %%
# append 4 diff quarter data to one
df = pd.concat([df1, df2, df3, df4])
#%%
# only subscriber to member, customer to casual
df['member_casual'] = df['member_casual'].replace(["Subscriber", "Customer"], ["member", "casual"])

#%%
# convert star and end time to datetime
df['started_at'] = pd.to_datetime(df["started_at"])
df['ended_at'] = pd.to_datetime(df["ended_at"])
# Ride Lenght in minutes end-start
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.components.minutes

#%%
#calculate some more measures
df['date'] = pd.to_datetime(df["started_at" ])
df['Year'] = df['date'].dt.year
df['Month'] =df['date'].dt.month
df['Day'] =df['date'].dt.day
df['Day_Of_week'] = df['date'].dt.day_name()

# %%
# to save the df 
#df.to_csv('all_trip_final.csv')

# %%
res = df.pivot_table(index = 'Day_Of_week', columns='member_casual',values='ride_length')
res
# %%
import matplotlib.pyplot as plt
ax = res.plot(kind='barh')
ax.set_xlabel("AVG Ride Duration (mins)")

#%%
plt.figure()
res.plot.line()
plt.ylabel("Avg ride duration (mins)")
# %%
