import logging
logging.basicConfig(level=logging.DEBUG)

def dodawanie(a, b):
    result = a + b
    logging.info(f"Wybrałeś dodawanie. Wynik jest równy: {result}")
    return result

def odejmowanie(a, b):
    result = a - b
    logging.info(f"Wybrałeś odejmowanie. Wynik jest równy: {result}")
    return result

def mnozenie(a, b):
    result = a * b
    logging.info(f"Wybrałeś mnożenie. Wynik jest równy: {result}")
    return result

def dzielenie(a, b):
    if b != 0:
        result = a / b
        logging.info(f"Wybrałeś dzielenie. Wynik jest równy: {result}")
    else:
        logging.info("Pamiętaj cholero nie dziel przez zero")
        exit(1)
    return result

operations = {
    "1": dodawanie,
    "2": odejmowanie,
    "3": mnozenie,
    "4": dzielenie
}

def get_data():
    operation = input("Podaj numer operacji jaką chcesz wykonać\n"
                      "1 - Dodawanie\n"
                      "2 - Odejmowanie\n"
                      "3 - Mnożenie\n"
                      "4 - Dzielenie\n"
                      "Twoja operacja: ")

    b = float(input("Podaj liczbe: "))
    a = float(input("Podaj liczbe: "))
    return operation, a, b


def main():
    op, a, b = get_data()
    try:
        result = operations[op](a, b)
    except KeyError:
        logging.info("Nie podano operacji!")


if __name__ == "__main__":
    main()
