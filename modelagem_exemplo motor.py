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
b = 0.0001 # coeficiente de atrito viscoso

r = 0.01 # raio da roda
c = 0.0001 # coeficiente de atrito viscoso
m = 0.1 # massa
g = 9.8 # aceleração da gravidade

Ea = 10 # tensão de armadura
V = 0 # velocidade
alpha = 0 # ângulo de inclinação

# Resolvendo as EDOs da dinâmica do motor
def main():
    ia0 = 0 # condição inicial da corrente
    w0 = 0 # condição inicial da velocidade angular
    t = np.linspace(0, 0.15, 30) # vetor de tempo
    ia_zero = odeint(f1, ia0, t, args=(L, 0, Kv, w0, Ra)) # corrente para tensão de armadura igual a 0
    ia5 = odeint(f1, ia0, t, args=(L, 5, Kv, w0, Ra)) # corrente para tensão de armadura igual a 5
    ia10 = odeint(f1, ia0, t, args=(L, 10, Kv, w0, Ra)) # corrente para tensão de armadura igual a 10
    w_zero = odeint(f2, w0, t, args=(J, Kv, ia_zero[-1], b)) # velocidade angular para tensão de armadura igual a 0
    w5 = odeint(f2, w0, t, args=(J, Kv, ia5[-1], b)) # velocidade angular para tensão de armadura igual a 5
    w10 = odeint(f2, w0, t, args=(J, Kv, ia10[-1], b)) # velocidade angular para tensão de armadura igual a 10

    # visualização dos resultados

    plt.figure(1)
    plt.plot(t, ia_zero, 'r-', linewidth=2, label='corrente')
    plt.plot(t, w_zero, 'b--', linewidth=2, label='velocidade angular')
    plt.xlabel('tempo (s)')
    plt.ylabel('corrente (A) / velocidade angular (rad/s)')
    plt.title('Resposta do motor para tensão de armadura igual a 0')
    plt.legend()
    plt.grid()

    plt.figure(2)
    plt.plot(t, ia5, 'r-', linewidth=2, label='corrente')
    plt.plot(t, w5, 'b--', linewidth=2, label='velocidade angular')
    plt.xlabel('tempo (s)')
    plt.ylabel('corrente (A) / velocidade angular (rad/s)')
    plt.title('Resposta do motor para tensão de armadura igual a 5')
    plt.legend()
    plt.grid()
    
    plt.figure(3)
    plt.plot(t, ia10, 'r-', linewidth=2, label='corrente')
    plt.plot(t, w10, 'b--', linewidth=2, label='velocidade angular')
    plt.xlabel('tempo (s)')
    plt.ylabel('corrente (A) / velocidade angular (rad/s)')
    plt.title('Resposta do motor para tensão de armadura igual a 10')
    plt.legend()
    plt.grid()

    plt.show()

if __name__ == '__main__':
    main()