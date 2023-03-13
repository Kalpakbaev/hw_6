# #  Определить индексы элементов массива (списка), 
#  значения которых принадлежат заданному диапазону 
#  (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
import random
K = int(input("Please, enter your size array: "))
array = [random.randint(-20,20) for i in range(K)]
print(array)
start_number = int(input("Please,enter your start number: "))
end_number = int(input('Please,enter your end number: '))
for i in range (len(array)):
        if start_number <= array[i] <= end_number:
          print(i)
           
        
       
            
        
        
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#  if min_number <= list_1[i] <= max_number:
#   print(i)        
    
    
