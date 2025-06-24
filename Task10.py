#Task10
l = list(map(int, input().split()))
y = int(input("Multiplier"))
x = int(input("condition"))
l_2 = [i*y for i in l if i>x ]
print(l_2)
