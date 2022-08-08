def plus():
    try:
        print("Jakie liczby chcesz dodać?")
        while True:
            first = float(input("Pierwsza liczba"))
            second = float(input("Druga liczba"))
            result = first + second
            print(f'Wynik działania {first} + {second}  = {result}')
            choice=input('Jeżeli chcesz wyjść wybierz x w innym przypadku wybierz y').upper()
            if choice=='X':
                print('Do widzenia!')
                break
            elif choice=='Y':
                continue
            else:
                print('podano zły znak. Do widzenia!')
                break
        return
    except: print('Błędnie wprowadzony znak!')




def minus():
    try:
        print("Jakie liczby chcesz odjąć?")
        while True:
            first = float(input("Pierwsza liczba"))
            second = float(input("Druga liczba"))
            result = first - second
            print(f'Wynik działania {first} - {second}  = {result}')
            choice = input('Jeżeli chcesz wyjść wybierz x w innym przypadku wybierz y').upper()
            if choice == 'X':
                print('Do widzenia!')
                break
            elif choice == 'Y':
                continue
            else:
                print('podano zły znak. Do widzenia!')
                break
        return
    except:
        print('Błędnie wprowadzony znak!')

def multi():
    try:
        print("Jakie liczby chcesz mnożyć?")
        while True:
            first = float(input("Pierwsza liczba"))
            second = float(input("Druga liczba"))
            result = first * second
            print(f'Wynik działania {first} * {second}  = {result}')
            choice = input('Jeżeli chcesz wyjść wybierz x w innym przypadku wybierz y').upper()
            if choice == 'X':
                print('Do widzenia!')
                break
            elif choice == 'Y':
                continue
            else:
                print('podano zły znak. Do widzenia!')
                break
        return
    except:
        print('Błędnie wprowadzony znak!')

def division():
    try:
        print("Jakie liczby chcesz dzielić?")
        while True:
            first = float(input("Pierwsza liczba"))
            second = float(input("Druga liczba"))
            result = first / second
            print(f'Wynik działania {first} / {second}  = {result}')
            choice = input('Jeżeli chcesz wyjść wybierz x w innym przypadku wybierz y').upper()
            if choice == 'X':
                print('Do widzenia!')
                break
            elif choice == 'Y':
                continue
            else:
                print('podano zły znak. Do widzenia!')
                break
        return
    except ZeroDivisionError: print('Nie dziel przez zero!')
    except ValueError: print('Błędnie wprowadzony znak!')
#dopisz manu

