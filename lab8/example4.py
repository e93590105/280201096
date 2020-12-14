def binary_to_dec(b):
  binary = list(b).reverse
  decimal = 0
  for i in binary:
    decimal += 2**i
  return(decimal)  

def dec_to_binary(d):
  binary = []
  while True:
    if d%2 == 0:
      binary.append("0")
      d = d/2
    elif d%2 == 1:
      binary.append("1")
      d = d//2
    if d == 1:
      binary.append("1")
      break
  binary = str(binary.reverse())
  return(binary)

def main():
  b = "10010"
  print(binary_to_dec(b))
  d = 18
  print(dec_to_binary(d))

main()