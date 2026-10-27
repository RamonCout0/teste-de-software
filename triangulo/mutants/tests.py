import subprocess
import sys
import os


def run_triangulo(a, b, c):
    script_dir = os.path.dirname(__file__)
    script_path = os.path.join(script_dir, 'triangulo.py')
    proc = subprocess.run([sys.executable, script_path], input=f"{a}\n{b}\n{c}\n", text=True, capture_output=True)
    return proc.stdout.strip()


def test_triangulo_cases():
    
    cases = [
        ((0, 0, 0), 'Equilátero'),
        ((0, 0, 1), 'Isósceles'),
        ((0, 1, 0), 'Isósceles'),
        ((1, 0, 0), 'Isósceles'),
        ((1, 1, 2), 'Isósceles'),
        ((1, 2, 3), 'Escaleno'),
        ((100, 100, 100), 'Equilátero'),
        ((99, 100, 100), 'Isósceles'),
        ((99, 100, 101), 'Escaleno'),
        ((0, 1, 1), 'Isósceles'),
        ((1, 0, 1), 'Isósceles'),
        ((2, 1, 1), 'Isósceles'),
        ((1, 2, 1), 'Isósceles'),
        ((1, 1, 0), 'Isósceles'),
    ]

    passed = 0
    for inp, expected in cases:
        out = run_triangulo(*inp)
        ok = expected == out
        status = 'PASS' if ok else 'FAIL'
        print(f"triangulo{inp} -> expected: {expected!r}, got: {out!r} => {status}")
        if ok:
            passed += 1

    print(f"\nTriangle tests passed: {passed}/{len(cases)}")
    return passed == len(cases)


def discount_percentage(age: int) -> float:
    if age < 0 or age > 24:
        raise ValueError('idade fora do intervalo [0..24]')
    if age <= 12:
        return 15.0
    if 13 <= age <= 18:
        return 12.0
    if 19 <= age <= 21:
        return 5.0
    return 3.0


def test_discount_cases():
   
    cases = [
        (-1, None),  # invalid
        (0, 15.0),
        (1, 15.0),
        (12, 15.0),
        (13, 12.0),
        (18, 12.0),
        (19, 5.0),
        (21, 5.0),
        (22, 3.0),
        (24, 3.0),
        (25, None),  # invalid
    ]

    passed = 0
    for age, expected in cases:
        try:
            got = discount_percentage(age)
            ok = (expected is not None and got == expected)
            status = 'PASS' if ok else 'FAIL'
            print(f"age={age} -> expected: {expected}, got: {got} => {status}")
            if ok:
                passed += 1
        except Exception as e:
            ok = (expected is None)
            status = 'PASS' if ok else 'FAIL'
            print(f"age={age} -> expected: {expected}, got exception: {e} => {status}")
            if ok:
                passed += 1

    print(f"\nDiscount tests passed: {passed}/{len(cases)}")


if __name__ == '__main__':
    print('Running triangle tests...')
    triangulo_ok = test_triangulo_cases()
    print('\nRunning discount tests...')
    test_discount_cases()
    sys.exit(0 if triangulo_ok else 1)
