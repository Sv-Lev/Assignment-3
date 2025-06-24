#Task5
l = list(map(int,input().split()))
l_2 = list(map(int,input().split()))
if len(l) == len(l_2):
  l_3 = list(zip(l, l_2))
  print(l_3)
else:
  print(l)
  print(l_2)
