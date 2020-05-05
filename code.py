# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data=pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)
#Code starts here



# --------------
#Code starts here

#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)

    
#Code ends here    


# --------------
#Code starts here




top_countries=pd.DataFrame(data,columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])



top_countries.drop(top_countries[::-1].index[0],axis=0,inplace=True)



def top_ten(df,v):
    country_list=df.nlargest(10,v)
    return(list(country_list['Country_Name']))
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

a_set = set(top_10_summer) 
b_set = set(top_10_winter) 
c_set= set(top_10)
if (a_set & b_set & c_set): 
    common=list(a_set & b_set &c_set) 


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xlabel("country name")
plt.ylabel("toatl")


# --------------
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio']) 


summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio=max(winter_df['Golden_Ratio'])

winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio=max(top_df['Golden_Ratio'])

top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here


#Removing the last column of the dataframe
data_1=data[:-1]

#Creating a new column 'Total_Points'
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1  # Use of position index to handle the ambiguity of having same name columns


#Finding the maximum value of 'Total_Points' column
most_points=max(data_1['Total_Points'])

#Finding the country assosciated with the max value of 'Total_Column' column
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('The maximum points achieved is ', most_points, ' by ', best_country )

#Code ends here


# --------------
#Code starts here





best=data[data['Country_Name'] == best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]


best.plot.bar()

plt.xlabel('United States')

plt.ylabel('Medals Tally')

plt.xticks(rotation=45)


