print("Checking whether number is divisible by 10")
print()

num = input("enter number: ")

def divisible_by_10(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(divisible_by_10(int(num)))