class StudentWallet:
    def __init__(self,nim,pin,balance):
        self.__nim = nim
        self.__pin = pin
        self.__balance = balance
    
    def show_nim(self):
        return self.__nim
    
    def verify_pin(self, pin):
        if pin == self.__pin:
            print("PIN correct")
        else:
            print("PIN incorrect")
    
        
    def show_balance(self):
        return self.__balance
    
    def check_balance(self,nim):
        if nim == self.__nim:
            print(f"your balance is {self.__balance}")
            return
        print(f"your nim is incorrect !!!")
    
    def add_balance(self,pin,amount):
        if pin == self.__pin:
            if amount > 0:
               self.__balance += amount
               print(f"your top up {amount} was succesful, yout balance is: {self.__balance}")
            else:
                print(f"must be above 0")
        else:
            print(f"your pin is incorrect !!!")
        
    def withdraw_balance(self,pin,amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                if amount > 0:
                    self.__balance -= amount
                    print(f"withdrawal is succesful")
                    print(f"remaining balance: {self.__balance}")
                else:
                    print(f"must be above 0")
            else:
                print(f"Insufficient balance")
        else:
            print(f"your pin is incorrect !!!")
            
puntodewo = StudentWallet(689695,2021,100000)
werkudoro = StudentWallet(690696,2022,200000)
ontoseno = StudentWallet(691697,2023,300000)

# check identity
print(puntodewo.show_nim())
ontoseno.verify_pin(2023)
print(werkudoro.show_balance())

# correct processing
werkudoro.check_balance(690696)
ontoseno.add_balance(2023,50000)
puntodewo.withdraw_balance(2021,25000)

# incorrect processing
puntodewo.check_balance(693699)
werkudoro.add_balance(2026,50000)
ontoseno.withdraw_balance(2023,400000)

# cannot acces private attribute
# print(puntodewo.__balance)
# ERROR because __balance is private


        
        
        
