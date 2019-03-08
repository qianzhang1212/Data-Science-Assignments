import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(record):
    # YOUR CODE GOES HERE
    txt = record[0]
    value = record[1]
    for w in set(value.split()):
      mr.emit_intermediate(w,txt)

# Implement the REDUCE function
def reducer(key, list_of_values):
    # YOUR CODE GOES HERE
    mr.emit((key, list_of_values))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
