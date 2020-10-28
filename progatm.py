import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
	print("+--------------------------------------------------+")
	print("+-------- Selamat Datang di ATM MAJU JAYA ---------+")
	print("+--------------------------------------------------+")
	id = int(input("Masukkan PIN Anda : "))
	trial = 0
	
	while (id != int(atm.checkPin()) and trial < 3):
		id = int(input("PIN Anda Salah. Silahkan Masukkan Lagi : "))
		
		trial += 1
	
		if trial == 3:
			print("Error. Silahkan Ambil Kartu dan Coba Lagi")
			exit()
	
	while True:
		print("")
		print("+--------------------------------------------------+")
		print("+-------- Selamat Datang di ATM MAJU JAYA ---------+")
		#print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
		print("+                  1. Cek Saldo                    +")
		print("+                  2. Tarik Tunai                  +")
		print("+                  3. Setor                        +")
		print("+                  4. Transfer                     +")
		print("+                  5. Ganti PIN                    +")
		print("+                  6. Keluar                       +")
		print("+--------------------------------------------------+")
		selectmenu = int(input("\nSilahkan Pilih Menu : "))
		 
		if selectmenu == 1:
			print("\nSaldo Anda : Rp" + str(atm.checkBalance()) + "\n")
			
			
		elif selectmenu == 2:
			nominal = float(input("Masukkan Nominal Yang Ingin Ditarik : "))
			verify_withdraw = input("Konfirmasi: Anda Akan Melakukan Tarik Tunai Dengan Nominal Rp" + str(nominal) + " (y/n) ? " + " ")

			if verify_withdraw == "y":
				print("Saldo Awal Anda : Rp" + str(atm.checkBalance()) + "")
			else:
				break
			if nominal < atm.checkBalance():
				atm.withdrawBalance(nominal)
				print("Transaksi Tarik Tunai Berhasil")
				print("Sisa Saldo Anda Saat Ini : Rp" + str(atm.checkBalance()) + "")
			else:
				print("Maaf. Saldo Anda Tidak Cukup")
				#print("Silakan Lakukan Penambahan Nominal Saldo")

			   
		elif selectmenu == 3:
			nominal = float(input("Masukkan Nominal Yang Ingin Disetor : "))
			verify_deposit = input("Konfirmasi: Anda Akan Melakukan Setor Dengan Nominal Rp" + str(nominal) + " (y/n) ?" + " ")

			if verify_deposit == "y":
				atm.depositBalance(nominal)
				print("Transaksi Setor Berhasil")
				print("Saldo Anda Saat Ini : Rp" + str(atm.checkBalance()) + "\n" )
			else:
				break
			
		
		elif selectmenu == 4:
			no_rektujuan = str(input("Masukkan Nomor Rekening Tujuan : "))
			nominal = float(input("Masukkan Nominal Yang Ingin Ditransfer : "))
			verify_transfer = input("Konfirmasi: Anda Akan Melakukan Transfer Dengan Nominal Rp" + str(nominal) + " Ke Nomor Rekening " + str(no_rektujuan) + " (y/n) ?" + " ")
		
			if verify_transfer == "y":
				atm.transferBalance(nominal)
				print("Transaksi Transfer Berhasil")
				print("Sisa Saldo Anda Saat Ini : Rp" + str(atm.checkBalance()) + "\n" )
			else:
				break
		
		elif selectmenu == 5:
			verify_pin = int(input("Masukkan PIN Lama Anda : "))

			while verify_pin != int(atm.checkPin()):
				print("PIN Anda Salah. Silahkan Masukkan PIN Yang Benar : ")

			updated_pin = int(input("Masukkan PIN Baru : "))
			verify_newpin = int(input("Konfirmasi PIN Baru : "))
			#print("PIN Anda Berhasil Diganti")
          
			#verify_newpin = int(input("Coba Masukkan PIN Baru : "))

			if verify_newpin == updated_pin:
				print("PIN Anda Berhasil Diganti")
			else:
				print("PIN Anda Salah. Gagal Mengganti PIN")

			   
		elif selectmenu == 6:
			#print("Resi Tercetak Otomatis Saat Anda Keluar. \n Harap Simpan Tanda Terima Ini \n Sebagai Bukti Transaksi Anda")
			print("")
			print("No. Record : ", random.randint(100000, 1000000))
			print("Tanggal : ", datetime.datetime.now())
			print("Saldo Akhir : ", atm.checkBalance())
			print("Terima Kasih Telah Menggunakan ATM MAJU JAYA") 
			#exit()
		
		
		else:
			print("Error. Maaf, Menu Tidak Tersedia")

