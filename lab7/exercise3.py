books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  chrs = len(list(i))
  unq = len(set(i))
  bookTuple = chrs , unq
  book_dict[i] = bookTuple
for x in book_dict.keys():
  average = (book_dict[x][0]+book_dict[x][1])/2
  bookTuple = bookTuple[0],bookTuple[1],average
  book_dict[x] = bookTuple
for element in book_dict.keys():
  x = str(element) + " -> " + str(book_dict[element])
  print(x)