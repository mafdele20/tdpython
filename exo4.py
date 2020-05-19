import math


def puissnace():
#version 1
        x = int(input(" entrer un nombre \n"))
        n =int (input("entre la puissance\n "))

        print(str(x)+" a la puissance "+str(n)+" est : "+str(math.pow(x,n)))


def puissance2():
    x = int(input(" entrer un nombre \n"))
    n = int(input("entre la puissance \n "))

    puiss  = 1;

    for i in range(n):
     puiss = puiss * x


    print(str(x) + " a la puissance" + str(n) + " est : " + str(puiss))

if __name__ == '__main__':
    puissnace()
    puissance2()