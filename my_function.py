# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time

def getData(url,second=5):
    # specify the url

    # The path to where you have your chrome webdriver stored:
    webdriver_path = 'D:/Master/chromedriver_win32/chromedriver.exe'

    # Add arguments telling Selenium to not actually open a window
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')

    # Fire up the headless browser
    browser = webdriver.Chrome(executable_path=webdriver_path,
                               options=chrome_options)

    # Load webpage
    browser.get(url)

    # It can be a good idea to wait for a few seconds before trying to parse the page
    # to ensure that the page has loaded completely.
    time.sleep(second)

    # Parse HTML, close browser
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.quit()

    return soup

def get_data_bar(url, ylabel, min_index, max_index):
    # import libraries
    import my_function as func
    # specify the url
    soup = func.getData(url)

    # find results within table
    result_wilayah = soup.find('table', attrs={'id': 'tableLeftBottom'})
    result_value = soup.find('table', attrs={'id': 'tableRightBottom'})

    rows_wilayah = result_wilayah.find_all('tr')
    rows_value = result_value.find_all('tr')

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
        wilayah = data_wilayah[0].getText()
        nilai = data_value[-1].getText()
        # Remove decimal point
        nilai = nilai.replace('.', '')
        # Cast Data Type Integer
        nilai = int(nilai)
        list_wilayah.append(wilayah)
        value.append(nilai)

    # Create Dictionary
    my_dict = {'wilayah': list_wilayah, 'value': value}
    # Create Dataframe
    df = pd.DataFrame(my_dict)

    # Plot dataframe to histogram
    plt.bar(df['wilayah'], df['value'])
    plt.xlabel('Provinsi')
    plt.ylabel(ylabel)
    if min_index == 0 :
        min_index = 0
    else:
        min_index = df['value'].min() - min_index

    plt.gca().set_ylim([min_index, df['value'].max() + max_index])
    plt.xticks(rotation='50', ha='right')
    plt.show()

def get_regression_pemilu(url2, ylabel):
    # import libraries
    import my_function as func

    # specify the url
    url1 = 'https://kawalpemilu.org/#pilpres:0'
    soup1 = func.getData(url1)

    # find results within table
    results1 = soup1.find('table', {'class': 'table'})
    rows1 = results1.find_all('tr', {'class': 'row'})
    # list_wilayah = []
    jokowi = []
    prabowo = []

    # print(rows)
    for r in rows1[:-1]:
        # find all columns per result
        data = r.find_all('td')
        # check that columns have data
        if len(data) == 0:
            continue
        # write columns to variables
        # wilayah = data[1].find('a').getText()
        satu = data[2].find('span', attrs={'class': 'abs'}).getText()
        dua = data[3].find('span', attrs={'class': 'abs'}).getText()
        # Remove decimal point
        satu = satu.replace('.', '')
        dua = dua.replace('.', '')
        # Cast Data Type Integer
        satu = int(satu)
        dua = int(dua)
        # list_wilayah.append(wilayah)
        jokowi.append(satu)
        prabowo.append(dua)

    soup2 = func.getData(url2)

    # find results within table
    result_value = soup2.find('table', attrs={'id': 'tableRightBottom'})
    rows_value = result_value.find_all('tr')
    target_value = []

    # print(rows)
    for id, r in enumerate(rows_value[:-1]):
        # find all columns per result
        data_value = rows_value[id].find_all('td', attrs={'class': 'datas'})

        # check that columns have data
        if len(data_value) == 0:
            continue

        # write columns to variables
        nilai = data_value[-1].getText()
        # Remove decimal point
        nilai = nilai.replace('.', '')
        # Cast Data Type Integer
        nilai = int(nilai)
        target_value.append(nilai)

    my_dict = {'jokowi': jokowi, 'prabowo': prabowo, 'target_value': target_value}
    # Create Dataframe
    df = pd.DataFrame(my_dict)
    jokowi = df['jokowi'].values
    prabowo = df['prabowo'].values
    target_value = df['target_value'].values

    jokowi = jokowi.reshape(-1, 1)
    prabowo = prabowo.reshape(-1, 1)
    target_value = target_value.reshape(-1, 1)

    # Fitting Simple Linear Regression
    reg1 = LinearRegression()
    reg2 = LinearRegression()

    # Create the prediction space
    prediction_space1 = np.linspace(min(jokowi), max(jokowi)).reshape(-1, 1)
    prediction_space2 = np.linspace(min(prabowo), max(prabowo)).reshape(-1, 1)

    # Fit the model to the data
    reg1.fit(jokowi, target_value)
    reg2.fit(prabowo, target_value)

    r_sq1 = reg1.score(jokowi, target_value)
    print('coefficient of determination Jokowi:', r_sq1)
    print('intercept Jokowi:', reg1.intercept_)
    print('slope Jokowi:', reg1.coef_)

    r_sq2 = reg1.score(prabowo, target_value)
    print('coefficient of determination Prabowo:', r_sq2)
    print('intercept Prabowo:', reg2.intercept_)
    print('slope Prabowo:', reg2.coef_)

    # Compute predictions over the prediction space: y_pred
    y_pred1 = reg1.predict(prediction_space1)
    y_pred2 = reg2.predict(prediction_space2)

    plt.scatter(jokowi, target_value, color='green', alpha=0.5, label='Jokowi')
    plt.scatter(prabowo, target_value, color='red', alpha=0.5, label='Prabowo')
    plt.plot(prediction_space1, y_pred1, color='green', linewidth=2, label='Jokowi Regression')
    plt.plot(prediction_space2, y_pred2, color='red', linewidth=2, label='Prabowo Regression')
    plt.title('Hasil Pemilu vs '+ylabel)
    plt.xlabel('Hasil Pemilu')
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.show()
