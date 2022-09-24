"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    print("Hi user! Please, write your age:")
    user_age = int(input())
    if user_age <= 7:
        print("You are " + str(user_age) + ", hence you go to kindergarten")
    elif user_age <= 18:
        print("You are " + str(user_age) + ", hence you go to school")
    elif user_age <= 22:
        print("You are " + str(user_age) + ", hence you go to university")
    elif user_age <= 65:
        print("You are " + str(user_age) + ", hence you go to work")
    elif user_age > 65:
        print("You are " + str(user_age) + ", hence you are retired")


if __name__ == "__main__":
    main()
