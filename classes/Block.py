import hashlib

import uuid

# Création de la classe Block

class Block:
    def __init__(self, unique_id, hash, base_hash, parent_hash, transactions ):
        self.unique_id = unique_id
        self.hash = hash
        self.base_hash = base_hash
        self.parent_hash = parent_hash
        self.transactions = transactions


# instanciation de l'objet Block

block1 = Block("001", "000024rty", {"jason":"maris"},("00AZE") ,"{2000, 5000, 7000}")


# Definition des methodes

# Definition de la methode check_hash
def check_hash(self, hash):
    print("{} check_hash : {}".format(self.check_hash, hash))


# Definition de la methode add_transaction
def add_transaction(self, transaction):
    print("{} add_transaction : {}".format(self.transaction, transaction))



# Definition de la methode get_transaction
def get_transaction(self, transaction):
    print("{} get_transaction : {}".format(self.get_transaction, transaction))



# Definition de la methode get_weight
def get_weight(self):
    header_bin = (str(self.unique_id) + 
                  str(self.hash) +
                  str(self.base_hash) + 
                  str(self.parent_hash) +
                  str(self.transactions)).encode()

    inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
    outer_hash = hashlib.sha256(inner_hash).hexdigest()
    return outer_hash

# Definition de la methode save
def save(self, hash):
    print("{} save : {}".format(self.save, hash))




# Definition de la methode load
def load(self, hash):
    print("{} load : {}".format(self.load, hash))


