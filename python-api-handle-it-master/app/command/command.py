from app.machine.machine import Machine

machine = Machine()

var = ''

while var != 'quitter':
    var = input(str("'machine' ou 'application' ou 'quitter' : "))
    if var == 'machine':
        action = input(str("'liste', 'afficher', 'ajouter', modifier ou 'supprimer': "))
        if action == 'liste':
            print(machine.liste())
        else :
            name = input(str('Nom de la machine: '))
            if action =='afficher':
                print(machine.get(name))
            elif action == 'supprimer':
                machine.delete(name)
            elif action == 'ajouter':
                print ('on demande les données')
            elif action == 'modifier':
                print('on recupere les données avec le nom et on propose de les modifier')
            else:
                print('Merci de saisir un choix valide')
    elif var == 'application':
        print("L'entrée n'est pas un palindrome")
    else:
        print('Merci de saisir un choix valide')