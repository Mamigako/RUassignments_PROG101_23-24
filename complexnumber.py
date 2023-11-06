class ComplexNumber:
    def __init__(self, real = 0, imaginary = 0) -> None:
        self.__real = real
        self.__imaginary = imaginary


    def re(self):
        return self.__real


    def im(self):
        return self.__imaginary


    def conjugate(self):
        return ComplexNumber(self.re(),-self.im())


    def __neg__(self):
        return ComplexNumber(-self.re(),-self.im())
    

    def __str__(self) -> str:
        if not self.__real and not self.__imaginary:
            return "0"

        if not self.__real:
            return "{0}i".format(self.__imaginary)

        if not self.__imaginary:
            return "{0}".format(self.__real)

        if self.__imaginary < 0:
            return "{0} - {1}i".format(self.__real, abs(self.__imaginary))
        
        if self.__imaginary > 0:
            return "{0} + {1}i".format(self.__real, self.__imaginary)


    def __neg__(self):
        return ComplexNumber(-self.re(), -self.im())


    def __repr__(self):
        return "ComplexNumber({0}, {1})".format(self.__real, self.__imaginary)


    def __eq__(self, __other) -> bool:
        return self.re() == __other.re() and self.im() == __other.im()


    def __add__(self, other):
        return ComplexNumber(self.re() + other.re(), self.im() + other.im())


    def __sub__(self, other):
        return ComplexNumber(self.re() - other.re(), self.im() - other.im())


    def __mul__(self, other):
        real = self.re()*other.re() - self.im()*other.im()
        imaginary = self.re()*other.im() + self.im()*other.re()
        return ComplexNumber(real, imaginary)


    def inverse(self):
        denominator = pow(self.re(), 2) + pow(self.im(), 2)
        real_fraction = self.re()/denominator
        imaginary_fraction = self.im()/denominator
        return ComplexNumber(real_fraction, -imaginary_fraction)


    def __truediv__(self, other):
        return self * other.inverse() 
    
