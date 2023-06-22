import numpy as np

# Dinâmica do motor

def f1(L, Ea, Kv, w, Ra, ia): # derivada da corrente
    return (Ea - Kv * w - Ra * ia) / L

def f2(J, Kt, ia, b, w): # derivada da velocidade angular
    return (Kt * ia - b * w) / J

# Dinâmica da translação

def f3(Kt, ia, r, c, V, m, g, alpha):
    return (Kt * ia / r - c * V - m * g * np.sin(alpha)) / m

# Parametrização do sistema

L = 0.0005 # indutância
Ea = 0 # tensão de armadura
Kv = 0.01 # constante de velocidade
Ra = 0.1 # resistência de armadura
J = 0.0001 # inércia
Kt = 0.01 # constante de torque
b = 0.0001 # coeficiente de atrito viscoso
r = 0.01 # raio da roda
c = 0.0001 # coeficiente de atrito viscoso
V = 0 # velocidade
m = 0.1 # massa
g = 9.8 # aceleração da gravidade
alpha = 0 # ângulo de inclinação

# Condições iniciais

ia0 = 0 # corrente inicial
w0 = 0 # velocidade angular inicial
V0 = 0 # velocidade inicial
x0 = 0 # posição inicial

# Parâmetros de simulação

t0 = 0 # tempo inicial
tf = 10 # tempo final
dt = 0.01 # passo de integração

# Vetores de tempo e estado

t = np.arange(t0, tf, dt)
ia = np.zeros(len(t))
w = np.zeros(len(t))
V = np.zeros(len(t))
x = np.zeros(len(t))

# Condições iniciais

ia[0] = ia0
w[0] = w0
V[0] = V0
x[0] = x0

# Dada uma referência, o objetivo é controlar a velocidade V do motor. Ea é a tensão imposta pelo controlador.

V_ref = 1 # velocidade de referência

# Controlador

Kp = 1 # ganho proporcional
Ki = 1 # ganho integral
Kd = 1 # ganho derivativo

# Parâmetros do controlador

e = np.zeros(len(t)) # erro
e[0] = V_ref - V[0] # erro inicial
E = np.zeros(len(t)) # erro acumulado
E[0] = e[0] * dt # erro acumulado inicial
de = np.zeros(len(t)) # derivada do erro
de[0] = 0 # derivada do erro inicial

# Simulação

for i in range(len(t) - 1):
    