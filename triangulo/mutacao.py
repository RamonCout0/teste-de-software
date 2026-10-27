"""Gera mutantes de triangulo.py e roda uma suíte de testes contra cada um.

Uso: python mutacao.py [arquivo_de_testes]   (padrão: tests.py)
Um mutante é MORTO se a suíte reporta falha (Triangle tests passed: n/m com n < m,
ou código de saída diferente de zero).
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGINAL = open(os.path.join(AQUI, 'triangulo.py'), encoding='utf-8').read()

MUTANTES = [
    ('M1', 'a == b == c', 'a != b == c', 'relacional: == -> != no equilátero'),
    ('M2', 'a == b or a == c or b == c', 'a == b and a == c or b == c', 'lógico: 1º or -> and'),
    ('M3', ' or b == c', '', 'remoção da condição b == c'),
    ('M4', 'a == b or', 'a <= b or', 'relacional: a == b -> a <= b'),
    ('M5', 'return "Isósceles"', 'return "Escaleno"', 'constante: rótulo do isósceles'),
    ('M6', 'elif a == b', 'if a == b', 'estrutura: elif -> if'),
    ('M7', 'a == b == c', 'a == b', 'remoção da condição b == c no equilátero'),
    ('M8', 'a == c or', 'a != c or', 'relacional: a == c -> a != c'),
]


def roda(testes, codigo):
    with tempfile.TemporaryDirectory() as d:
        shutil.copy(testes, os.path.join(d, 'tests.py'))
        with open(os.path.join(d, 'triangulo.py'), 'w', encoding='utf-8') as f:
            f.write(codigo)
        p = subprocess.run([sys.executable, os.path.join(d, 'tests.py')],
                           capture_output=True, text=True, cwd=d)
    m = re.search(r'Triangle tests passed: (\d+)/(\d+)', p.stdout)
    falhou = p.returncode != 0 or not m or m.group(1) != m.group(2)
    return falhou


def main():
    testes = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, 'tests.py'))
    if roda(testes, ORIGINAL):
        sys.exit('A suíte falha no código original; corrija antes de mutar.')
    os.makedirs(os.path.join(AQUI, 'mutantes'), exist_ok=True)
    mortos = 0
    for nome, velho, novo, desc in MUTANTES:
        assert velho in ORIGINAL, nome
        codigo = ORIGINAL.replace(velho, novo, 1)
        with open(os.path.join(AQUI, 'mutantes', f'triangulo_{nome}.py'), 'w', encoding='utf-8') as f:
            f.write(codigo)
        morto = roda(testes, codigo)
        mortos += morto
        print(f'{nome}  {"MORTO     " if morto else "SOBREVIVEU"}  {desc}')
    print(f'\nMutation score: {mortos}/{len(MUTANTES)} = {100 * mortos / len(MUTANTES):.0f}%')


if __name__ == '__main__':
    main()
