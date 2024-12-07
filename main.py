"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""
def isPalindrom(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
    
user_input = input('Введите слово: ')

print(isPalindrom(user_input))

def isPalindromList(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

def check_palindromes(words):
    palindromes = []
    for word in words:
        if isPalindromList(word):
            palindromes.append(word.lower())
    return palindromes

user_input = input("Введите слова через запятую: ")
words_list = [word.strip() for word in user_input.split(",")]

print(check_palindromes(words_list))

def isPalindromString(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

def find_palindromes(text):
    words = text.split()
    palindromes = set()
    
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if isPalindromString(word) and word:
            palindromes.add(word.lower())

    return list(palindromes)

user_input = input("Введите текст: ")

print(find_palindromes(user_input))
