# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2015/12/22/1052/angka-partisipasi-murni-apm-menurut-provinsi-2011-2017.html'
ylabel = 'Angka Partisipasi Murni'
func.get_data_bar(url, ylabel, 1000, 500)
func.get_regression_pemilu(url, ylabel)