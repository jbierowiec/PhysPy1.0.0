import math
import re
from Units import Units
from Magnitude import Magnitude
from Constants import Constants

units = Units()
magnitude = Magnitude()
constants = Constants()

class Formulas:
    def distance(self, x1, x2, y1, y2):
        if (isinstance(x1, str) or isinstance(x2, str) or isinstance(y1, str) or isinstance(y2, str)):
            num1 = re.sub('[^0-9.-]','', x1)
            num2 = re.sub('[^0-9.-]','', x2)
            num3 = re.sub('[^0-9.-]','', y1)
            num4 = re.sub('[^0-9.-]','', y2)

            n1 = float(num1)
            n2 = float(num2)
            n3 = float(num3)
            n4 = float(num4)
            
            calc = math.sqrt(((n2 - n1)**2) + ((n4 - n3)**2))
            return units.length(calc)
        
        else:
            calc = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
            return units.length(calc)

    
    def change_in_distance(self, d1, d2):
        if (isinstance(d1, str) or isinstance(d2, str)):
            num1 = re.sub('[^0-9.-]','', d1)
            num2 = re.sub('[^0-9.-]','', d2)

            d1 = float(num1)
            d2 = float(num2)

            calc = (d2 - d1)
            return units.length(calc)
        
        else:
            calc = (d2 - d1)
            return units.length(calc)
    
    def change_in_time(self, t1, t2):
        if (isinstance(t1, str) or isinstance(t2, str)):
            num1 = re.sub('[^0-9.-]','', t1)
            num2 = re.sub('[^0-9.-]','', t2)

            t1 = float(num1)
            t2 = float(num2)

            calc = (t2 - t1)
            return units.length(calc)
        
        else:
            calc = (t2 - t1)
            return units.time(calc)
    
    def change_in_velocity(self, v1, v2):
        if (isinstance(v1, str) or isinstance(v2, str)):
            num1 = re.sub('[^0-9.-]','', v1)
            num2 = re.sub('[^0-9.-]','', v2)

            v1 = float(num1)
            v2 = float(num2)

            calc = (v2 - v1)
            return units.length(calc)
        
        else:
            calc = (v2 - v1)
            return units.velocity(calc)
    
    def average_velocity(self, d1, d2, t1, t2):
        change_in_distance = self.change_in_distance(d1, d2)
        change_in_time = self.change_in_time(t1, t2)

        num1 = re.sub('[^0-9.-]','', change_in_distance)
        num2 = re.sub('[^0-9.-]','', change_in_time)
        
        calc = float(num1) / float(num2)
        return units.velocity(calc)
    
    def average_acceleration(self, v1, v2, t1, t2):
        change_in_velocity = self.change_in_velocity(v1, v2)
        change_in_time = self.change_in_time(t1, t2)

        num1 = re.sub('[^0-9.-]','', change_in_velocity)
        num2 = re.sub('[^0-9.-]','', change_in_time)
        
        calc = float(num1) / float(num2)
        return units.acceleration(calc)
    
    def force_ma(self, a1, m1):
        if (isinstance(a1, str) and isinstance(m1, str)):
            num1 = re.sub('[^0-9.-]','', a1)
            num2 = re.sub('[^0-9.-]','', m1)
            calc = float(num1) * float(num2)
            return units.force(calc)

        elif (isinstance(a1, float) or isinstance(m1, str)):
            num1 = a1
            num2 = re.sub('[^0-9.-]','', m1)
            calc = float(num1) * float(num2)
            return units.force(calc)

        elif (isinstance(a1, str) or isinstance(m1, float)):
            num1 = re.sub('[^0-9.-]','', a1)
            num2 = m1
            calc = float(num1) * float(num2)
            return units.force(calc)
        
        else:
            calc = num1 * num2
            return units.force(calc)

    def force_mv2_r(self, v, m, r):
        if (isinstance(v, str) and isinstance(m, str) and isinstance(r, str)):
            num1 = re.sub('[^0-9.-]','', v)
            num2 = re.sub('[^0-9.-]','', m)
            num3 = re.sub('[^0-9.-]','', r)
            
            n1 = float(num1)
            n2 = float(num2)
            n3 = float(num3)
            
            calc = float(((n1**2) / n3) * n2)
            return units.force(calc)

        elif (isinstance(v, str) and isinstance(m, str) or isinstance(r, float)):
            num1 = re.sub('[^0-9.-]','', v)
            num2 = re.sub('[^0-9.-]','', m)
            num3 = r

            n1 = float(num1)
            n2 = float(num2)

            calc = float(((n1**2) / num3) * n2)
            return units.force(calc)

        elif (isinstance(v, str) and isinstance(r, str) or isinstance(m, float)):
            num1 = re.sub('[^0-9.-]','', v)
            num2 = m
            num3 = re.sub('[^0-9.-]','', r)

            n1 = float(num1)
            n3 = float(num3)
            
            calc = float(((n1**2) / n3) * num2)
            return units.force(calc)
        
        elif (isinstance(v, float) or isinstance(m, str) and isinstance(r, str)):
            num1 = v
            num2 = re.sub('[^0-9.-]','', m)
            num3 = re.sub('[^0-9.-]','', r)

            n2 = float(num2)
            n3 = float(num3)
            
            calc = float(((num1**2) / n3) * n2)
            return units.force(calc)
        
        elif (isinstance(v, str) or isinstance(m, float) and isinstance(r, float)):
            num1 = re.sub('[^0-9.-]','', v)
            num2 = m
            num3 = r

            n1 = float(num1)
            
            calc = float(((n1**2) / num3) * num2)
            return units.force(calc)
        
        elif (isinstance(v, float) and isinstance(r, float) or isinstance(m, str)):
            num1 = v
            num2 = re.sub('[^0-9.-]','', m)
            num3 = r

            n2 = float(num2)
            
            calc = float(((num1**2) / num3) * n2)
            return units.force(calc)
        
        elif (isinstance(v, float) and isinstance(m, float) or isinstance(r, str)):
            num1 = v
            num2 = m
            num3 = re.sub('[^0-9.-]','', r)

            n3 = float(num3)
            
            calc = float(((num1**2) / n3) * num2)
            return units.force(calc)
        
        else:
            num1 = v
            num2 = m
            num3 = r

            calc = float(((num1**2) / num3) * num2)
            return units.force(calc)
    
    def force_kqq_r2(self, q1, q2, r, k = constants.ke):
        if (isinstance(q1, str) and isinstance(q2, str) and isinstance(r, str)):
            num1 = k
            num2 = re.sub('[^0-9.-]','', q1)
            num3 = re.sub('[^0-9.-]','', q2)
            num4 = re.sub('[^0-9.-]','', r)

            n2 = float(num2)
            n3 = float(num3)
            n4 = float(num4)

            calc = (float(num1) * n2 * n3) / (n4**2)
            return units.force(calc)

        elif (isinstance(q1, str) or isinstance(q2, str) or isinstance(r, float)):
            num1 = k
            num2 = re.sub('[^0-9.-]','', q1)
            num3 = re.sub('[^0-9.-]','', q2)
            num4 = r

            n2 = float(num2)
            n3 = float(num3)

            calc = (float(num1) * n2 * n3) / float(num4**2)
            return units.force(calc)

        elif (isinstance(q1, float) or isinstance(q2, float) or isinstance(r, str)):
            num1 = k
            num2 = q1
            num3 = q2
            num4 = re.sub('[^0-9.-]','', r)

            n4 = float(num4)

            calc = float(num1 * num2 * num3) / (n4**2)
            return units.force(calc)

        else:
            num1 = k
            num2 = q1
            num3 = q2
            num4 = r

            calc = float(num1 * num2 * num3) / float(num4**2)
            return units.force(calc)
    
    def force_GMm_r2(self, M, m, r, G = constants.G):
        if (isinstance(M, str) or isinstance(m, str) or isinstance(r, str)):
            num1 = G
            num2 = re.sub('[^0-9.-]','', M)
            num3 = re.sub('[^0-9.-]','', m)
            num4 = re.sub('[^0-9.-]','', r)

            n2 = float(num2)
            n3 = float(num3)
            n4 = float(num4)


            calc = (float(num1) * n2 * n3) / (n4**2)
            return units.force(calc)


        elif (isinstance(M, str) or isinstance(m, str) or isinstance(r, float)):
            num1 = G
            num2 = re.sub('[^0-9.-]','', M)
            num3 = re.sub('[^0-9.-]','', m)
            num4 = r

            n2 = float(num2)
            n3 = float(num3)

            calc = (float(num1) * n2 * n3) / float(num4**2)
            return units.force(calc)

        elif (isinstance(M, float) or isinstance(m, float) or isinstance(r, str)):
            num1 = G
            num2 = M
            num3 = m
            num4 = re.sub('[^0-9.-]','', r)

            n4 = float(num4)

            calc = float(num1 * num2 * num3) / (n4**2)
            return units.force(calc)

        else:
            num1 = G
            num2 = M
            num3 = m
            num4 = r

            calc = float(num1 * num2 * num3) / float(num4**2)
            return units.force(calc)
