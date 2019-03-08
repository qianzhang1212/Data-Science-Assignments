import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    if record[0] == 'a':
      for i in range(5):
        mr.emit_intermediate((record[1],i), record)
    else:
      for i in range(5):
        mr.emit_intermediate((i,record[2]), record)  

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    A = []
    B = []
    for v in list_of_values:
      if v[0] == 'a':
        A.append(v)
      else:
        B.append(v)
    total = 0
    for a in A:
      for b in B:
        if a[2] == b[1]:
          total += a[3]*b[3]
          break
    mr.emit((key[0],key[1],total))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
