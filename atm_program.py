import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input('Masukan Pin lu brow: '))
    trial = 0
    
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('pin lu salah brow, masukin ulang: '))
        trial += 1

        if trial == 3:
            print('pin salah, selamat atm anda tertelan')
            exit()

    while True:
        print('selamat datang di ATM Neraka')
        print('\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar')
        selectmenu = int(input('\nSilakan pilih menu: '))

        if selectmenu == 1:
            print('\nSaldo anda sekarang: Rp. ' + str(atm.checkBalance()) + '\n')

        elif selectmenu == 2:
            nominal = float(input('Masukan nominal saldo : '))
            verify_withdraw = input('Konfirmasi: Anda akan melakukan debet dengan nominal' + str(nominal) + '? y/n')

            if verify_withdraw == "y":
                print('Saldo awal anda adalah: Rp. ' + str(atm.checkBalance()) + ' ')
                
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print('transaksi debet berhasil!')
                print('Saldo sisa sekarang: Rp. ' + str(atm.checkBalance()) + ' ')
            else: 
                print('Maaf, saldonya tidak cukup untuk debet')
                print('Silahkan lakukan penambahan nominal saldo')

        elif selectmenu == 3:
            nominal = float(input('masukan nominal saldo: '))
            verify_deposit = input('Konfirmasi: anda akan melakukan penyimpanan dengan nominal berikut ? y/n ' + str(nominal) + '')

            if verify_deposit == 'y':
                atm.depositBalance(nominal)
                print('saldo anda sekarang adalah: Rp.' + str(atm.checkBalance()) + '\n')
            else:
                break

        elif selectmenu == 4:
            verify_pin = int(input('masukan pin anda: '))
            
            
            while verify_pin != int(atm.checkPin()):
                print('pin anda salah, silakan masukan pin:')
                

            updated_pin = int(input('silakan masukan pin baru: '))
            print('pin anda berhasil diganti')

            verify_newpin = int(input('coba masukan pin baru: '))

            if verify_newpin == updated_pin:
                print('pin baru berhasil dibuat')
            else:
                print('maaf, pin anda salah')
        
        elif selectmenu == 5:
            print('resi tercetak otomatis saat anda keluar. \n harap simpan tanda terima ini \n sebagai bukti transaksi anda')
            print('No. Rekord: ', random.randint(100000,1000000))
            print('tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ', atm.checkBalance())
            print('Terima kasih telah menggunakan ATM Neraka')
            exit()

else:
    print('Error. Maaf, salah masukin angka')

            


