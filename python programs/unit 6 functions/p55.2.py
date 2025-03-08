# Python filter() function example

user=input('choose for filter a or b:')
def filterdata(x):
 if user in x[0]:
  return x
# Calling function

result= filter(filterdata,('apple','angur','banana','berry'))
# Displaying result
print(list(result))
  