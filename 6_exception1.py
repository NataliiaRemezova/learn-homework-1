"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user():
  print("Hi, user!")
  how_are_you = "How are you?"
  im_fine = "I'm fine"
  user_answer = "No"
  while user_answer != im_fine:
    try:
      print(how_are_you)
      user_answer = input()
    except KeyboardInterrupt:
          print("\nBye!")
          break
  if user_answer == im_fine:
    print("Great!")


if __name__ == "__main__":
    hello_user()
