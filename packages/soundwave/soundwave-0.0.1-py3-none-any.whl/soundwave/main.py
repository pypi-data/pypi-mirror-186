def pascal_triangle():
  n=int(input("Enter the number of rows: "))

  def fact(num):
    f = 1
    for i in range(1, num+1):
      f = f*i
    return f

  for i in range(n):
    for j in range(n-i):
      print(' ',end='')
    for j in range(i+1):
      val = int(fact(i)/(fact(j)*fact(i-j)))
      print(val, end=" ")
    print()

