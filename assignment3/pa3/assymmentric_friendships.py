import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    a = record[0]
    b = record[1]

    mr.emit_intermediate(min(a,b),record)

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    results = []
    for v in list_of_values:
      flag0 = 0
      #flag1 = 0
      for w in list_of_values:
        if(v[0] == w[1] and v[1] == w[0]):
          flag0 = 1
      if(flag0 == 0):
        '''
        for u in results:
          if(v[0] == u[0] and v[1] == u[1]):
            flag1 = 1
        if(flag1 == 0):
          results.append(v)
        '''
        results.append(v)
        
    for r in results:
      mr.emit((r[1],r[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
