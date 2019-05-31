# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2018/06/29/1508/rata-rata-lama-sekolah-penduduk-umur-15-tahun-menurut-provinsi-2015---2016.html'
ylabel = 'Rata-Rata Lama Sekolah'
func.get_data_bar(url, ylabel, 100, 50)
func.get_regression_pemilu(url, ylabel)
