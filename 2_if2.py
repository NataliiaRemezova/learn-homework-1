"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  first_input = input()
  second_input = input()
  if type(first_input) != str:
    print("0")
  if type(second_input) != str:
    print("0")
  if first_input == second_input:
    print("1")
  if first_input != second_input and len(first_input) > len(second_input):
    print("2")
  if first_input != second_input and second_input == "learn":
    print("3")
    
if __name__ == "__main__":
    main()
