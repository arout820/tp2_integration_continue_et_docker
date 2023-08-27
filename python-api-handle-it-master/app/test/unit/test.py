import unittest
import json
import HtmlTestRunner

from application.application import Application
from machine.machine import Machine

class TestApplication(unittest.TestCase):
    # Initialisation de données pour mes tests
    # def setUp(self):
    #     self.demo_donnes=('ma_super_liste',1)
    
    # # Nettoyage après les tests
    # def tearDown(self) -> None:
    #     print('Je nettoie les données')
    #     return super().tearDown()
    

    # Exemple de test avec un echec (failure)
    # def test_liste_application_ko(self):
    #     contenu_liste = Application.liste()
    #     self.assertEqual(contenu_liste,'Une phrase')

    def test_liste_application_ok(self):
        contenu_liste = Application.liste()
        self.assertEqual(contenu_liste,'Liste des applications')

    def test_add_application(self):
        add_app = Application.add(('ma_super_liste',1))
        self.assertEqual(add_app,'Application ajoutée')

# class TestMachines(unittest.TestCase):
#     def test_ajout_machine(self):
#         Machine.fichier="machines.json"
#         ajout_machine = Machine.add(Machine,'{"donnees":"mes donnees à écrire"}')
#         with open('machines.json', 'r') as f:
#             try:
#                 contenu_fichier = json.load(f)
#             except Exception as e:
#                 print("Exception raised | %s " % str(e))
#                 exit()
#         self.assertEqual(contenu_fichier,{"donnees":"mes donnees à écrire"})



test1 = unittest.TestLoader().loadTestsFromTestCase(TestApplication)
suite = unittest.TestSuite([test1])
runner = HtmlTestRunner.HTMLTestRunner(verbosity=2, output='reports/unittest', report_name='report')
runner.run(suite)


if __name__ == "__main__":
    unittest.main()