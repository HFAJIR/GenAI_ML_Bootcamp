class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        label = self.currency + ("s" if self.amount != 1 else "")
        return f"{self.amount} {label}"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency != other.currency:
                print(f"you can not add {self.currency} and {other.currency}")
                return None
            return self.amount + other.amount
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        if isinstance(other, Currency):
            if self.currency != other.currency:
                print(f"Impossible d’additionner {self.currency} et {other.currency}")
                return self
            self.amount += other.amount
            return self
        return NotImplemented
# Tests

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)          
print(int(c1))     
print(repr(c1))    
print(c1 + 5)      
print(c1 + c2)    
print(c1)          

c1 += 5
print(c1)         

c1 += c2
print(c1)          
print(c1 + c3)    
