import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import sweep_poly


class Generator:
    def __init__(self, A, f, t0, tn):
        self.A = A
        self.f = f
        self.t = np.linspace(t0, tn, f * tn * 100)
        self.sin = A * np.sin(2 * np.pi * f * self.t)
        self.square = A * signal.square(2 * np.pi * f * self.t)
        self.triangle = A * signal.sawtooth(2 * np.pi * f * self.t, 0.5)
        self.noise = (np.random.random_sample((len(self.t))) - .5) * .2
    def sinus(self):

        plt.plot(self.t, self.sin)

        plt.title('Sinus')
        plt.xlabel('t[s]')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()

    def kwadrat(self):

        plt.plot(self.t, self.square)

        plt.title('Sygnał kwadratowy')
        plt.xlabel('t[s]')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()

    def pwm(self, PWM):
        pwm = self.A * signal.square(2 * np.pi * self.f * self.t, duty=PWM * 0.01)
        plt.plot(self.t, pwm)

        plt.title('PWM')
        plt.xlabel('t[s]')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()

    def trojkat(self):
        plt.plot(self.t, self.triangle)

        plt.title('Triangle')
        plt.xlabel('t[s]')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()

    def szum(self):


        plt.plot(self.t, self.noise)

        plt.title('Szum')
        plt.xlabel('t[s]')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()

    def sweep(self, p1, p2, p3, p4, p5):

        p = np.poly1d([p1, p2, p3, p4, p5])
        sweep = sweep_poly(self.t, p)
        plt.plot(self.t, sweep)

        plt.title('Sweep Poly')
        plt.xlabel('t[s]')
        plt.ylabel('Amplituda')
        plt.grid(True)
        plt.show()