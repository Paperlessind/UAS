# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2017/05/04/1243/indeks-kebahagiaan-menurut-provinsi-2014-2017.html'
ylabel = 'Indeks Kebahagiaan'
func.get_data_bar(url, ylabel, 1000, 200)
func.get_regression_pemilu(url, ylabel)