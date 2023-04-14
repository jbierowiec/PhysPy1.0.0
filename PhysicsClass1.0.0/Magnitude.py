import re

class Magnitude:

    def convert(self, order):

        if (isinstance(order, str)):
            num = re.sub('[^0-9.]','', order)
        
            calc = float(num)

            if calc >= 10**-24 and calc < 10**-21:
                return self.yocto(order)

            elif calc >= 10**-21 and calc < 10**-18:
                return self.zepto(order)

            elif calc >= 10**-18 and calc < 10**-15:
                return self.atto(order)

            elif calc >= 10**-15 and calc < 10**-12:
                return self.femto(order)

            elif calc >= 10**-12 and calc < 10**-9:
                return self.pico(order)

            elif calc >= 10**-9 and calc < 10**-6:
                return self.nano(order)

            elif calc >= 10**-6 and calc < 10**-3:
                return self.micro(order)

            elif calc >= 10**-3 and calc < 10**-2:
                return self.milli(order)
        
            elif calc >= 10**-2 and calc < 10**-1:
                return self.centi(order)

            elif calc >= 10**-1 and calc < 10**0:
                return self.deci(order)

            elif calc >= 10**0 and calc < 10**1:
                return order

            elif calc >= 10**1 and calc < 10**2:
                return self.deca(order)

            elif calc >= 10**2 and calc < 10**3:
                return self.hecto(order)
        
            elif calc >= 10**3 and calc < 10**6:
                return self.kilo(order)
        
            elif calc >= 10**6 and calc < 10**9:
                return self.mega(order)

            elif calc >= 10**9 and calc < 10**12:
                return self.giga(order)

            elif calc >= 10**12 and calc < 10**15:
                return self.tera(order)

            elif calc >= 10**15 and calc < 10**18:
                return self.peta(order)

            elif calc >= 10**18 and calc < 10**21:
                return self.exa(order)

            elif calc >= 10**21 and calc < 10**24:
                return self.zetta(order)

            elif calc >= 10**24 and calc < 10**27:
                return self.yotta(order)
        
            else:
                return calc
            
        elif (isinstance(order, float)):
            calc = float(num)
            return calc

        
    # lower end


    def yocto(self, order):
        u = ' y'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-24))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def zepto(self, order):
        u = ' z'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-21))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def atto(self, order):
        u = ' a'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-18))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def femto(self, order):
        u = ' f'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-15))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def pico(self, order):
        u = ' p'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-12))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def nano(self, order):
        u = ' n'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-9))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def micro(self, order):
        u = ' µ'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-6))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def milli(self, order):
        u = ' m'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-3))
        string_addition = (u + result2)

        return str(calc) + string_addition
    
    def centi(self, order):
        u = ' c'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-2))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def deci(self, order):
        u = ' d'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**-1))
        string_addition = (u + result2)

        return str(calc) + string_addition
    
    
    # higher end


    def deca(self, order):
        u = ' da'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**1))
        string_addition = (u + result2)

        return str(calc) + string_addition
    
    def hecto(self, order):
        u = ' h'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**2))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def kilo(self, order):

        u = ' k'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**3))
        string_addition = (u + result2)

        return str(calc) + string_addition
        
    def mega(self, order):
        u = ' M'

        result1 = re.sub('[^0-9.-]', '', order)
        result2 = re.sub(r'[\s\d.-]+', '', order)

        calc = float(float(result1)/(10**6))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def giga(self, order):
        u = ' G'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**9))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def tera(self, order):
        u = ' T'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**12))
        string_addition = (u + result2)

        return str(calc) + string_addition
    
    def peta(self, order):
        u = ' P'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**15))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def exa(self, order):
        u = ' E'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**18))
        string_addition = (u + result2)

        return str(calc) + string_addition

    def zetta(self, order):
        u = ' Z'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**21))
        string_addition = (u + result2)

        return str(calc) + string_addition
    
    def yotta(self, order):
        u = ' Y'

        result1 = re.sub('[^0-9.-]','', order)
        result2 = re.sub(r'[\s\d\.-]+', '', order)

        calc = float(float(result1)/(10**24))
        string_addition = (u + result2)

        return str(calc) + string_addition
    