print('====Program Konversi====')

print('\nList menjadi Set')
angka_list = [1, 2, 3, 2, 4, 5, 1, 2]
print(f'Sebelum (List): {angka_list}')

hasil_set = set(angka_list)
print(f'Sesudah (Set): {hasil_set}')
print()

print('Set menjadi List')
data_set = {10, 20, 30, 40}
print(f'Sebelum (Set): {data_set}')

hasil_list = list(data_set)
print(f'Sesudah (List): {hasil_list}')
print()

print('Tuple menjadi Set')
data_tuple = (7, 8, 9, 7, 9, 10)
print(f'Sebelum (Tuple): {data_tuple}')

hasil_tuple_set = set(data_tuple)
print(f'Sesudah (Set): {hasil_tuple_set}')
print()

print('Set menjadi Tuple')
angka_set = {100, 200, 300}
print(f'Sebelum (Set): {angka_set}')

hasil_tuple = tuple(angka_set)
print(f'Sesudah (Tuple): {hasil_tuple}')
print()