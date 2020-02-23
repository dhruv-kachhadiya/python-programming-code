class car():
    def __init__(self,company,model,price):
        self.company=company
        self.model=model
        self.price=price

    def inc_price(self):
        self.price=int(self.price*1.1)


car1=car('honda','city',100000)
car2=car('tata','bolt',500000)


print(car1.price)
car1.inc_price()
print(car1.price)

print(car1.__dict__)
print(car2.__dict__)
