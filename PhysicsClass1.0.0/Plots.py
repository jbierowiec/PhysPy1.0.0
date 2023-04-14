from Formulas import Formulas
import matplotlib.pyplot as plt
import math

formulas = Formulas()

class Plots:
    def plot_distance(self, x1, x2, y1, y2, xmin, xmax, ymin, ymax):
        calc = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

        fig, ax = plt.subplots()
        ax.plot(x1, y1, 'ro')
        ax.plot(x2, y2, 'go')
        ax.plot([x1, x2], [y1, y2], 'b-')

        ax.text(x1+0.1, y1+0.1, '({}, {})'.format(x1, y1), fontsize=10)
        ax.text(x2+0.1, y2+0.1, '({}, {})'.format(x2, y2), fontsize=10)
        ax.text(10, 10, 'Distance: {:.2f}'.format(calc), fontsize=12)

        ax.set_title('Distance between two points')
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ax.grid(True)

        return plt.show()
    
    def change_in_distance(self, d1, d2, xmin, xmax, ymin, ymax):
        calc = (d2 - d1)

        x = [d1, d2]
        y = [0, 0]

        fig, ax = plt.subplots()

        ax.plot(x, y)
        ax.scatter(x, y, color='red')

        ax.text(d1+0.1, 0+0.1, '({}, {})'.format(d1, 0), fontsize=10)
        ax.text(d2+0.1, 0+0.1, '({}, {})'.format(d2, 0), fontsize=10)
        ax.text(10, 10, 'Change in distance: {:.2f}'.format(calc), fontsize=12)

        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_title('Change in distance')

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ax.grid(True)

        return plt.show()
    
    def change_in_time(self, t1, t2, xmin, xmax, ymin, ymax):
        calc = (t2 - t1)

        x = [t1, t2]
        y = [0, 0]

        fig, ax = plt.subplots()

        ax.plot(x, y)
        ax.scatter(x, y, color='red')

        ax.text(t1+0.1, 0+0.1, '({}, {})'.format(t1, 0), fontsize=10)
        ax.text(t2+0.1, 0+0.1, '({}, {})'.format(t2, 0), fontsize=10)
        ax.text(10, 10, 'Change in time: {:.2f}'.format(calc), fontsize=12)

        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_title('Change in time')

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ax.grid(True)

        return plt.show()
    
    def change_in_velocity(self, v1, v2, xmin, xmax, ymin, ymax):
        calc = (v2 - v1)

        x = [v1, v2]
        y = [0, 0]

        fig, ax = plt.subplots()

        ax.plot(x, y)
        ax.scatter(x, y, color='red')

        ax.text(v1+0.1, 0+0.1, '({}, {})'.format(v1, 0), fontsize=10)
        ax.text(v2+0.1, 0+0.1, '({}, {})'.format(v2, 0), fontsize=10)
        ax.text(10, 10, 'Change in velocity: {:.2f}'.format(calc), fontsize=12)

        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_title('Change in velocity')

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ax.grid(True)

        return plt.show()
    
    def plot_average_velocity(self, d1, d2, t1, t2, xmin, xmax, ymin, ymax):
        v_avg = (d2 - d1) / (t2 - t1)

        fig, ax = plt.subplots()

        ax.plot([t1, t2], [d1, d2], 'ro-')

        ax.text(t1+0.1, d1+0.1, '({}, {})'.format(t1, d1), fontsize=10)
        ax.text(t2+0.1, d2+0.1, '({}, {})'.format(t2, d2), fontsize=10)
        ax.text(10, 10, 'Average velocity: {:.2f}'.format(v_avg) + 'm/s', fontsize=12)

        ax.set_title('Average velocity')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Distance (m)')

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ax.grid(True)

        return plt.show()
    
    def plot_average_acceleration(self, v1, v2, t1, t2, xmin, xmax, ymin, ymax):
        v_avg = (v2 - v1) / (t2 - t1)

        fig, ax = plt.subplots()

        ax.plot([t1, t2], [v1, v2], 'ro-')

        ax.text(t1+0.1, v1+0.1, '({}, {})'.format(t1, v1), fontsize=10)
        ax.text(t2+0.1, v2+0.1, '({}, {})'.format(t2, v2), fontsize=10)
        ax.text(10, 10, 'Average acceleration: {:.2f}'.format(v_avg) + 'm/s^{2}', fontsize=12)

        ax.set_title('Average acceleration')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Velocity (m/s)')

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ax.grid(True)

        return plt.show()
