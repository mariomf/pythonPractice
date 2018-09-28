def pedir_pizza():
    print("pedir pizza")


pedir_pizza();


def checar_entrada(edad):
    if edad == 21:
        print("puedes entrar al bar".upper());
        print("y tambien puedes beber");
    elif edad <= 18:
        print("no puedes entrar");
    else:
        print("puedes hacer todo");


checar_entrada(21)
