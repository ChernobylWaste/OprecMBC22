# defining functions  
def volumeb(panjang,lebar,tinggi):  
    hasil = panjang*lebar*tinggi  
    print("Volume Balok: ", hasil) 
  
def luasb(panjang, lebar, tinggi):  
    hasil = 2 * (panjang * lebar + panjang * tinggi + lebar* tinggi)
    print("Luas Balok: ", hasil)  
  
def volumek(sisi):  
    hasil = sisi * sisi * sisi 
    print("Volume Kubus: ", hasil)  
  
def luask(sisik):  
    hasil = 6 * sisik * sisik  
    print("Luas Kubus: ", hasil)  
  
def volumes(alas, tinggis, tinggip):
    hasil = (0.5 * alas * tinggis) * tinggip 
    print("Volume Segitiga: ", hasil)  
  
def luass(alas, tinggis):
    hasil = 0.5 * alas * tinggis
    print("Luas Segitiga", hasil)  
  
# printing the starting line  
print("Open Recruitment MBC Laboratory")  
print("Kelompok Cyber Security 2")

# creating options  
while True:  
    print("\nMAIN MENU")  
    print("1. Volume Balok")  
    print("2. Luas Balok")
    print("3. Volume Kubus")
    print("4. Luas Kubus")
    print("5. Volume Segitiga")
    print("6. Luas Segitiga")
    print("7. Exit")  
    pilih = int(input("Silahkan isi dengan 1-7: "))  
  
    if pilih == 1:  
        panjang = int(input("Masukan Panjang : "))
        lebar = int (input("Masukan Lebar : "))
        tinggi = int (input("Masukkan Tinggi : "))
        volumeb(panjang,lebar,tinggi)
        break

    elif pilih == 2:  
        panjang = int(input("Masukan Panjang : "))
        lebar = int (input("Masukan Lebar : "))
        tinggi = int (input("Masukkan Tinggi : "))
        luasb(panjang,lebar,tinggi)
        break 
      
    elif pilih == 3:  
        sisi = int(input("Masukkan Sisi: "))
        volumek(sisi)
        break

    elif pilih == 4:  
        sisik = int(input("Masukkan Sisi: "))
        luask(sisik)
        break
    
    elif pilih == 5:  
        alas = int(input("Masukkan Alas: "))
        tinggis = int(input("Masukkan Tinggi: "))
        tinggip = int(input("Masukkan Tinggi Prisma: "))
        volumes(alas, tinggis, tinggip)
        break

    elif pilih == 6:  
        alas = int(input("Masukkan Alas: "))
        tinggis = int(input("Masukkan Tinggi: "))
        luass(alas, tinggis)
        break
    
    elif pilih == 7:
        break
    else:  
        print("Oops! Incorrect Choice.")  