import pandas as pd 

df1 = pd.read_csv("C:/Users/govin/Desktop/ver1/P5QuestionnaireChefMenage2_ver1.tab", sep = '\t')
df2 = pd.read_csv("C:/Users/govin/Desktop/ver2/P5QuestionnaireChefMenage2_ver2.tab", sep = '\t')
df3 = pd.read_csv("C:/Users/govin/Desktop/ver3/P5QuestionnaireChefMenage2_ver3.tab", sep = '\t')
df4 = pd.read_csv("C:/Users/govin/Desktop/ver4/P5QuestionnaireChefMenage2_ver4.tab", sep = '\t')



df1_list = list(df1)
df2_list = list(df2)
df3_list = list(df3)
df4_list = list(df4)
# print(len(df1_list))
# print(len(df2_list))
# print(len(df3_list))
# print(len(df4_list))

# compare1 = [element for element in df4_list if element not in df3_list]

# print(compare1)

# print(df2['qm9__1'].unique())
if(df2['qm1_visite'] == 1)
    print(df2['qm9__3'].value_counts())