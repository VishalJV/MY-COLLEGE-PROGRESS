print("   N     N^2     N^3     Square root N")
for i in range(1,16):
    print(f"{i:>4}",end="   ")
    print(f"{i**2:>4}",end="   ")
    print(f"{i**3:>4}",end="   ")
    print(f"{i**0.5:.4f}",end="   ")
    print(" ")