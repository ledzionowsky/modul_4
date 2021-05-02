def is_palindrome(word):
    print(f"My word: {word[::]}")
    print(f"Reverced word: {word[::-1]}")
    return word == word[::-1]


print(is_palindrome("kajak"))