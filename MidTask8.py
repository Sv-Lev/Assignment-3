#Task8
l = list(input().split())
x = int(input("Strings that are lonager, then..."))
count = 0
for string in l:
  if len(string)>x:
    count += 1
print(f"number of strings that are longer: {count}")
