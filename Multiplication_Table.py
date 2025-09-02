size = 10

print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print()

print("    " + "----" * size)


for i in range(1, size + 1):
    print(f"{i:3} |", end="")  
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print()