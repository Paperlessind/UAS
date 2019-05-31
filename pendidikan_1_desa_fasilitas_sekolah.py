# import libraries
import my_function as func

# specify the url
url = 'https://www.bps.go.id/dynamictable/2015/09/17/905/jumlah-desa-yang-memiliki-fasilitas-sekolah-menurut-provinsi-dan-tingkat-pendidikan-2003-2018.html'
ylabel = 'Desa Fasilitas Sekolah'
func.get_data_bar(url, ylabel, 0, 50)
func.get_regression_pemilu(url, ylabel)