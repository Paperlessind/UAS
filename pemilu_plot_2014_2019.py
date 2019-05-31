# import libraries
import numpy as np
import my_function as func
import matplotlib.pyplot as plt
# specify the url
url1 = 'https://kawalpemilu.org/#pilpres:0'
soup1 = func.getData(url1)

results1 = soup1.find('table',{'class':'table'})
rows1 = results1.find_all('tr',{'class':'row'})
list_wilayah1 = []
jokowi1 = []
prabowo1 = []

# print(rows)
for r in rows1:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
# write columns to variables
    wilayah = data[1].find('a').getText()
    if wilayah != 'KALIMANTAN UTARA':
        satu = data[2].find('span', attrs={'class':'abs'}).getText()
        dua = data[3].find('span', attrs={'class': 'abs'}).getText()
        # Remove decimal point
        satu = satu.replace('.','')
        dua = dua.replace('.','')
        # Cast Data Type Integer
        satu = int(satu)
        dua = int(dua)
        list_wilayah1.append(wilayah)
        jokowi1.append(satu)
        prabowo1.append(dua)

# Convert to numpy
np_wilayah1 = np.array(list_wilayah1)
np_jokowi1 = np.array(jokowi1)
np_prabowo1 = np.array(prabowo1)

# specify the url
url2 = 'https://2014.kawalpemilu.org/#0'
soup2 = func.getData(url2)

# find results within table
results2 = soup2.find('table',{'class':'aggregate'})
rows2 = results2.find_all('tr',{'class':'datarow'})
# print(rows)
list_wilayah2 = []
jokowi2 = []
prabowo2 = []
#
# print(rows)
for r in rows2:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
# write columns to variables
    wilayah = data[1].find('a').getText()
    satu = data[2].getText()
    dua = data[10].getText()
    # Remove decimal point
    satu = satu.replace('.','')
    dua = dua.replace('.','')
    # Cast Data Type Integer
    satu = int(satu)
    dua = int(dua)
    list_wilayah2.append(wilayah)
    jokowi2.append(satu)
    prabowo2.append(dua)

# # Convert to numpy
np_wilayah2 = np.array(list_wilayah2)
np_jokowi2 = np.array(jokowi2)
np_prabowo2 = np.array(prabowo2)

# Naming label
plt.xlabel('PROVINSI')
plt.ylabel('PEROLEHAN SUARA')

# styling x,y value
plt.xticks(rotation=30,ha='right')
plt.yticks(np.arange(np_jokowi1.min(),np_jokowi1.max(),1000000))

# plot data
plt.plot(np_wilayah2,np_jokowi2,color='red',label='Jokowi 2014',linestyle='dashed', marker='o', alpha=0.5)
plt.plot(np_wilayah1,np_jokowi1,color='green',label='Jokowi 2019',linestyle='dashed', marker='o', alpha=0.5)
plt.plot(np_wilayah2,np_prabowo2,color='blue',label='Prabowo 2014',linestyle='dashed', marker='o', alpha=0.5)
plt.plot(np_wilayah1,np_prabowo1,color='orange',label='Prabowo 2019',linestyle='dashed', marker='o', alpha=0.5)

plt.legend(loc='upper right')
plt.yscale('linear')
plt.show()
