calendar = [[0 for hour in range(24)] for day in range(7)]

print(calendar)

# Merkitään maanantai klo 10 varatuksi
calendar[0][0] = 1

print(calendar[0][10])  # 1 (varattu)