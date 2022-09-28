# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def grab(text):
  count = 1
  res = ''
  for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
      count += 1
    else:
      res = res + str(count) + text[i]
      count = 1
  if count > 1 or (text[len(text) - 2] != text[-1]):
    res = res + str(count) + text[-1]
  return res


def deGrab(text):
  number = ''
  res = ''
  for i in range(len(text)):
    if not text[i].isalpha():
      number += text[i]
    else:
      res = res + text[i] * int(number)
      number = ''
  return res


userText = input("Введите текст: ")

print(f"Текст после сжатия: {grab(userText)}")

print(f"Текст после разжатия: {deGrab(grab(userText))}")