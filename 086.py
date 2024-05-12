triplets = []
for x in range (1,1000):
    for y in range (x+1,1000):
        for z in range(y+1, 1000):
            if x**2 + y**2 == z**2:
                triplets.append(tuple((x,y,z)))
                if x + y + z == 1000:
                    print(f"{x}, {y} y {z} son un triple pitagórico cuya suma da 1000")
print(f"Hay {len(triplets)} triples pitágoricos.")
for i in range(16):
    print(triplets[i])