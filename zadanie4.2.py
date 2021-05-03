import string

def is_palindrome(s):
    """
    funkcja posiada zmienną "s"
    metoda "lower" zmienia wszystkie litery na małe
    pętla for selekcjonuje znaki zatrzymując tylko te, które w tym przypadku są tylko literą a następnia wrzuca ją do listy "znaki"
    porownujemy znaki w liscie ze znakami listy odwroconej
    """
    znaki = []
    s=s.lower()
    for znak in s:
        if znak.isalnum():
            znaki.append(znak)
    return znaki == znaki[::-1]

print(is_palindrome("Kobyła ma, mały bok"))