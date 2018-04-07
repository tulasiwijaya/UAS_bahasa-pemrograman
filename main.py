import getpass
def login():
    print("=============================================")
    print("\n\t----Menu Utama-----")
    print("\t1. Kalkulator")
    print("\t2. pembayaran_mahasiswa")
    print("\t3. penilaian_mahasiswa")
    
    pilih = input("\n\tSilahkan Pilih : ")
    if pilih =="1" :
       from perhitungan.kalkulator import kalkulator
       tanya()
    elif pilih =="2" :
       from perhitungan.pembayaran_mahasiswa import pembayaran_mahasiswa
       tanya()
    elif pilih =="3":
        from perhitungan.penilaian_mahasiswa import penilaian_mahasiswa
        tanya()
    else:
        exit
        tanya()

def tanya():
    tanya = input("\nKembali Ke menu (y/n) ?")
    if tanya == "y":
        login()
    elif tanya == "n":
        exit
    else:
        print("\n\tSalah Input !!")

username = input("\nUsername : ")
password = getpass.getpass()
print("=====================================================")

if username == "tulasi" and password == "12345" :
    login()

else :
    print("Maaf username atau password kamu salah")
        

