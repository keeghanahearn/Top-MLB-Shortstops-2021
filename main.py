import openpyxl
import pandas as pd
import os
import glob

#107 games into the season, 16 post all star break

#Set WD
os.chdir("C:/Users/kahea/Desktop/Python/")

#Merge SS Hitting Data from 7 separate excel sheets
df = pd.read_excel('./All Star SS 2021/Turner All Star.xlsx', index_col='Year')

files = [file for file in os.listdir('./All Star SS 2021')]

all_SS_batting = pd.DataFrame()

for file in files:
        df = pd.read_excel('./All Star SS 2021/'+file)
        all_SS_batting = pd.concat([all_SS_batting,df])

all_SS_batting.to_csv("all_SS_batting.xlsx",index=False)

print(all_SS_batting.columns)

#3 Isolate the most common years in the data set
print(all_SS_batting['Year'][0:3]) #This is a somewhat entering their prime years

#Neat and useful trick to iterate data
for index, row in all_SS_batting.iterrows():
        print(index, row)

#Display some basic data description to get an idea of the numbers
all_SS_batting.mean()

all_SS_batting.min()

all_SS_batting.max()

##Only include the 2021 season row and include every column except column past ops
#Drop columns
all_SS_batting_columns = all_SS_batting.drop(all_SS_batting.columns[20:], axis=1)
#Drop Rows
all_SS_batting_2021 = all_SS_batting_columns.loc[all_SS_batting_columns['Year'].astype(str) == '2021']



#correct this so it translates in order
name = ['Tatis','Bichette','Correa','Swanson','Turner','Bogaerts','Anderson']

#Example of sorting values based on batting average and age

all_SS_batting_2021 = all_SS_batting_2021.sort_values(['Age','BA'], ascending = [1,0])

#Creating a column with combined slash for each player
all_SS_batting_2021['Total Slash'] = all_SS_batting_2021.iloc[:, 17:20].sum(axis = 1)

all_SS_batting_2021['Name'] = ['Anderson','Bichette','Bogaerts','Correa','Swanson','Tatis','Turner']

#adding column in a specific place
all_SS_batting_2021['Name'] = all_SS_batting_2021.insert(3, 'name',['Tatis','Bichette','Correa','Swanson','Turner','Bogaerts','Anderson'], True)

print(all_SS_batting_2021)

#visualizing the data
import matplotlib.pyplot as plt
import numpy as np

bars = plt.bar(Players,Totals,data=all_SS_batting_2021)


Players = all_SS_batting_2021['name']
Totals = all_SS_batting_2021['Total Slash']


plt.xticks(Players)
plt.yticks(np.arange(0,max(Totals), 0.1))
plt.ylabel('Total Slash')
plt.xlabel('Shortstop Names')
plt.title('First 107 Games')



bars[0].set_color('black')
bars[1].set_color('blue')
bars[2].set_color('red')
bars[3].set_color('orange')
bars[4].set_color('navy')
bars[5].set_color('yellow')
bars[6].set_color('grey')


plt.show()