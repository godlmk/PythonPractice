import math
dayfactor = 0.01
dayup = math .pow((1.0 + dayfactor), 365)
daydow = math.pow((1.0 - dayfactor), 365)
print("向上：{:.2f},向下：{:.2f}.".format(dayup, daydow))
