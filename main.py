from limite import verify_limite, result


def f(x: float) -> float:
    """
    f(x) = eq
    """
    return 2 * x + 3


# Definições do ponto, limite e precisão
a = 1
L = 5
epsilon = 0.01

# Chamada da função de verificação de limite
direita_x, esquerda_x = verify_limite(f, a, L, epsilon)

# Exibição dos resultados
print("Resultados à esquerda de a:")
result(esquerda_x, f) if len(esquerda_x) > 0 else print("Não há valores para '\
                                                        'esse limite.")
print("\nResultados à direita de a:")
result(direita_x, f) if len(direita_x) > 0 else print("Não há valores para '\
                                                        'esse limite.")
