l = list(map(int, input("Enter numbers for the List: ").split()))
x = int(input("The number u wanna use to filter list(all smaller one will be sorted out): "))
filt_x_l = [i for i in l if i>x]
nonnegative_l = [i for i in l if i>=0]
nonnegative_l_avg = sum(nonnegative_l)/len(nonnegative_l)
print("the list itself",(l))
print(f"only the numbers which are bigger tnen {x}: {filt_x_l}")
print(f"the avg of nonnegative: {nonnegative_l_avg}")