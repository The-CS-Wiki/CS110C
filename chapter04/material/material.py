#
#  Author: Benjamin Herrera
#


class Material:
    def __init__(self, cost, durability, material_uid):
        self.cost = cost
        self.durability = durability
        self.material_uid = material_uid

    def info(self):
        print(f"{self.material_uid} >> {self.cost}, {self.durability}")
