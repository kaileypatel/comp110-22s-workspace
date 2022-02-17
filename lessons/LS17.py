
print("for..in output:")
ys: list[int] = [110, 120]
for y in ys:
    print(y)    

print("while loop output:")
i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
    y: int = ys[i] 
    print(y)
    i += 1