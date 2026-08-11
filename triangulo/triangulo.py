a = int(input())
b = int(input())
c = int(input())

if( a == b == c):
    print("Equilátero")
elif (a == b or a == c or b == c):
        print("Isósceles")
else:
        print("Escaleno")