
def resistance():

    R1 = float(input("entre la resistance R1\n"))

    R2 = float(input("entre la resistance R1\n"))

    R3 = float(input("entre la resistance R1\n"))

    rserie = R1 + R2 + R3;

    rpara = (R1 * R2 * R3) / (R1 * R2 + R2 * R3 + R1 * R3);
    # python 2.x
    print("1--resistance en serie")
    print ("2--resistance en parallele")
    while 1:
        i = int(input("Choisissez 1 ou 2: "))
        if i not in [1, 2]:
            print("Choix incorrect !")
        elif i==1 :
             frqserie = (R1 / rserie) + (R2 / rserie) + (R3 / rserie);
             print("la fréquence en serie est: " + str(frqserie));
        else:
             frqpara = (R1 / rpara) + (R2 / rpara) + (R3 / rpara)
             print("la fréquence en parallèle est: " + str(frqpara))


if __name__ == '__main__':
    resistance()




