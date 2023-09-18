
#Step01 - Split the file entered in two txt temp files

#Line Separator
delimiter = '"SUMMARY OF DATA SETS BY VOLUME REPORT"'
with open(r'C:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor.txt') as spacemonitor:
    linhas = spacemonitor.readlines()

position_line = -1
for i, linha in enumerate(linhas):
    if delimiter in linha:
        position_line = i
        break

if position_line >= 0:
    linhas = linhas[position_line + 1:]
spacemonitor.close()

with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor2.txt', "w") as spacemonitor:
    spacemonitor.writelines(linhas)

#step2 - Remove all lines after the delimiter string
delimiter21 = ('"SUMMARY OF DATA SETS BY VOLUME REPORT"')
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor.txt', "r+") as spacemonitor:
    for line in iter(spacemonitor.readline, ""):
        if delimiter21 in line:
            spacemonitor.seek(0, 1)
            spacemonitor.truncate()
            break
spacemonitor.close()

#Step 3 - Remove all lines after the delimiter22
delimiter22 = ('TOTAL DASD UTILIZATION BY VOLUME/DEVICE-TYPE REPORT')
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor2.txt', "r+") as spacemonitor:
    for line in iter(spacemonitor.readline, ""):
        if delimiter22 in line:
            spacemonitor.seek(0, 1)
            spacemonitor.truncate()
            break
spacemonitor.close()

#Step 4 - Remove all unecessary lines from spacemonitor1
linha311 = 'IMS HIGH PERFORMANCE POINTER CHECKER FOR z/OS - SPMN'
linha312 = '5655-U09'
linha313 = 'MEMBER NAME : N/A'
linha314 = 'SUMMARY OF DATA SETS BY VOLUME REPORT'
linha315 = 'DBNAME'
linha316 = '--------'
linha317 = 'TYP'
linha318 = 'DATASET'
linha319 = '/'
linha3110 = 'CYL'
linha3111 = 'TRK'

removed_linhas31 = [linha311, linha312, linha313, linha314, linha315, linha316, linha317, linha318, linha319, linha3110, linha3111]
linhas_sem_string31 = []
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor.txt', "r") as spacemonitor:
    for linha in spacemonitor:
        if not any(removed in linha for removed in removed_linhas31) and not linha.strip() == '':
            linhas_sem_string31.append(linha)
spacemonitor.close()
    
    
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor.txt', "w") as spacemonitor:
    spacemonitor.writelines(linhas_sem_string31)
spacemonitor.close()


#Step 5 - Remove all commas "," from Spacemonitor1
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor.txt', "r+") as spacemonitor:
    conteudo = spacemonitor.read()
    conteudosemvirgulas = conteudo.replace(",",'')
    spacemonitor.seek(0)
    spacemonitor.truncate()
    spacemonitor.write(conteudosemvirgulas)


#Step6 - Remove all unecessary lines from Spacemonitor2
linha321 = 'IMS HIGH PERFORMANCE POINTER CHECKER FOR z/OS - SPMN'
linha322 = '5655-U09'
linha323 = 'MEMBER NAME : N/A'
linha324 = 'SUMMARY OF DATA SETS BY VOLUME REPORT'
linha325 = 'TOTAL DASD UTILIZATION BY VOLUME/DEVICE-TYPE REPORT'
linha326 = '--------'
linha327 = 'VOLSER  DBNAME   DDNAME   DSNAME'

removed_linhas32 = [linha321, linha322, linha323, linha324, linha325, linha326, linha327]

linhas_sem_string32 = []
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor2.txt', "r") as spacemonitor:
    for linha in spacemonitor:
        if not any(removed in linha for removed in removed_linhas32) and not linha.strip() == '':
            linhas_sem_string32.append(linha)
spacemonitor.close()
    
    
with open(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor2.txt', "w") as spacemonitor:
    spacemonitor.writelines(linhas_sem_string32)
spacemonitor.close()

#Step7 - Creates a dataframse for Spacemonitor1 and modifies it as necessary
import pandas as pd
spacemonitor1df = pd.read_csv(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor.txt', delim_whitespace = True, on_bad_lines='skip',header=None)
spacemonitor1df = spacemonitor1df.drop(spacemonitor1df.columns[0],axis=1)
spacemonitor1df.columns = ['DATASET SIZE','SZ%']
spacemonitor1df.info()

spacemonitor1df.to_csv(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitortemp1.txt',index=False,sep='|')


#Step8 - Creates a dataframe for spacemonitor2 and modifies it as necessary
spacemonitor2df = pd.read_csv(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitor2.txt', delim_whitespace = True, on_bad_lines='skip',header=None)
spacemonitor2df.columns = ['VOLSER','DBNAME','DDNAME','DSNAME','DBORG','ACCM','UNIT','BLKSZ','TYP','PRI','SEC','EXT','ALLOC','%USE']

celulasvazias = spacemonitor2df[spacemonitor2df.iloc[:, -1].isnull()]

for index in celulasvazias.index:
    spacemonitor2df.iloc[index, 1:] = spacemonitor2df.iloc[index, :-1].values
    spacemonitor2df.iloc[index, 0] = None

spacemonitor2df = spacemonitor2df.sort_values(by=['DDNAME'])

spacemonitor2df = spacemonitor2df.drop_duplicates(subset=['DDNAME'])

spacemonitor2df = spacemonitor2df.drop('VOLSER',axis=1)

spacemonitor2df.to_csv(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitortemp2.txt',index=False,sep='|')

#Step8 - Unify both spacemonitor1 and spacemonitor2
#unir os dataframes anteriores e salvar num txt
spacemonitor1df = spacemonitor1df.reset_index(drop=True)
spacemonitor2df = spacemonitor2df.reset_index(drop=True)

spacemonitorfinal = pd.concat([spacemonitor2df,spacemonitor1df],axis=1)

#Step9 - Saves the final file to a txt document.
spacemonitorfinal.to_csv(r'c:\Users\VitorAugustoSilighin\Documents\Python\spacemonitorfinal.txt',index=False,sep='|')
