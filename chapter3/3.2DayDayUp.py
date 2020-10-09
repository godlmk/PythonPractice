ability = 1
for i in range(365):
    j = i % 7
    if j >= 3:
        ability = ability * 1.01
print("365天后的能力值:", format(ability))