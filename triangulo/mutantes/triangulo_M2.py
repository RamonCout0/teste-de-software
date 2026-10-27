def classifica(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b and a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(classifica(a, b, c))
