
def somme():
    tous = 0

    def som(x):
        return tous + x


    for i in range(5):
        val = int(input("entrer un nombre entier \n"))
        tous = som(val)



    print(" la somme des 5 valeurs est :" +str(tous))

if __name__ == '__main__':
    somme()