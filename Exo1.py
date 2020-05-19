def main() :
    a = int(input("entrer le dividende "))
    # diviseur
    b = int(input("entrer le diviseur"))
    # reste
    rt = a % b
    qe = a // b
    qr = a / b
    print("les quotient entier : " + str(qe))
    print("les quotient reel : " + str(qr))
    print("’ le reste est : " + str(rt))

if __name__ == '__main__':

   main()