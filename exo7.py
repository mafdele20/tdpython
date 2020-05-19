
def decomposition():

     montant =  int(input("saisir un montant"))
     if montant < 0:
      print("error")
     else:
            billet20 = (montant // 20)
            rest = (montant % 20)
            billet10 = (rest // 10)
            rest = (rest % 10)
            billet5 = (rest // 5)
            rest = (rest % 5)
            piece2 = (rest // 2)
            piece1 = (rest % 2)

            print(str(montant) + " est composé de " +str(billet20) + " billet de 20 ,"
            +str(billet10)+ " billet de 10 ," +str(billet5) + "billet de 5 ,"
            +str(piece2)+ "pieces de 2 et "+str(piece1) + " piece de 1 ,")


if __name__ == '__main__':
    decomposition()