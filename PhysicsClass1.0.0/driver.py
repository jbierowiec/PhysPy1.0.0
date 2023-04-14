from Formulas import Formulas
from Magnitude import Magnitude
from Units import Units
from Plots import Plots

formulas = Formulas()
magnitude = Magnitude()
units  = Units()
plots = Plots()


# limit points
xmin = -30
ymin = -30
xmax = 30
ymax = 30

# points
x1 = 10
x2 = 30
y1 = 20
y2 = 0

# distance
d1 = 2
d2 = 18
r = 100

# time
t1 = 0
t2 = 10

# velocity 
v1 = 3.2
v2 = 25.7

# mass
m2 = 10000000
m1 = 5000

# charges
q1 = 8
q2 = -10

# formulas and plots
dist = formulas.distance(x1, x2, y1, y2)
dist2 = formulas.change_in_distance(d1, d2)
plotdist2 = plots.change_in_distance(d1, d2, xmin, xmax, ymin, ymax)
plotdist = plots.plot_distance(x1, x2, y1, y2, xmin, xmax, ymin, ymax)

vel = formulas.average_velocity(d1, d2, t1, t2)
plotvel = plots.plot_average_velocity(d1, d2, t1, t2, xmin, xmax, ymin, ymax)

acc = formulas.average_acceleration(v1, v2, t1, t2)
plotacc =plots.plot_average_acceleration(v1, v2, t1, t2, xmin, xmax, ymin, ymax)

force1 = formulas.force_ma(acc, m1)
force2 = formulas.force_kqq_r2(q1, q2, r)
force3 = formulas.force_GMm_r2(m1, m2, r)

# mass units
mass = units.mass(m1)

# magnitude unit conversions
v = magnitude.convert(vel)
a = magnitude.convert(acc)
F = magnitude.convert(force1)
Fe = magnitude.convert(force2)
Fg = magnitude.convert(force3)

# print statements
print('The distance is: ' + dist)
print('The average velocity of is: ' + v)
print('The average acceleration is: ' + a)
print('The force is: ' + F)
print('The mass is: ' + mass)
print('The electrostatic force is: ' + Fe)
print(force3)
print('The gravitational force is: ' + Fg)
