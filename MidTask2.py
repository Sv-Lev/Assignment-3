l = [1, [2, 3], 4, [5, [6, 7]], 8] # created with help of this video "https://www.youtube.com/watch?v=FK29FtRCB74&ab_channel=ProgrammingandMathTutorials"
def flattened(name_list):
  filtered_list = []
  for i in name_list:
    if isinstance(i,list):
      filtered_list.extend(flattened(i))
    else:
      filtered_list.append(i)
  return  filtered_list
x = flattened(l)
print(x)