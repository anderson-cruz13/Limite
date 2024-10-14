from typing import Callable, List, Tuple


def verify_limite(
        y: Callable[[float], float],
        a: float, L: float, epsilon: float) -> Tuple[List[str], List[str]]:
    """
    Verifica se a função y tem limite L no ponto a, com uma precisão epsilon.

    y: Função a ser calculada
    a: Ponto para calcular o limite
    L: Limite a ser verificado
    epsilon: Critério para a verificação
    """

    direita_x = []  # Valores de x à direita de a
    esquerda_x = []  # Valores de x à esquerda de a

    # Define um delta pequeno relacionado ao epsilon
    delta = epsilon / 2

    def condition_limit(x: float) -> bool:
        """
        Verifica se a condição do limite para a função y no ponto x é TRUE.
        """
        # 0 < ∣ x−a ∣ < δ e ∣ y(x)-L ∣ < ε
        return 0 < abs(x - a) < delta and abs(y(x) - L) < epsilon

    # Verifica valores à direita de a
    for i in range(1, 11):
        x1 = a + delta / i
        if condition_limit(x1):
            direita_x.append(f"{x1:.5f}")

    # Verifica valores à esquerda de a
    for i in range(1, 11):
        x2 = a - delta / i
        if condition_limit(x2):
            esquerda_x.append(f"{x2:.5f}")

    return direita_x, esquerda_x


def result(numbers: List[str], y: Callable[[float], float]) -> None:
    """
    Imprime os valores de x e suas respectivas saídas da função y.

    numbers: Lista de números a serem avaliados
    y: Função a ser avaliada
    """
    for number in numbers:
        f = y(float(number))
        print(f"x = {number} y = {f:.5f}")
