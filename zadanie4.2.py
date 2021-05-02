def is_palindrome(word):
    """
    funkcja posiada zmienną "word"
    pierwsza funckaj "print" wypisuje podane przeze mnie słowo
    druga funkcja "print" wypisuje owrócone słowo
    przy komendzie :return został podany warunek sprawdzenia czy podane przeze mnie słowo jest równe odwróconemu
    wypisujemy wywołaną funkcję
    jeśli słowa są takie same otrzymujemy True, inczej False
    """
    print(f"My word: {word}")
    print(f"Reverced word: {word[::-1]}")
    return word == word[::-1]

print(is_palindrome("kajak"))