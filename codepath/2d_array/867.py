# 1. Transpose Matrix
'''
input:
[
[1, 2],
[3, 4],
[5, 6]
]
output:
[
[1, 3, 5],
[2, 4, 6]
]

1 = matrix[0][0] -> matrix[0][0]
2 = matrix[0][1] -> matrix[1][0]
3 = matrix[1][0] -> matrix[0][1]
5 = matrix[2][0] -> matrix[0][2]
'''

def transpose(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  
  transposed_matrix = [[0] * rows for _ in range(cols)]
  # trnasposed_matrix = [[0] for _ in range(rows)] * cols
  # print(transposed_matrix)

  for row in range(rows):
    for col in range(cols):
      transposed_matrix[col][row] = matrix[row][col]
  

  return transposed_matrix

def main():
  tests = [
    { 'input': [[1]], 'output': [[1]] },
    { 'input': [[1,2]], 'output': [[1],[2]] },
    { 'input': [[1],[2]], 'output': [[1,2]] },
    # Add more tests
  ]

  for i in range(len(tests)):
    print('Test', i+1, 'Pass:',
      transpose(tests[i]['input']) == tests[i]['output']
    )

main()
