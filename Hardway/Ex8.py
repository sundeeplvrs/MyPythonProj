formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One","Two","Three","Four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Let me try",
    "Writing something",
    "That comes",
    "on my mind"
))
print(formatter.format(1+2, 2+3, 3+4, 4+5))