

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classifica__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_classifica__mutmut)
def classifica(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_orig(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_1(a, b, c):
    if a != b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_2(a, b, c):
    if a == b != c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_3(a, b, c):
    if a == b == c:
        return "XXEquiláteroXX"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_4(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_5(a, b, c):
    if a == b == c:
        return "EQUILÁTERO"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_6(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c and b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_7(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b and a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_8(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a != b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_9(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a != c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_10(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b != c:
        return "Isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_11(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "XXIsóscelesXX"
    else:
        return "Escaleno"
def x_classifica__mutmut_12(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "isósceles"
    else:
        return "Escaleno"
def x_classifica__mutmut_13(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "ISÓSCELES"
    else:
        return "Escaleno"
def x_classifica__mutmut_14(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "XXEscalenoXX"
def x_classifica__mutmut_15(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "escaleno"
def x_classifica__mutmut_16(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "ESCALENO"

mutants_x_classifica__mutmut['_mutmut_orig'] = x_classifica__mutmut_orig # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_1'] = x_classifica__mutmut_1 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_2'] = x_classifica__mutmut_2 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_3'] = x_classifica__mutmut_3 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_4'] = x_classifica__mutmut_4 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_5'] = x_classifica__mutmut_5 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_6'] = x_classifica__mutmut_6 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_7'] = x_classifica__mutmut_7 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_8'] = x_classifica__mutmut_8 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_9'] = x_classifica__mutmut_9 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_10'] = x_classifica__mutmut_10 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_11'] = x_classifica__mutmut_11 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_12'] = x_classifica__mutmut_12 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_13'] = x_classifica__mutmut_13 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_14'] = x_classifica__mutmut_14 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_15'] = x_classifica__mutmut_15 # type: ignore # mutmut generated
mutants_x_classifica__mutmut['x_classifica__mutmut_16'] = x_classifica__mutmut_16 # type: ignore # mutmut generated


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(classifica(a, b, c))
