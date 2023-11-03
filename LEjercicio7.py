abc = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

abecedario_G = []

for i in range(len(abc)):
    if (i + 1) % 3 != 0:
        abecedario_G.append(abc[i])
        

print(abecedario_G)


