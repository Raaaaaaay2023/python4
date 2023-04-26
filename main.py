#1
# n = int(input("Enter the number of elements in the first set: "))
# a = set(map(int, input("Enter the elements of the first set: ").split()))

# m = int(input("Enter the number of elements in the second set: "))
# b = set(map(int, input("Enter the elements of the second set: ").split()))

# # Intersection of sets
# c = sorted(list(a.intersection(b)))

# print("Numbers common to both sets in ascending order: ")
# for num in c:
#     print(num, end=" ")

#2
n = int(input("enter the quantity of bushs:"))#enter the quantity of bushs
a = list(map(int, input().split("enter the quantity of berries in each bush:")))# enter the quantity of berries in each bush

max_berries = 0

for i in range(n):
    berries = a[i] + a[(i-1)%n] + a[(i+1)%n]
    max_berries = max(max_berries, berries)

print(max_berries)