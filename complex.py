class Complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
       
    def show_number(self):
        print(self.real,"i+", self.img, "j")

    def add(self, num2):
        newReal= self.real + num2.real
        newIMg= self.img + num2.img
        return Complex(newReal, newIMg)
    
    def sub(self, num2):
        newReal= self.real - num2.real
        newIMg= self.img - num2.img
        return Complex(newReal, newIMg)


num1= Complex(1,3)
num1.show_number()

num2=Complex(2,4)
num2.show_number()

num3=num1.add(num2)
num3.show_number()

num4=num1.sub(num2)
num4.show_number()