import sys
def unic(n):
# Ділянка коду, де можуть виникнути виключення
    try:
        for i in n:
            if type (i) != int:
                raise ValueError
# Ділянка з кодом, де описується реакцію на відоме виключення
# Ввели тексет:
    except TypeError as ex:
        print(ex, file=sys.stderr)
        print("Ви ввели меньше 2-х символів", file=sys.stderr)
        return
    except ValueError as ex:
        print(ex, file=sys.stderr)
        print("Ви ввели некоректний символ", file=sys.stderr)
        return

    if len(n) == len(set(n)):
        return True
    else:
        return False

#print(unic([1,2,3,4,5, "6"]))

print(unic([1, 2, "3"]))
