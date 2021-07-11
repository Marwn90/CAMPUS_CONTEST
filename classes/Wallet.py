import uuid

import hashlib


# Création de la classe Wallet

class Wallet:
    def __init__(self, unique_id, balance, history):
        self.unique_id = unique_id
        self.balance = balance
        self.history = history



# instanciation de l'objet Chain

# Creation du premier objet  wallet1
wallet1 = Wallet("01", "0", "{100, 500, 10000}")

# Creation du second wallet2
wallet2 = Wallet("02", "2000", "{300, 6000, 5000}")



# Definition de la methode generate_unique_id
def generate_unique_id(self, unique_id):
    unique_id = id.get_unique_id(unique_id)
    print("{} a genere : {}".format(self.unique_id, unique_id))
    return generate_unique_id




# Definition de la methode add_balance


def add_balance(self, balance):
    uuid.balance= int(input(0))
    n=1000
    for i in range (1, n):
         balance= i+ balance
         print(balance)
    # new_balance = 1000
    # for i in range(1000, 10000):
    #       new_balance = new_balance + i
    #       print("la somme vaut")



# Definition de la methode sub_balance
def sub_balance(self, balance):
    print("{} sub : {}".format(self.sub_balance, balance))



# Definition de la methode send
def send(self, history):
    print('send of history')
    return self.history




# Definition de la methode save
def save(self, history):
    print('sauvegarde des history')
    return save.history


# Definition de la methode load
def load(self, history):
    pass