import logging
logging.basicConfig(level=logging.DEBUG)

def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnozenie(a,b):
    return a*b
def dzielenie(a,b):
    return a/b
def dane():
    a=input()
    b=input()
    return a,b
operation = input("Podaj numer operacji jaką chcesz wykonać\n"
                  "1 - Dodawanie\n"
                  "2 - Odejmowanie\n"
                  "3 - Mnożenie\n"
                  "4 - Dzielenie\n"
                  "Twoja operacja: ")

#b = float(input("Podaj liczbe: "))
#a = float(input("Podaj liczbe: "))

if operation == '1':

    logging.info("Wybrałeś dodawanie. Wynik jest równy: "+str(dodawanie(a,b)))
elif operation == '2':
    logging.info("Wybrałeś odejmowanie. Wynik jest równy: "+str(odejmowanie(a,b)))
elif operation == '3':
    logging.info("Wybrałeś mnożenie. Wynik jest równy: "+str(mnozenie(a,b)))
elif operation == '4':
    if b!=0:
        logging.info("Wybrałeś dzielenie. Wynik jest równy: "+str(dzielenie(a,b)))
    else:
        logging.info("Pamiętaj cholero nie dziel przez zero")
        exit(1)
else:
    logging.info("Nie podano operacji!")
    exit(1)