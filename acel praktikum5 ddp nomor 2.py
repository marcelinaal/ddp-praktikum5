ket='''selamat datang di aplikasi perhitungan
silahkan pilih menu yang akan anda jalankan 
1. menghitung luas persegi
2. menghitung luas lingkaran 
3. menghitung luas segitiga'''

Pilihan = input(Pesan)

match pilihan:
    case"1":
      print("anda memasukan angka 1 untuk menghitung luas persegi")
      sisi = float(input("masukan sisi:"))
      luasp = sisi*sisi
      print("luas persegi dengan sisi ",sisi, "adalah", luasp)
    case"2":
      print("kamu memasukan angka 2 untuk menghitung luas lingkarang")
      jari = float(input("masukan jari-jari: "))
      luasl =3,14*jari*jari
      print("luas lingkaran yang jari-jarinya ",jari,"adalah",int(luasl))
    case"3":
      print("kamu memasukan angka 3 untuk menghitung luas segitiga")
      alas = int(input("masukan alas: "))
      tinggi = int(input("masukan tinggi: "))
      luass = 0,5*alas*tinggi
      print("luas segitiga yang alasnya",alas, " dan tingginya ",tinggi," adalah", int(luass))
    case _:
      print("anda salah memilih")