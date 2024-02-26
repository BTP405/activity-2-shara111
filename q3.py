def wordCount(t):
  """
  This function takes a string `t` and returns a dictionary where the keys are unique words in the string and the
  corresponding values are lists of line numbers where the words are found in the string.

  Args:
    t: A string containing the text to be analyzed.

  Returns:
    A dictionary where the keys are unique words in the string and the corresponding values are lists of line numbers
    where the words are found in the string.
  """

  word_counts = {}
  lines = t.splitlines() #spliting the input text into individual files and using the splitlines() to store them in a list called lines
  for line_number, line in enumerate(lines, start=1): #iterating over each line in the lines first, and use enumerate to keep track of both the line number
    words = line.lower().split() #it extracts individual words using split(), and also converts to lower for the case insensitive
    for word in words: # iterates over each word in the current line
      if word not in word_counts: #if the word is not apready present in the word_count dictionary
        word_counts[word] = [] #it adds the word as a key and initializes an empty list as its value
      word_counts[word].append(line_number) 

  return word_counts #it returns the final word_counts distionary

# Example usage
text = """This is a sample text file.
It has multiple lines.
Let's see how the wordCount function works."""

word_counts = wordCount(text)

print(word_counts)
