import hashlib

import uuid


# Création de la classe Chain

class Chain:
    def __init__(self, blocs, last_transactions_number):
        self.blocs = [12, 45, 6]
        self.last_transactions_number = {"0101"}






# Definition de la methode generate_hash
def generate_hash(self):
    print("{} generate_hash : {}".format(self.generate_hash, hash))




# Definition de la methode verify_hash
def verify_hash(self):
    print("{} verif_hash : {}".format(self.verif_hash, hash))



# Definition de la methode add_block
def add_block(self):
    print("{} add_block : {}".format(self.add_block, hash))



# Definition de la methode get_block
def get_block(self):
    header_bin = (str(self.blocs) +
                  str(self.last_transactions_number)).encode()




# Definition de la methode add_transaction
def add_transaction(self, hash):
    print("{} add_transaction : {}".format(self.add_transaction, hash))
