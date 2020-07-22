class complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def display(self):
        print(str(self.real)+"+"+str(self.imaginary)+"i")
        
    def add(self,a):
        real_total = self.real + a.real
        imag_total = self.imaginary + a.imaginary
        return complex(real_total,imag_total)
    
    def subtract(self,a):
        real_total = self.real - a.real
        imag_total = self.imaginary - a.imaginary
        return complex(real_total,imag_total)
        
    def multiply(self,a):
        real_total = self.real*a.real - self.imaginary*a.imaginary
        imag_total = self.real*a.imaginary + self.imaginary*a.real
        return complex(real_total,imag_total)
        
    def modulus(self):
        print((self.real**2 + self.imaginary**2)**(0.5))
        
    def conjugate(self):
        return complex(self.real,-self.imaginary)
        
    def inverse(self):
        divisor = self.real**2 + self.imaginary**2
        return complex(self.real/divisor,-self.imaginary/divisor)
        