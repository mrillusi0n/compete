def FindIntersection(strArr):

  # code goes here
  a = list(map(int, strArr[0].split(', ')))
  b = list(map(int, strArr[1].split(', ')))
  
  res = []
  
  ai = 0
  bi = 0
  
  while ai < len(a) and bi < len(b):
    ay = a[ai]
    be = b[bi]
    
    if ay == be:
      res.append(ay)
      ay += 1
      be += 1
    elif ay < be:
      ay += 1
    elif ay > be:
      be += 1
      
  return ','.join(res)
    

# keep this function call here 
print(FindIntersection(input()))

