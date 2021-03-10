#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/
testcases = int(input())

def determine_min_deletions(firstWord,secondWord):
  len_firstWord = len(firstWord)
  len_secondWord = len(secondWord)
  count = 0

  #from the short string see how many characters are actually present in the second string
  #subtract the rest and we will get anagrams

  if len_firstWord < len_secondWord:
    #Number of common characters between first and second words
    for x in firstWord:
      if x in secondWord:
        count = count+1
        secondWord.remove(x)
  else:
    for x in secondWord:
      if x in firstWord:
        count = count+1
        firstWord.remove(x)
        # print(firstWord)
  # print(f"firstWord {firstWord} counter {count}")

  # Adding the elements in both the list and subtracting the removed elements. Multiplying it by 2 because the common
  # element in in both first and second
  print(len_firstWord+len_secondWord-2*count)
  return None

for cases in range(testcases):
  inp1 = input()
  inp2 = input()
  #Strings are immutable in python
  firstWord = []
  secondWord = []
  firstWord[:0] = inp1
  secondWord[:0] = inp2
  determine_min_deletions(firstWord,secondWord)
