
loopCnt = 0
while True:
  loopCnt += 1
  for maxVal in range(1,69):
    x = 1
    for i in range(1,maxVal):
      x *= i
    #print("Factorial: {}  = {}".format(maxVal, x))
  if loopCnt % 10000  == 0:
    print("Factorial loops: {}".format(loopCnt))




