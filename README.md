# Simulação de Movimento Robótico

Este projeto tem como objetivo aplicar conceitos de cinemática de robôs móveis, simulando o movimento de um robô em um ambiente virtual. A simulação leva em conta a influência da velocidade linear, velocidade angular e aceleração no deslocamento do robô.

## Descrição

A partir dos conhecimentos adquiridos em sala de aula, este projeto visa calcular a posição final do robô no sistema de coordenadas global após um intervalo de tempo especificado, utilizando as velocidades linear e angular fornecidas pelo usuário. Além disso, inclui uma representação gráfica da trajetória do robô, mostrando ponto a ponto o caminho percorrido durante o período de movimento.

## Equações Utilizadas

A cinemática do robô é descrita pelas seguintes equações:

- \( \Delta x = v \cdot \cos(\theta) \cdot \Delta t \)
- \( \Delta y = v \cdot \sin(\theta) \cdot \Delta t \)
- \( \Delta \theta = \omega \cdot \Delta t \)

Onde:
- \( \Delta x, \Delta y \) são as mudanças nas coordenadas x e y.
- \( \theta \) é o ângulo de orientação do robô.
- \( \Delta t \) é o intervalo de tempo.

## Implementação

A implementação do código foi realizada em Python utilizando as bibliotecas `numpy` para cálculos matemáticos e `matplotlib` para a visualização gráfica.
