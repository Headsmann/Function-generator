from generator import *


def main():
    #RYSOWANIE SINUSA (AMPLITUDA, CZESTOTLIWOSC, T, Tn)
    sin = Generator(3, 2, 4, 1)
    sin.sinus()

    #RYSOWANIE KWADRATU (AMPLITUDA, CZESTOTLIWOSC, T, Tn)
    kwadr = Generator(3, 2, 4, 1)
    kwadr.kwadrat()

    #RYSOWANIE PWM (AMPLITUDA, CZESTOTLIWOSC, T, Tn)
    pwmm = Generator(3, 1, 0, 2)
    #(PWM)
    pwmm.pwm(65)

    #RYSOWANIE SYGNALU TROJKATNEGO (AMPLITUDA, CZESTOTLIWOSC, T, Tn)
    troj = Generator(3, 3, 0, 1)
    troj.trojkat()

    #NOISE (AMPLITUDA(ZAWSZE = 0), CZESTOTLIWOSC, T, Tn)
    noi = Generator(0, 2, 0, 1)
    noi.szum()

    #SWEEP (AMPLITUDA(ZAWSZE = 0), CZESTOTLIWOSC, T, Tn)
    sweep1 = Generator(0, 4, 0, 4)
    #Podajemy p1, p2, p3, p4, p5
    sweep1.sweep(2, 1, 0, 4, 3)


main()