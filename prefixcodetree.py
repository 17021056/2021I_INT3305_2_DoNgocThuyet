class PrefixCodeTree:
  def __init__(self): # hàm tạo class
    # thiết lập cây nhị phân theo mảng
    self.tree = [0]*10000

  def insert(self,codeword,symbol):
    #tìm index của codeword
    index=0
    for element in codeword:
      if element == 1: 
        index = index * 2 + 2
      elif element == 0:
        index = index * 2 + 1
    #chỉ định symobl vào trong tree[index]
    self.tree[index]=symbol

  def decode(self,encodedData, datalen):
    # tạo giá trị
    results=""
    index=0
    # convert encodedData
    data=""
    for byte in encodedData:
      data += f'{byte:0>8b}'
    #start decode
    for i in range(datalen):
      char = data[i]
      if char == '1': 
        index = index * 2 + 2
      elif char == '0':
        index = index * 2 + 1
      #if find a symbol, add to results, go to root of tree
      if self.tree[index] != 0:
        results += " " + self.tree[index]
        index=0 
    return results

codeTree = PrefixCodeTree()
codebook = {
  'x1': [0], 
  'x2': [1,0,0], 
  'x3': [1,0,1], 
  'x4': [1,1] 

}

for symbol in codebook:
  codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)