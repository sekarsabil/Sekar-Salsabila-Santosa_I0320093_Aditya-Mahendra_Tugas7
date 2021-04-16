print("===== Laman Penggantian Username =====")
nama = input("Masukan Nama Panggilan Anda : ")
namaa = nama.upper()
uname = input("Masukan Username Anda : ")
unamee = "@"+uname
app = "pintarest"
appp = app.capitalize()
print("HAI,", namaa, "!!",
      "\nSelamat Bergabung Lagi Bersama Kami di", appp,
      "\nApakah Anda Yakin akan Mengganti Username Anda" ,unamee, "? (Y/T)")
keputusan = input(">>")
if keputusan == 'Y' :
    new = input("Masukan Username Baru :")
    print("Selamat Menjelajah dengan Username Baru Anda,",unamee.replace(uname, new), "!!")
else:
    print("Anda Membatalkan Proses Penggantian Username"
          "\n===== Sampai Jumpa !! =====")
