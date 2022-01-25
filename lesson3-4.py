num_str = input("Введите целое число: \n")
if num_str.isdigit():
    num = int(num_str)
else:
    print("Вы ввели не число")
summa_1, summa_2, summa_3 = 0, 0, 0
index = 1
while index < num+1:
    summa_1 += index**3
    index +=1

for i in range(num+1):
    summa_2 += i**3

summa_3 = sum([j**3 for j in range(num+1)])

print(f"В while получилась сумма {summa_1}")
print(f"В for получилась сумма {summa_2}")
print(f"В списачном выражении получилась сумма {summa_3}")

