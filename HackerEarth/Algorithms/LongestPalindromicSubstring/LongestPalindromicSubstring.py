dp_table = []

def print_matrix(dp_table):
  print("--------")
  for row in dp_table:
    print(row,sep= ' ')

def fill_default_palindromes(str):
  """Fills the DP Table for length 1 and 2.
  The variable of length 1 is always a palindrome.
  So for T[start=i,end = j] all the diagonal elements will be equal to 1
  start < end
  """
  # Fill for the palindrome for size 1
  for start in range(len(dp_table)):
    end = start
    # print(f"{start} {end}")
    dp_table[start][end] = 1
  # print_matrix(dp_table)

  # Fill for palindrome for size 2 start = 0 end = 1
  size = 2
  for start in range(len(dp_table)):
    end = start+size-1
    if end >= len(str):
      # print(end)
      break;
    if str[start] == str[end]:
      dp_table[start][end] = 1
    else:
      dp_table[start][end] =0

  # print_matrix(dp_table)

def build_dp_table(str):
  """builds the DP Table for the lenght of the string"""
  global dp_table
  rows,cols = len(str),len(str)
  dp_table = [[0 for i in range(cols)] for j in range(rows)]
  # print_matrix(dp_table)

def fill_dp_table(str):
  """For the strings greater than eq to the
    lengths of 3 a string is palindrome
    if str(start) == str(end)
    and the string inbetween the start and end is palindrome
    the string in between palindrome is calculated and filled in the table
    if the string is palindrome then we populate the table
    T[start,end] = 1

  """
  size = 3
  while size <= len(str):
    for start in range(len(str)):
      end = start+size - 1
      if end >= len(str):
        break
      if str[start] == str[end] and dp_table[start+1][end-1] == 1:
        dp_table[start][end] = 1
      else:
        dp_table[start][end] = 0
    # incrementing the size of the substring on every iteration
    size += 1

  # print_matrix(dp_table=dp_table)
  return None

def find_longest_palindrome():
  row = 0
  max_length = 1
  for rows in dp_table:
    for cols in range(len(rows)):
      # print(f"rows {row} cols {cols} value at the position is {rows[cols]}")
      if rows[cols] == 1:
        len_of_palindrome = cols - row +1
        # Determine the maximum length of the palindrome
        if len_of_palindrome > max_length:
          max_length = len_of_palindrome
          start,end = row,cols
    row += 1
  return start,end


def longest_palinndromic_substring(str):
  build_dp_table(str)
  fill_default_palindromes(str)

  fill_dp_table(str)

  start,end = find_longest_palindrome()
  # print(start,end)
  print(str[start:end+1])




inp = "jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"


longest_palinndromic_substring(inp)