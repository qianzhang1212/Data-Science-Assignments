import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    key = record[1]
    value = record
    mr.emit_intermediate(key,value)

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    order = []
    items = []

    for v in list_of_values:
      if v[0] == 'order':
        order.append(v[:])
      else:
        items.append(v[:])

    for o in order:
      for i in items:
        mr.emit(o+i)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
