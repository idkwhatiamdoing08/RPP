from random import randint


def delete():
    matrix = list(map(int, input().split())) #ввод матрицы с клавиатруы
    if len(matrix) == 1:
        print("Список должен содержать больше 1 элемента")
        quit() #завершение программы при некорректном вводе
    print('A[%d] =' % (len(matrix)), matrix)
    s = sum(matrix) / len(matrix) #поиск среднего значения
    print("Среднее", s)
    for i in matrix:
        if i > s and i % 2 == 0: #проверка на соотвествование условию
            matrix.remove(i) #удаление элемента
    print('A[%d] =' % (len(matrix)), matrix)


def delete2():
    y = randint(3, 8)
    list = [randint(1, 10) for j in range(y)]
    new_list = []
    sume = 0
    count = 0
    print("A[%d]" % y,list)
    for i in range(y):
        sume += list[i]
        count = count + 1
    print("Среднее: ", sume/count)
    for i in range(y):
        if list[i] <= (sume / count) or list[i] % 2 != 0:
            new_list.append(list[i])
    return print("A[%d]" % len(new_list), new_list);


delete()
delete2()

