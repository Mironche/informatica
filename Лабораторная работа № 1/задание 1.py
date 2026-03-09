# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers[4]=0
#пропуск находится на 4ой позиции заменим его на 0
medium = sum(numbers)/len(numbers)
#и посчитаем ср.знач. чисел
wrong_element = numbers[4]
correct_element = wrong_element + medium
numbers[4] = correct_element
# меняем none на ср.знач.
print("Измененный список:", numbers)