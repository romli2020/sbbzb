import os
try:
	import requests
except:
	os.system('pip install requests')
	import requests

rs = requests.Session()

def menu():
	os.system('clear')
	print('')
	print('    [ DATA KASUS CORONA DI INDONESIA ]')
	print('')
	print('    [•] Author  : Pandas ID')
	print('    [•] Contact : WA : 082250223147')
	print('                  FB : Pandas ID')
	print('    [•] Versi   : 2.0')
	print('')
	print("    [*] Data diambil dari 'https://kawalcorona.com'")
	print('')
	print('    ==================================')
	print('    [1] Indonesia')
	print('    [2] Provinsi Di Indonesia')
	print('    [3] Dunia')
	print('    [0] Exit')
	pil()

def pil():
	print('')
	pilih = input('    [•] Chose: ')
	if pilih == '1':
		indonesia()
	elif pilih == '2':
		prov()
	elif pilih == '3':
		dunia()
	elif pilih == '0':
		print('')
		print('    [•] Silahkan Tunggu Update Selanjutnya :)')
		exit()
	else:
		print('')
		print('    [!] Silahkan masukan angka pilihan')
		
def indonesia():
	indonesia = rs.get('https://api.kawalcorona.com/indonesia')
	data = indonesia.json()
	negara = data[0]['name']
	positif = data[0]['positif']
	sembuh = data[0]['sembuh']
	mati = data[0]['meninggal']
	print('')
	print('    [ DATA KASUS CORONA DI INDONESIA ]')
	print('    ==================================')
	print('')
	print('    [•] Negara :',negara)
	print('    [•] Positif Corona : ' + str(positif) + ' orang')
	print('    [•] Sembuh : ' + str(sembuh) + ' orang')
	print('    [•] Meninggal : ' + str(mati) + ' orang')
	print('')
	input('    [ Kembali ]')
	menu()
	
def prov():
	url_prov = rs.get('https://api.kawalcorona.com/indonesia/provinsi')
	data_prov = url_prov.json()
	print('')
	print('    [ DATA KASUS CORONA DI SETIAP PROVINSI DI INDONESIA ]')
	print('    =====================================================')
	print('')
	for x in data_prov:
		nama_prov = (x['attributes']['Provinsi'])
		positif = (x['attributes']['Kasus_Posi'])
		sembuh = (x['attributes']['Kasus_Semb'])
		mati = (x['attributes']['Kasus_Meni']) 
		print('    [•] Provinsi :',nama_prov)
		print('    [•] Positif Corona : ' + str(positif) + ' orang')
		print('    [•] Sembuh : ' + str(sembuh) + ' orang')
		print('    [•] Meninggal : ' + str(mati) + ' orang')
		print('')
	print('    [•] Total Provinsi :',len(data_prov))
	print('')
	input('    [ Kembali ]')
	menu()

def dunia():
	positif = rs.get('https://api.kawalcorona.com/positif').json()
	sembuh = rs.get('https://api.kawalcorona.com/sembuh').json()
	mati = rs.get('https://api.kawalcorona.com/meninggal').json()
	ttl_positif = positif['value']
	ttl_sembuh = sembuh['value']
	ttl_mati = mati['value']
	print('')
	print('    [ DATA KASUS CORONA DI SELURUH DUNIA ]')
	print('    ======================================')
	print('')
	print('    [•] Total Positif : ' + str(ttl_positif) + ' orang')
	print('    [•] Total Sembuh : ' + str(ttl_sembuh) + ' orang')
	print('    [•] Total Meninggal : ' + str(ttl_mati) + ' orang')
	print('')
	input('    [ Kembali ]')
	menu()
		
menu()
