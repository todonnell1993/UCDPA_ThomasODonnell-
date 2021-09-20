import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

t250 = pd.read_csv('Top250.csv', index_col=0)
pd.set_option('display.max_columns', None)
print(t250.head())
#to check contents of dataframe
print(t250.info())
#remove contents and headquarters columns are there is too much missing data
t250.drop(['Content', 'Headquarters'], axis=1, inplace=True)

#to check meanvsales and units sold of all Restaurants
print(t250['Sales'].mean())
print(t250['Units'].mean())

#View Top 10 sales in a bar plot
Top10_sales = t250.sort_values(by=['Sales'], ascending=False)
Top10_sales = Top10_sales.head(10)
palette = sns.color_palette('bright')
sns.set_style('darkgrid')
ax = sns.barplot(x='Restaurant', y='Sales', data=Top10_sales, palette='bright').set(title='Restaurant Top 10 Sales')
plt.show()

#View Top 10 units in a bar plot
Top10_units = t250.sort_values(by=['Units'], ascending=False)
Top10_units = Top10_units.head(10)
palette = sns.color_palette('bright')
sns.set_style('darkgrid')
ax = sns.barplot(x='Restaurant', y='Units', data=Top10_units, palette='bright').set(title='Restaurant Top 10 Units')
plt.show()

#comparing top 10 sales and units of companies and mergeing to see which companies are in both categories
data = [['McDonalds', '40412'], ['Starbucks', '21380'], ['Chick-fil-A', '11320'], ['Taco Bell', '11293'], ['Burger King', '10204'], ['Subway', '10200'], ['Wendys', '9762'], ['Dunkin', '9228'], ['Dominos', '7044'], ['Panera Bread', '5890']]
df1 = pd.DataFrame(data, columns= ['Restaurant', 'Sales'])
data2 = [['Subway', '23801'], ['Starbucks', '15049'], ['McDonalds', '13846'], ['Dunkin', '9630'], ['Burger King', '7346'], ['Pizza Hut', '7306'], ['Taco Bell', '6766'], ['Dominos', '6126'], ['wendys', '5852'], ['Dairy Queen', '4391']]
df2 = pd.DataFrame(data2, columns= ['Restaurant', 'Units'])
df3 = df1.merge(df2, on='Restaurant', how='left')
print(df3)

#using iterrows to quickly show top 10 sales & top 10 units sold
for index, row in Top10_sales.iterrows():
    print(row['Restaurant'], row['Sales'])

for index, row in Top10_units.iterrows():
    print(row['Restaurant'], row['Units'])

#Group top 10 sales by Segment Categort
Segment_sales = t250.groupby('Segment_Category').sum()
Segment_sales = Segment_sales.sort_values('Sales', ascending=False)
print(Segment_sales.head(10))

#companies with sales less than 2000
Low_sales = t250.loc[:, 'Sales'] < 2000
print(Low_sales)