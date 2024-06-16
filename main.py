import numpy as np
import matplotlib.pyplot as plt

# Definições iniciais
dt = 0.1  # Intervalo de tempo
total_time = 20  # Tempo total da simulação
steps = int(total_time / dt)  # Número de passos na simulação

# Condições iniciais
x, y, theta = 0, 0, 0  # Posições iniciais
linear_velocity = 1  # Velocidade linear inicial
angular_velocity = 0.1  # Velocidade angular inicial
acceleration = 0.05  # Aceleração

# Arrays para armazenar os dados da trajetória
x_data, y_data = [x], [y]

# Loop de simulação
for step in range(steps):
    # Atualiza as velocidades com a aceleração
    linear_velocity += acceleration * dt
    angular_velocity += acceleration * dt
    
    # Calcula a nova posição
    x += linear_velocity * np.cos(theta) * dt
    y += linear_velocity * np.sin(theta) * dt
    theta += angular_velocity * dt
    
    # Armazena os dados
    x_data.append(x)
    y_data.append(y)

# Visualização da trajetória
plt.figure()
plt.plot(x_data, y_data, label="Trajetória")
plt.title("Simulação de Movimento Robótico")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
