def func(n):
  array = [int(element) for element in str(n)]

  product = 1
  for element in array:
    product *= element
  array_sum = sum(array)
  return(product - array_sum)

print(func(123456))
