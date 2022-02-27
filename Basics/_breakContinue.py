ages = [18,21,35,46,78]

#break
print("---BREAK---")
for age in ages:
    if age == 35:
        break
    print(age)

#continue
print("---CONTINUE---")
for age in ages:
    if age == 21:
        continue
    print(age)