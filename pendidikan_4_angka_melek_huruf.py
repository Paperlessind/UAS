# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2018/07/13/1536/persentase-angka-melek-huruf-amh-penduduk-usia-di-atas-15-tahun-menurut-provinsi-2015-2016.html'
ylabel = 'Angka Melek Huruf'
func.get_data_bar(url, ylabel, 1000, 500)
func.get_regression_pemilu(url, ylabel)
