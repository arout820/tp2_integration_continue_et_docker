import json

class Machine():

    fichier = 'machine/machines.json'

    def __init__(self):
        self.nom = 'Nom par défaut'
        self.ip = '10.0.0.1'
        self.cpu = '1'
        self.ram = '4'
        self.disques = [{'0': '10Go'}, {'1':'30Go'}] 
        self.os = {'ubuntu':'20.04'}

    def add(self, data):
        # Pour écrire 
        with open(self.fichier, 'w') as f:
            f.write(str(data))
            return 'Machine ajoutée'
    
    def get(self, nom):
        return nom
    
    def liste(self):
        with open(self.fichier, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print("Exception raised | %s " % str(e))
                exit()
        return data

    def edit(self,name,data):
        return 'Machine modifiée'
    
    def delete(self,name):
        return 'Machine supprimée'
