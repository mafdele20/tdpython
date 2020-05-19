import math

def main() :
    r =int(input("entrer le reyon"))
    pi =float( 4 * math.atan(1))
    prm= r * pi * 2
    surf = pi * r * r
    print("le perimetre est : " + str(prm)+ " cm et la surface est : " + str (surf) + " cm²")


if __name__ == '__main__':
   main()