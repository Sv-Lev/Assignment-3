l = list(map(int, input("Enter numbers for the List: ").split()))
s = sum(l)
multiplier = int(input("Enter the num to multiply the whole list by: "))
mlist = [i*2 for i in l]
copy_l = l.copy()
copy_l.reverse()
odds = [i for i in l if i%2 != 0]
print("the list itself",(l))
print("Sum:", s)
print(f"Min number : {min(l)}")
print(f"reversed list: {copy_l}")
print("only odd nums", (odds))
print(f"numbers after multiplication", (mlist))