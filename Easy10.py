l = list(map(int,input("Nums for list: ").split()))
logic = []
x = int(input("U are dividing by: "))
for i in l:
  if i%x!=0:
    logic.append(False)
  else:
    logic.append(True)
print(logic)
