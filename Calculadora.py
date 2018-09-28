def realizar_operacion(opcion):
    if opcion == '1':
        try:
            a = int(input("Dame un numero "));
            b = int(input("Dame otro numer "));
        except ValueError:
            print("Eso no es un numero");
        else:
            suma = a + b;
            print("La suma es: " + str(suma));
    elif opcion == '2':
        try:
            a = int(input("Dame un numero "));
            b = int(input("Dame otro numer "));
        except ValueError:
            print("Eso no es un numero");
        else:
            suma = a - b;
            print("El resultado es: " + str(suma));
    elif opcion == '3':
        try:
            a = int(input("Dame un numero "));
            b = int(input("Dame otro numer "));
        except ValueError:
            print("Eso no es un numero");
        else:
            suma = a * b;
            print("El resultado es: " + str(suma));
    elif opcion == '4':
        try:
            a = int(input("Dame un numero "));
            b = int(input("Dame otro numer "));
        except ValueError:
            print("Eso no es un numero");
        else:
            suma = a / b;
            print("El resultado es: " + str(suma));


flag = 'si';
while flag == 'si':
    print("\n"+"Bienvanido a la calculadora"+"\n"+
          "Estas son las operaciones que puedes ralizar:"+"\n"+
          "1 - Suma"+"\n"+
          "2 - Resta"+"\n"+
          "3 - Multiplicacion"+"\n"+
          "4 - Division"+"\n")
    opcion = input("Introduce el numero de operacion quieres realizar: ");


    realizar_operacion(opcion)

    flag = input("Deseas continuar? si/no ");