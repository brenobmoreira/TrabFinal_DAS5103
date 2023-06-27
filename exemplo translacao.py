import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Dinâmica do motor

def f1(ia, t, L, Ea, Kv, w, Ra): # derivada da corrente
    return (Ea - Kv * w - Ra * ia) / L

def f2(w, t, J, Kt, ia, b): # derivada da velocidade angular
    return (Kt * ia - b * w) / J

# Dinâmica da translação

def f3(V, t, Kt, ia, r, c, m, g, alpha): # derivada da velocidade
    return (Kt * ia / r - c * V - m * g * np.sin(alpha)) / m

# Parametrização do sistema

L = 0.0005 # indutância
Kv = 0.01 # constante de velocidade
Ra = 0.1 # resistência de armadura

J = 0.0001 # inércia
Kt = 0.01 # constante de torque
b = 0.01 # coeficiente de atrito viscoso

r = 0.01 # raio da roda
c = 5 # coeficiente de atrito viscoso
m = 0.1 # massa
g = 9.8 # aceleração da gravidade

Ea = 1 # tensão de armadura
alpha = 0 # ângulo de inclinação

# Resolvendo as EDOs da dinâmica do motor
def main():
    ia0 = 0 # condição inicial da corrente
    w0 = 0 # condição inicial da velocidade angular
    v0 = 0 # condição inicial da velocidade
    t = np.linspace(0, 0.15, 30) # vetor de tempo
    ia = odeint(f1, ia0, t, args=(L, Ea, Kv, w0, Ra)) # corrente
    w = odeint(f2, w0, t, args=(J, Kv, ia[-1], b)) # velocidade angular
    v = odeint(f3, v0, t, args=(Kt, ia[-1], r, c, m, g, alpha)) # velocidade

    # visualização dos resultados

    plt.figure(1)
    plt.plot(t, ia, 'r-', linewidth=2, label='corrente')
    plt.plot(t, w, 'b--', linewidth=2, label='velocidade angular')
    plt.plot(t, v, 'g:', linewidth=2, label='velocidade')
    plt.xlabel('tempo (s)')
    plt.ylabel('corrente (A), velocidade angular (rad/s), velocidade (m/s)')
    plt.legend(loc='best')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()