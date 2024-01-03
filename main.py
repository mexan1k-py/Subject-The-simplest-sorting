# Homework Простейшие сортировки №3
import random


n = 5
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print('Not sorted:')
print(*arr)
print('-----------')
##############################################################
right_index = n - 1

for j in range(right_index):
    is_sorted = True
    for i in range(right_index - j): # не доходим до конца списка на i,
        if arr[i] > arr[i + 1]:      # потому что в конце уже находятся наибольшии элемент списка
            is_sorted = False        # оказавшись там при придыдущем проходе по списку
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(*arr)
    if is_sorted is True: # помагает понять что список уже отсортирован
        break             # и прекращает процесс сортировки
##############################################################
print('-----------')
print('Sorted:')
print(*arr)