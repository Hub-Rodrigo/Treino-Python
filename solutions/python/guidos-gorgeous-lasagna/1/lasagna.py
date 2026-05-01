# Constantes
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # minutos por camada


def bake_time_remaining(elapsed_bake_time):
    """Calcula o tempo restante de forno.

    :param elapsed_bake_time: int - tempo já passado no forno.
    :return: int - tempo restante (em minutos).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calcula o tempo de preparo com base no número de camadas.

    :param number_of_layers: int - número de camadas da lasanha.
    :return: int - tempo total de preparo (em minutos).
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula o tempo total já gasto (preparo + forno).

    :param number_of_layers: int
    :param elapsed_bake_time: int
    :return: int - tempo total decorrido
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time