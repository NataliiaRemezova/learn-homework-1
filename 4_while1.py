"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    print("Hi, user!")
    how_are_you = "How are you?"
    im_fine = "I'm fine"
    user_answer = "No"
    while user_answer != im_fine:
      print(how_are_you)
      user_answer = input()
    print("Great!")


    
if __name__ == "__main__":
    hello_user()
