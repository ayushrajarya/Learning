list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c= [561,651,651,65,1651,65,165,1651,61,8,654]
for ind,( a, b,c) in enumerate(zip(list_a, list_b, list_c)):
  # Add your code here!
  print(max(a,b,c))
  print(ind)
print("avssssssssssss")
for ind,t in enumerate(zip(list_a, list_b, list_c)):
  # Add your code here!
  print(max(t))
  print(ind)
  print(type(t))