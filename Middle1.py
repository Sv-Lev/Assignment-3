l = list(map(int,input("Nums for list: ").split()))
x =int(input())
y = int(input())
l_filt = [i for i in l if i % x==0 and i % y!= 0]
print(f"Devisible by {x}, not by {y}: {l_filt}")