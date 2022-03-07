def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word

while True:
    x = input("Insert the word:")
    print(is_palindrome(x))