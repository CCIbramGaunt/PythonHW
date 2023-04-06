def check_seq(): #функция проверки корректности ввода последовательности пользователем
    try:
        seq = [int(x) for x in input('Введите последовательность чисел через пробел ').split()] #преобразуем пользовательский ввод в список чисел
    except ValueError: #если там не последовательность чисел
        print('Кажется, вы ввели не последовательность, состоящую из чисел. Попробуйте еще раз') #принимаем данные заново
        return (check_seq())
    else:
        pass
    return seq

def check_number(): #функция проверки корректности ввода числа пользователем
    try:
        number = int(input('Введите одно число для внесения в последовательность '))
    except ValueError:
        print('Кажется, вы ввели не одно число или не число вовсе, попробуйте снова')
        return (check_number())
    else:
        pass
    return number

def sorting(list): #функция сортировки введенной последовательности
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return(list)

def binary_search_insert(input_list, element, left, right): #функция поиска индекса элемента, согласно условию задачи
        if input_list[left] > input_list[right]:  # если левая граница превысила правую,
            print('Требуется сначала отсортировать список')
            return False  # значит список не отсортирован, искать бессмысленно
        if element < input_list[0]: #если введенное число меньше первого,
            return 'Элемент вставлен на первое место списка:', [element] + input_list # то вставляем его в начало
        elif element > input_list[-1]: #если введенное число больше последнего,
            return 'Элемент вставлен на последнее место списка:', input_list + [element] # то вставляем его в конец
        else:
            middle = (right + left) // 2  # находим середину
            if input_list[middle+1] >= element and input_list[middle] < element: #если попали на искомый элемент списка
                input_list_left = input_list[0:middle+1] # разбиваем список по найденному индексу
                input_list_right = input_list[middle+1:len(input_list)]
                added_list = input_list_left + [user_number] + input_list_right # и собираем заново, вставляя введенное пользователем число
                return f"Искомый индекс - {middle}, \n Элемент вставлен на {middle+2} место в списке, его индекс стал {middle+1} \n Итоговый список: {added_list}"   # возвращаем искомый индекс и новый список
            elif element < input_list[middle]:  # если элемент меньше элемента в середине - рекурсивно ищем в левой половине
                return binary_search_insert(input_list, element, left, middle - 1)
            else:  # иначе в правой
                return binary_search_insert(input_list, element, middle + 1, right)

user_seq = check_seq()
user_number = check_number()
list_sorted = sorting(user_seq)
#print('Отсортированная последовательность выглядит так:', list_sorted)
print('\n', binary_search_insert(list_sorted, user_number, 0, len(list_sorted)-1))


