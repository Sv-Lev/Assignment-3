#Task3
def task3():
  l = "jkvdfckmwkKJHLS efj  oekwdok LKJKLdm"
  l_2 = [i for i in l if i.isupper()]
  for i in l_2:
    print(i)
#Task4
def task4():
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    l_2 = l.copy()

    print(l)
def task4b():
   #Task4(sort )
l = list(map(int,input().split()))
c = []
for i in l:
  a=l.count(i)
  t = (i, a)
  c.append(t)
c.sort(key=lambda с :с[1], reverse=True)
f_l = [i for (i,y) in c ]
print(f_l)
