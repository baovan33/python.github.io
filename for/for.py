list = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}),
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}),
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}),
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for index, (x,y) in enumerate(list):
  
    for i in x: 
        print(x[i],end=' ')
    print(' ')
    
    for i in y: 
        print(y[i],end=' ')
    print(' ')
