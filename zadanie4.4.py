import logging
logging.basicConfig(level=logging.DEBUG)

result = None
operation = input("Podaj numer operacji jaką chcesz wykonać\n"
                  "1 - Dodawanie\n"
                  "2 - Odejmowanie\n"
                  "3 - Mnożenie\n"
                  "4 - Dzielenie\n"
                  "Twoja operacja: ")
if operation == '1':
    logging.info("Wybrałeś dodawanie")
    num1 = float(input("pierwszy składnik dodawania: "))
    num2 = float(input("drugi składnik dodawania: "))
    result = num1+num2
elif operation == '2':
    logging.info("Wybrałeś odejmowanie")
    num1 = float(input("Odjemna: "))
    num2 = float(input("Odjemnik: "))
    result =num1-num2
elif operation == '3':
    logging.info("Wybrałeś mnożenie")
    num1 = float(input("Pierwszy czynnik: "))
    num2 = float(input("Drugi czynnik: "))
    result = num1*num2
elif operation == '4':
    logging.info("Wybrałeś dzielenie")
    num1 = float(input("Dzielna: "))
    num2 = float(input("Dzielnik: "))
    if num2>0:
        result =num1/num2
    else:
        logging.info("Pamiętaj cholero nie dziel przez zero")
        exit(1)
else:
    logging.info("Nie podano operacji!")
    exit(1)
print("Wynik Twojej operacji to: %s" % str(result))