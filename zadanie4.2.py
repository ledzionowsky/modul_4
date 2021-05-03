import string

def is_palindrome(s):
    """
    funkcja posiada zmienną "s"
    metoda "lower" zmienia wszystkie litery na małe
    metoda "replace" usuwa spacje
    pierwsza meotda "print" wypisuje podane przeze mnie słowo
    druga funkcja "print" wypisuje owrócone słowo
    przy komendzie :return został podany warunek sprawdzenia czy podane przeze mnie słowo jest równe odwróconemu
    wypisujemy wywołaną funkcję
    jeśli słowa są takie same otrzymujemy True, inczej False
    """
    znaki = []
    s=s.lower()
    for znak in s:
        if znak.isalnum():
            znaki.append(znak)
    return znaki == znaki[::-1]

print(is_palindrome("Kobyła ma, mały bok"))