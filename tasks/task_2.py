letters = {1:"", 
  2: "abc",
  3: "def",
  4: "ghi",
  5: "jkl",
  6: "mno",
  7: "prst",
  8: "tuv",
  9: "wxyz",
  0: "+"
}


def combine(letters:dict, input:str):
  """create combination from letters
  letters[dict] -> dict with letters from phone
  input[str] -> string with key number from phone
  
  return[list] -> list with all posible combinations
  """

  result = ['']
  for x in input:
    result = [first+second for first in result for second in letters[int(x)]]
  return result


print(combine(letters, "46"))