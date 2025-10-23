import os
os.system('clear')

print("nama\t\t:Nama Lengkap")
print("prodi\t\t:Robotika\n")

print("Praktikum 2")

# # x > 2
# # ----------2++++++++++

# x = float(input('Masukkan nilai x > 2: '))

# cek  = x > 2
# print(f'x > 2 adalah {cek}')

# =====================================================


# # 2 < x < 4
# # ----------2++++++++++4----------

# x = float(input('Masukkan nilai 2 < x < 4: ')) # 3

# cek1  = x > 2 # T
# cek2  = x < 4 # T

# cek  = cek1 and cek2

# print(f'2 < x < 4 adalah {cek}') #T

# =====================================================

# # x < 2 atau x > 5
# # ++++++++++2----------5++++++++++

# x = float(input('Masukkan nilai 2 < x < 4: ')) # 1

# cek1  = x < 2 # T
# cek2  = x > 5 # F

# cek  = cek1 or cek2

# print(f'2 < x < 4 adalah {cek}') #T

# =====================================================

# # x < 2 atau 5 < x < 8
# # ++++++++++2----------5++++++++++8----------

# x = float(input('Masukkan nilai x < 2 atau 5 < x < 8: ')) # 1

# cek1  = x < 2               # T
# cek2  = x > 5 and x < 8     # F

# cek  = cek1 or cek2

# print(f'Hasilnya adalah {cek}') #T

# =====================================================

# x < 2 atau 5 < x < 8
# ----------(-3)++++++++++2----------5++++++++++8----------9+++++13------

x = float(input('Masukkan nilai x < 2 atau 5 < x < 8: ')) # 1

cek1  = x > -3 and x < 2           # T
cek2  = (x > 5  and x < 8)    or (x > 9 and x < 13   )   # F

cek  = cek1 or cek2

print(f'Hasilnya adalah {cek}') #T