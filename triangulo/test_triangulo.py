import pytest

from triangulo import classifica


@pytest.mark.parametrize("lados, esperado", [
    ((0, 0, 0), "Equilátero"),
    ((100, 100, 100), "Equilátero"),
    ((0, 0, 1), "Isósceles"),
    ((0, 1, 0), "Isósceles"),
    ((1, 0, 0), "Isósceles"),
    ((1, 1, 2), "Isósceles"),
    ((99, 100, 100), "Isósceles"),
    ((0, 1, 1), "Isósceles"),
    ((1, 0, 1), "Isósceles"),
    ((2, 1, 1), "Isósceles"),
    ((1, 2, 1), "Isósceles"),
    ((1, 1, 0), "Isósceles"),
    ((1, 2, 3), "Escaleno"),
    ((99, 100, 101), "Escaleno"),
])
def test_classifica(lados, esperado):
    assert classifica(*lados) == esperado
