import os
import csv

def dir_files(directory):
    files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    print(directory)
    print(len(files))


def write(filename):
    print("Номер: ")
    number = int(input())
    print("Артикул: ")
    art = str(input())
    print("Наименование: ")
    name = str(input())
    print("Количетсво: ")
    amount = int(input())
    print("Цена: ")
    price = int(input())
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['number', 'art', 'name', 'amount', 'price']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writerow({'number': number, 'art': art, 'name': name, "amount": amount, 'price': price})
    csvfile.close()


def out(filename):
    csvfile = open(filename, 'r', newline='')
    fieldnames = ['number', 'art', 'name', 'amount', 'price']
    reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
    data = [row for row in reader]
    print(data)
    print("Сортировка по наименованию:")
    for i in sorted(data, key=lambda x: str(x['name'])):
        print(i)
    print("Сортировка по количеству:")
    for i in sorted(data, key = lambda x: int(x['amount'])):
        print(i)

    print("Цена больше 50 рублей:")

    for row in data:
        if int(row['price']) >= 50:
           print(row)
    csvfile.close()

if __name__ == '__main__':
    do = int(input("Показать файлы - 1\tВывод csv - 2\tДобавить в csv - 3\n"))
if do == 1:
    dir_files('venv/Scripts')
elif do == 2:
    out('data.csv')
else:
    write('data.csv')