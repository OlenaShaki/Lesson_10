import sys
def month_name(n):
    months = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень', 9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}

#Ділянка коду, де можуть виникнути виключення
    try:
        n = int(n)
        if n in months:
            return months[n]
# Ділянка з кодом, де описується реакцію на відоме виключення
# Ввели тексет:
    except ValueError as ex:
        print(ex, file=sys.stderr)
        print("Ви ввели некоректний символ", file=sys.stderr)

# Ввели не дійсне значення більше 12, або >=0
    except KeyError as ex:
        print(ex, file=sys.stderr)
        print("Ви ввели не дійсне значення більше 12, або >=0", file=sys.stderr)


print(month_name(3))
print(month_name(13))
print(month_name("3"))
print(month_name("уке"))
print("ПРОГРАМА ЗАКІНЧИЛА РОБОТУ!")