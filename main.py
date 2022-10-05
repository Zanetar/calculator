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

def menu():
    try:
        while True:
            print('Witaj w kalkulatorze')
            print('Co chcesz zrobić?')
            print('1----dodawanie')
            print('2----odejmowanie')
            print('3----mnożenie')
            print('4----dzielenie')
            print('0----wyjście')
            choice=int(input())
            if  choice==1:
                plus()
            elif choice==2:
                minus()
            elif choice==3:
                multi()
            elif choice==4:
                division()
            elif choice==0:
                break
            else:
                print('Wybrano zły znak!')
    except: print ('Wybrano zły znak!')

menu() #wywołanie kalkulatora
