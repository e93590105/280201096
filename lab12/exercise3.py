class dna:
  def __init__(self,string):
    self.set_string(string)
  def get_string(self):
    return self.string
  def set_string(self,string):
    self.string = string

  def count_nucleotides(self):
    countA = 0
    countT = 0
    countC = 0
    countG = 0
    for i in self.string:
      if i == "A":
        countA += 1
      elif i == "T":
        countT += 1
      elif i == "C":
        countC += 1
      elif i == "G":
        countG += 1
    dictCounts = {}
    dictCounts["A"] = countA
    dictCounts["T"] = countT
    dictCounts["C"] = countC
    dictCounts["G"] = countG
    return dictCounts
  
  def calculate_complement(self):
    complement = ""
    for i in self.string:
      if i == "A":
        complement += "T"
      elif i == "T":
        complement += "A"
      elif i == "C":
        complement += "G"
      elif i == "G":
        complement += "C"
    return complement
  
  def count_point_mutations(dna):
    