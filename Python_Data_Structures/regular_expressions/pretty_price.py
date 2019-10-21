#My Solution
import math
class Pretty_Price:
    def __init__(self, price, new_change):
        self.price = price
        self.new_change = str(new_change)

    def render(self):
        dollar_amount = math.floor(self.price)
        dollar_amount = str(dollar_amount)
        if '.' in self.new_change:
            dollar_amount += self.new_change
        else:
            dollar_amount += str((int(self.new_change))/100)

        return dollar_amount
price = Pretty_Price(3.50, 99)
price2 = Pretty_Price(3.50, .99)

def price_render(variable):
    print(variable.render())

price_render(price)
price_render(price2)

#Instructor Solution
def instructor_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01
    return int(gross_price) + extension
print(instructor_price(3.50, 0.95))
print(instructor_price(3.50, 95))