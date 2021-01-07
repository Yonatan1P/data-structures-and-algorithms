def rotate_clockwise(matrix):
  output = []
  for i in range(len(matrix)):
    current_output_row = []
    for j in range(len(matrix[0])):
      print(j)
      current_output_row += [matrix[len(matrix[0])-1-j][i]]
    output += [current_output_row]
  return output
