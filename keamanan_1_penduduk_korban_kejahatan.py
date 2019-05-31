# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2018/05/30/1407/proporsi-penduduk-yang-menjadi-korban-kejahatan-kekerasan-dalam-12-bulan-terakhir-menurut-provinsi-2015---2016.html'
ylabel = 'Penduduk Korban Kejahatan'
func.get_data_bar(url, ylabel, 0, 1)
func.get_regression_pemilu(url, ylabel)
