from sympy import symbols
from sympy.printing.latex import latex
import re

#x = symbols('x')
#expr = x**2
#print(latex(expr))

class Units:


    # base units


    # mass = kg (kilogram)
    def mass(self, number):
        u = ' kg'
        return str(number) + u
    
    # time = s (second)
    def time(self, number):
        u = ' s'
        return str(number) + u
    
    # length = m (meter)
    def length(self, number):
        u = ' m'
        return str(number) + u
    
    # temperature = K (Kelvin)
    def tempertature(self, number):
        u = ' K'
        return str(number) + u
    
    # mole = mol (amount of substance)
    def mole(self, number):
        u = ' mol'
        return str(number) + u
    
    # ampere = A (electric current)
    def ampere(self, number):
        u = ' A'
        return str(number) + u
    
    # candela = cd (light intensity)
    def candela(self, number):
        u = ' cd'
        return str(number) + u
    

    # kinematic units 
    

    # velocity = m/s (meter per second)
    def velocity(self, number):
        u = ' (m/s)'
        return str(number) + u

    # acceleration = m/s^2 (meter per second squared)
    def acceleration(self, number):
        u = ' (m/s^{two})'
        #u = symbols(' m/s')
        #expr = u**2
        #print(latex(expr))
        #r = ' ' + latex(expr)
        return str(number) + u
    
    # force = kg * m / s^2 (kilogram times meter per second squared)
    def force(self, number):
        u = ' N'
        return str(round(number, 6)) + u
    
    # joule = kg * m^2 / s^2 (kilogram times meter squared per second squared)
    def joule(self, number):
        u = ' J'
        return str(number) + u
    
    # pascal = kg / m * s^2 / (kilogram per meter times second squared)
    def pascal(self, number):
        u = ' Pa'
        return str(number) + u
    

    # space units


    # area = m^2 (meter squared)
    def area(self, number):
        u = ' (m^{two})'
        return str(number) + u
    
    # volume = m^3 (meter cubed)
    def volume(self, number):
        u = ' (m^{three})'
        return str(number) + u
    
    # specific volume = m^3/kg (meter cubed per kilogram)
    def specific_volume(self, number):
        u = ' (m^{three}/kg)'
        return str(number) + u
    
    # density = kg/m^3 (kilogram per meter cubed)
    def density(self, number):
        u = ' ρ'
        return str(number) + u
    

    # electric units


    # current density = A/m^2 (ampere per meter squared)
    def current_density(self, number):
        u = ' (A/m^{two})'
        return str(number) + u

    # magnetic field strength = A/m (ampere per meter)
    def magnetic_field_strength(self, number):
        u = ' (A/m)'
        return str(number) + u
    
    # coulomb = A*s (ampere times second)
    def coulomb(self, number):
        u = ' C'
        return str(number) + u


class BaseUnits:


    # kinematic units 


    # force = kg * m / s^2 (kilogram times meter per second squared)
    def force(self, number):
        u = ' (kg*m/s^{two})'
        return str(number) + u
    
    # joule = kg * m^2 / s^2 (kilogram times meter squared per second squared)
    def joule(self, number):
        u = ' (kg*m^{two}/s^{two})'
        return str(number) + u
    
    # pascal = kg / m * s^2 / (kilogram per meter times second squared)
    def pascal(self, number):
        u = ' (kg/m*s^{two})'
        return str(number) + u
    

    # space units


    # density = kg/m^3 (kilogram per meter cubed)
    def density(self, number):
        u = ' (kg/m^{three})'
        return str(number) + u
    

    # electric units


    # coulomb = A*s (ampere times second)
    def coulomb(self, number):
        u = ' (A*s)'
        return str(number) + u
    