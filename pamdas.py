
#Import the Pandas framework, defined as pd
import pandas as pd
 
#Define our color variable as a list
color = ['blue','green','red','yellow']
#Define our fruit variable as a list
fruit = ['blueberry','apple','cherry','banana']

df=pd.DataFrame(columns=['color', 'fruit'])
	
df['color']=color
df['fruit']=fruit

print(df)