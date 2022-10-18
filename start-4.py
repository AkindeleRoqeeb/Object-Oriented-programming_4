
class item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        ############### run validation to the recieve argument ######################
        # assert price >= 0
        ##################### OR ###############
        assert price >= 0, f"price {price} is not greater or equal zero"

        # assert quality >= 0
        ##################### OR ###############
        assert quality >= 0, f"quality {quality} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quality

########################################################### notice the int that is use as str ##########################
# item1 = item('laptop', 300, 3, -2)
item1 = item('laptop', 300, 3, 2)
item2 = item('phone', 100, 43, 5)

print(item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

############################################################
print(item.__dict__) # All the attributes for class lavel
print(item1.__dict__) # All the attributes for instance lavel

##############################################################################################################


class item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        ############### run validation to the recieve argument ######################
        # assert price >= 0
        ##################### OR ###############
        assert price >= 0, f"price {price} is not greater or equal zero"

        # assert quality >= 0
        ##################### OR ###############
        assert quality >= 0, f"quality {quality} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quality

    def apply_discount(self):
        self.price = self.price * self.pay_rate

########################################################### notice the int that is use as str ##########################
item1 = item('laptop', 300, 3, 2)
item1.apply_discount()
print(item1.price)

item2 = item('phone', 100, 43, 5)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
