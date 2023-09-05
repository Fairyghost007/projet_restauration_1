import os


def effacer_ecran():
    # pour nettoyer le terminal apres chaque utilisation
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('clear')


def menu_generale():
    print("--------- MENU ---------")  
    print("1)--------- Plat du jour ---------")
    print("2)--------- Fast Food ---------")
    print("3)--------- Quitter ---------")
    print("4)--------- Caisse ---------")
    saisir_entier(1,4,"Faite votre choix\ne")


def saisir_entier(min,max,expression):
    ok=False
    while ok==False:
        choix = input(expression)
        if choix.isdigit():
            # verifie si c'est un digit
            choix=int(choix)
            if(choix>=min and choix<=max):
                return choix
        else:
            print(expression)


menu_generale()