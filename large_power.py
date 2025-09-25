print("Testing large power greater than 5000")
print()

def large_power(base, expotent):
    if base ** expotent > 5000:
        return True
    else:
        return False

base = input("Input number(base): ")
expontent = input("Input the expontent: ")

print(large_power(int(base), int(expontent)))