# version 2
def puissance():
    x = int(input(" entrer un nombre \n"))
    n = int(input("entre la puissance \n "))

    puiss  = 1;

    for i in range(n):
     puiss = puiss * x


    print(str(x) + " a la puissance" + str(n) + " est : " + str(puiss))

if __name__ == '__main__':
    puissance()