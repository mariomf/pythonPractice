
try:
    a = int(input("Dame un numero "));
    b = int(input("Dame otro numer "));
except ValueError:
    print("Eso no es un numero");
else:
    suma = a + b;
    print("La suma es: " + str(suma));
