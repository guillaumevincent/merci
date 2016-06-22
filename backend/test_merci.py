import uuid
import datetime
import unittest

from freezegun import freeze_time


class Entreprise:
    def __init__(self):
        self.récompenses = []
        self.salariés = []

    def embauche(self, salarié):
        self.salariés.append(salarié)

    def répartition_des_merci(self, salarié):
        comptage = {}
        total = 0
        autres_salariés = [s for s in self.salariés if s != salarié]
        if not salarié.remerciements:
            for autre_salarié in autres_salariés:
                total += 1
                comptage[autre_salarié.id] = 1

        for merci in salarié.remerciements:
            uid = merci.destinataire.id
            comptage[uid] = comptage.get(uid, 0) + 1
            total += 1
        répartition = {}
        for uid, nombre_de_merci in comptage.items():
            répartition[uid] = round(100 * nombre_de_merci / total)
        return répartition

    def récompense(self):
        quand = datetime.datetime.now()
        for salarié in self.salariés:
            for uid, récompense in self.répartition_des_merci(salarié).items():
                self.récompenses.append({'quand': quand, 'id': uid, 'récompense': récompense})

    def solde(self, qui, date1, date2):
        comptage = {}
        total = 0
        for récompense in self.récompenses:
            quand = récompense['quand']
            id = récompense['id']
            montant = récompense['récompense']
            if date1 <= quand <= date2:
                comptage[id] = comptage.get(id, 0) + montant
                total += montant
        return {'pourcentage': round(100 * comptage[qui] / total), 'montant': comptage[qui]}


class Salarié:
    def __init__(self, nom='', prénom=''):
        self.nom = nom
        self.prénom = prénom
        self.remerciements = []
        self.id = str(uuid.uuid4())

    def remercie(self, salarié, raison=''):
        self.remerciements.append(Merci(self, salarié, raison))


class EntrepriseADeuxSalariés(Entreprise):
    def __init__(self):
        super().__init__()
        guillaume = Salarié()
        édouard = Salarié()
        self.salariés.append(guillaume)
        self.salariés.append(édouard)


class EntrepriseCasDeTests(unittest.TestCase):
    def test_entreprise_peut_ajouter_un_salarié(self):
        entreprise = Entreprise()
        guillaume = Salarié()
        entreprise.embauche(guillaume)
        self.assertEqual(entreprise.salariés, [guillaume])

    def test_calcule_la_répartition_des_merci_pour_un_salarié(self):
        guillaume = Salarié()
        édouard = Salarié()
        po = Salarié()
        guillaume.remercie(édouard)
        guillaume.remercie(po)

        entreprise = Entreprise()
        entreprise.salariés = [guillaume, édouard, po]
        répartition = entreprise.répartition_des_merci(guillaume)
        self.assertEqual(répartition[édouard.id], 50)
        self.assertEqual(répartition[po.id], 50)

    def test_larrondi_de_la_répartition_des_merci_pour_un_salarié(self):
        guillaume = Salarié()
        édouard = Salarié()
        po = Salarié()
        guillaume.remercie(édouard)
        guillaume.remercie(po)
        guillaume.remercie(po)

        entreprise = Entreprise()
        entreprise.salariés = [guillaume, édouard, po]
        répartition = entreprise.répartition_des_merci(guillaume)
        self.assertEqual(répartition[édouard.id], 33)
        self.assertEqual(répartition[po.id], 67)

    def test_la_répartition_si_aucun_merci(self):
        guillaume = Salarié()
        édouard = Salarié()
        po = Salarié()

        entreprise = Entreprise()
        entreprise.salariés = [guillaume, édouard, po]
        répartition = entreprise.répartition_des_merci(édouard)
        self.assertEqual(len(répartition), 2)
        self.assertEqual(répartition[guillaume.id], 50)
        self.assertEqual(répartition[po.id], 50)

    @freeze_time("2016-06-22")
    def test_récompenser_chaque_salarié(self):
        guillaume = Salarié()
        édouard = Salarié()
        po = Salarié()
        guillaume.remercie(édouard)
        guillaume.remercie(po)
        guillaume.remercie(po)

        entreprise = Entreprise()
        entreprise.salariés = [guillaume, édouard, po]
        entreprise.récompense()

        self.assertCountEqual(entreprise.récompenses, [
            {'quand': datetime.datetime(2016, 6, 22), 'id': édouard.id, 'récompense': 33},
            {'quand': datetime.datetime(2016, 6, 22), 'id': po.id, 'récompense': 67},
            {'quand': datetime.datetime(2016, 6, 22), 'id': guillaume.id, 'récompense': 50},
            {'quand': datetime.datetime(2016, 6, 22), 'id': po.id, 'récompense': 50},
            {'quand': datetime.datetime(2016, 6, 22), 'id': guillaume.id, 'récompense': 50},
            {'quand': datetime.datetime(2016, 6, 22), 'id': édouard.id, 'récompense': 50},
        ])

    def test_peut_donner_pourcentage_entre_deux_dates(self):
        entreprise = Entreprise()
        entreprise.récompenses = [
            {'récompense': 50, 'quand': datetime.datetime(2016, 6, 21), 'id': '8012f30f-f161-45d7-b7c5-937b643e9740'},
            {'récompense': 50, 'quand': datetime.datetime(2016, 6, 22), 'id': 'e8a4465c-4b24-4d3d-b41f-ca67018b26d5'},
            {'récompense': 50, 'quand': datetime.datetime(2016, 6, 22), 'id': 'ea8c4894-3522-4643-8078-2a3dba030927'},
            {'récompense': 50, 'quand': datetime.datetime(2016, 6, 22), 'id': 'e8a4465c-4b24-4d3d-b41f-ca67018b26d5'},
            {'récompense': 50, 'quand': datetime.datetime(2016, 6, 24), 'id': 'ea8c4894-3522-4643-8078-2a3dba030927'},
            {'récompense': 50, 'quand': datetime.datetime(2016, 6, 25), 'id': '8012f30f-f161-45d7-b7c5-937b643e9740'}
        ]
        solde1 = entreprise.solde('e8a4465c-4b24-4d3d-b41f-ca67018b26d5', datetime.datetime(2016, 6, 22),
                                  datetime.datetime(2016, 6, 22))
        self.assertEqual(solde1['pourcentage'], 67)
        self.assertEqual(solde1['montant'], 100)
        solde2 = entreprise.solde('e8a4465c-4b24-4d3d-b41f-ca67018b26d5', datetime.datetime(2016, 6, 22),
                                  datetime.datetime(2016, 6, 25))
        self.assertEqual(solde2['pourcentage'], 40)


class SalariéCasDeTests(unittest.TestCase):
    def test_un_salarié_a_un_identifiant_unique(self):
        guillaume = Salarié()
        self.assertTrue(guillaume.id)

    def test_salarié_peut_remercier_quelquun(self):
        guillaume = Salarié()
        édouard = Salarié()
        guillaume.remercie(édouard)
        self.assertEqual(len(guillaume.remerciements), 1)

    def test_salarié_peut_préciser_la_raison_dun_merci(self):
        guillaume = Salarié()
        édouard = Salarié()
        guillaume.remercie(édouard, 'sans raison')
        self.assertEqual(guillaume.remerciements[0].raison, 'sans raison')


class Merci:
    def __init__(self, émetteur, destinataire, raison=''):
        self.raison = raison
        self.quand = datetime.datetime.now()
        self.émetteur = émetteur
        self.destinataire = destinataire


class MerciEntreDeuxPersonnes(Merci):
    def __init__(self, *args, **kwargs):
        self.émetteur = Salarié()
        self.destinataire = Salarié()
        super().__init__(self.émetteur, self.destinataire, *args, **kwargs)


class RemerciementCasDeTests(unittest.TestCase):
    @freeze_time("2016-06-21")
    def test_merci_a_une_date_de_création_correspondant_à_maintenant(self):
        merci = MerciEntreDeuxPersonnes()
        self.assertEqual(merci.quand, datetime.datetime(2016, 6, 21))

    def test_un_merci_peut_avoir_une_raison(self):
        merci = MerciEntreDeuxPersonnes(raison='sans raison')
        self.assertEqual(merci.raison, 'sans raison')

    def test_un_merci_a_un_émetteur_et_un_destinataire(self):
        guillaume = Salarié()
        édouard = Salarié()
        merci = Merci(émetteur=guillaume, destinataire=édouard)
        self.assertEqual(merci.émetteur, guillaume)
        self.assertEqual(merci.destinataire, édouard)


if __name__ == '__main__':
    unittest.main()
