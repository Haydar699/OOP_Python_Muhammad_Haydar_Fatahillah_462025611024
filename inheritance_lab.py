class Grandpa:
    def greeting(self):
        print('this is our family')

class Father(Grandpa):
    def greeting(self):
        print("this is my father family")
        super().greeting()

class Uncle(Grandpa):
    def greeting(self):
        print("this is my uncle family")
        super().greeting()

class Son(Father, Uncle):
    def greeting(self):
        
        print("this is my family")
        super().greeting()

tommy = Son()
tommy.greeting()
