# TODO Найдите количество книг, которое можно разместить на дискете
number_sumbols_1 = 50*25
# найдем число символов на 1 стр.
number_sumbols_2 = 100 * number_sumbols_1
#найдем кол-во символов на 100стр
weigth_1_book = number_sumbols_2 * 4
#кол-во байт в 1 книге
MB = int(1.44*1024*1024)
books_number = MB // weigth_1_book
print("Количество книг, помещающихся на дискету:", books_number)