import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Continua criando novos passeios enquanto o programa estiver ativo
while True:
    # Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)

    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c='green', edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=75, zorder=2)

    # Remove os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Continuar a caminhada:  (y/n):")
    if keep_running == 'n':
        break