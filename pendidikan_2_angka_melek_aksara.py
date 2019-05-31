# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2018/07/24/1544/angka-melek-aksara-penduduk-umur-15-59-tahun-menurut-provinsi-2015-2016.html'
ylabel = 'Angka Melek Aksara'
func.get_data_bar(url, ylabel, 1000, 500)
func.get_regression_pemilu(url, ylabel)