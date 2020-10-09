ability = 1
j = 0
for i in range(365):
    if (i % 10) == 0:
        j = 0
    if j >= 3:
        j += 1
        ability = ability * 1.01
print("365天后的能力值:", format(ability))
