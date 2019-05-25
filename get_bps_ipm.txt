
# import libraries
import numpy as np
import pandas as pd
import my_function as func
import matplotlib.pyplot as plt
# specify the url
url = 'https://www.bps.go.id/dynamictable/2016/06/16/1211/indeks-pembangunan-manusia-menurut-provinsi-2010-2018-metode-baru-.html'
soup = func.getData(url)

# find results within table
result_wilayah  = soup.find('table', attrs={'id': 'tableLeftBottom'})
result_value    = soup.find('table', attrs={'id': 'tableRightBottom'})

rows_wilayah    = result_wilayah.find_all('tr')
rows_value      = result_value.find_all('tr')

list_wilayah = []
value = []

# print(rows)
for id, r in enumerate(rows_wilayah[:-1]):
    # find all columns per result
    data_wilayah = r.find_all('td', attrs={'id': 'th4'})
    data_value = rows_value[id].find_all('td', attrs={'class': 'datas'})

    # check that columns have data
    if len(data_wilayah) == 0:
        continue

    # write columns to variables
    wilayah = data_wilayah[0].find('b').getText()
    nilai = data_value[-1].getText()
    # Remove decimal point
    nilai = nilai.replace('.','')
    # Cast Data Type Integer
    nilai = int(nilai)
    list_wilayah.append(wilayah)
    value.append(nilai)

# Create Dictionary
my_dict = {'wilayah':list_wilayah,'value':value}
# Create Dataframe
df = pd.DataFrame(my_dict)

# Plot dataframe to histogram
plt.bar(df['wilayah'], df['value'])
plt.xlabel('Provinsi')
plt.ylabel('Indeks Pembangunan Manusia')
plt.gca().set_ylim([df['value'].min(),df['value'].max()])
plt.xticks(rotation='vertical',ha='right')
plt.legend(loc='upper right')
plt.show()
