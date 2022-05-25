import pandas as pd
import numpy as np


df = pd.read_csv("C:/Users/govin/Downloads/P5_Questionnaire_HxMed_1.tab", sep='\t')

df1 = pd.read_excel("C:/Users/govin/Downloads/iButton_serial_numbers.xlsx", skiprows=1)

# print (df.describe(include=['object']))

# print(df['freq_Cardiaque1'].mean())
# print(df.head())

# control = df1[ (df1['Type d’intervention']!='CONTROLE') & (df1['Type de toit']!='Banco') ]

#Create new dataframe 'studygroup' by selecting rows based on whether they belong to control/intervention and banco/tin
studygroup = df1[ (df1['Type d’intervention']!='CONTROLE') & (df1['Type de toit']!='Banco') ]


# df_latest = df[ (df['qm1_visite']==6) ]

df['dateEntree'] = pd.to_datetime(df['dateEntree']) 


start_day = '2021-08-01'
end_day = '2021-08-31'
start_day = pd.to_datetime(start_day)
end_day = pd.to_datetime(end_day)

month_df = df[df['dateEntree'].between(start_day, end_day)]




list =[]

for index, each in enumerate(month_df['numMenage']):
    for element in studygroup['ID Menage']:
        if str(element) == str(each):
            list.append(df.loc[index,['freq_Cardiaque1']].item())
            
cleanedList = [x for x in list if str(x) != 'nan']  
cleaned2list = [i for i in cleanedList if i >= 26]    
      
print(np.mean(cleaned2list))
print(np.std(cleaned2list))
print(np.max(cleaned2list))
print(np.min(cleaned2list))


