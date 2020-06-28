def print_mat(mat):
  print("########")
  for i in mat:
    print(i)

def lcs(string_a, string_b):
  mat = [[0 for x in range(len(string_a) + 1)] for y in range(len(string_b) + 1)]    

  for j in  range(1, len(string_b) + 1):
    for i in range(1, len(string_a) + 1):
      if string_b[j - 1] == string_a[i - 1]:
        mat[j][i] = 1 + mat[j - 1][i - 1]        
      else:
        mat[j][i] = max(mat[j][i - 1], mat[j - 1][i])      

  return mat[len(mat) - 1][len(mat[0]) - 1]

  
print(lcs("ABCD", "AXBXD"))