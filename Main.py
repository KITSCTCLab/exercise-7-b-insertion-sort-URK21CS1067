from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  for i in range(1, len(data)):
  
        key = data[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < data[j] :
                data[j + 1] = data[j]
                j -= 1
        data[j + 1] = key

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
