# Nomor 4
print("Program n x n")
print("==============")
x = int(input("Masukan nilai n : "))
baris = x
kolom = x
def bentuk_pola(y, z):
    for a in range(1, y+1):
        for b in range(1, z+1):
            if (a <= 1 or a == x or b <= 1 or b == z):
                print("* ", end="")
            else:
                print("# ", end="")
        print("")
bentuk_pola(baris,kolom)