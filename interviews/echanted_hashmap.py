def solution(queryType, query):
  hashmap, sum_hashmap, counter_key, counter_value = dict(), 0, 0, 0
  sum_hashmap = 0
  for operation, queryValues in zip(queryType, query):
    if operation == "insert":
      hashmap[queryValues[0] - counter_key] = queryValues[1] - counter_value
    elif operation == "get":
      sum_hashmap += hashmap[queryValues[0] - counter_key] + counter_value
    elif operation == "addToKey":
      counter_key += queryValues[0]
    elif operation == "addToValue":
      counter_value += queryValues[0]
  return sum_hashmap


queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1, 2], [2, 3], [2], [1], [3]]

print(solution(queryType, query))
