totalbelanja = int(input("Masukkan Total Belanja : "))
member = input("Apakah Member (y/t): ")
if (member == "y"):
    if(totalbelanja>=1000000):
        print("Selamat anda mendapatkan diskon 8%")
    elif(totalbelanja<=1000000 and totalbelanja>=500000):
        print("Selamat anda mendapatkan diskon 7%")
    else:
        print("Selamat karena anda member, anda mendapatkan diskon 5%")
else :
    if(totalbelanja>=1000000):
        print("Selamat anda mendapatkan diskon 3%")
    elif(totalbelanja<=1000000 and totalbelanja>=500000):
        print("Selamat anda mendapatkan diskon 2%")
    else:
        print("Anda Tidak mendapatkan diskon")
