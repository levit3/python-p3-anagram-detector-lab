class Anagram:
  def __init__(self, word):
      self.word = word

  def match(self, list):
      return [value for value in list if sorted(value) == sorted(self.word)]
  