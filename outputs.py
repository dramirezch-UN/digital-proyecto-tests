def neg(n):
  if (n==1):
    return 0
  elif (n==0):
    return 1
  else:
    return -1

def outputs(Q3,Q2,Q1,Q0):
  p1 = (neg(Q3) | neg(Q0))
  p0 = Q3 & Q0

  c12= neg(Q1) & neg(Q0) | Q1 & Q0 | Q2 | Q3
  c11= neg(Q2) & Q1 & neg(Q0)			
  c10= neg(Q3) & neg(Q2) & neg(Q1) & Q0

  c22= Q1 & neg(Q0) | Q2 & Q0 | neg(Q2) & neg(Q1)
  c21= Q2 & neg(Q1) & neg(Q0)
  c20= neg(Q2) & Q1 & Q0

  c32= neg(Q1) &  neg(Q0) | Q1 & Q0 | neg(Q2)
  c31= Q2 & Q1 & neg(Q0)
  c30= Q2 & neg(Q1) & Q0
  
  c42= neg(Q3) & neg(Q2) | neg(Q3) & neg(Q1) | neg(Q3) & neg(Q0) | neg(Q2) & Q0
  c41= Q3 & neg(Q0)
  c40= Q2 & Q1 & Q0

  print('peatonal',p1,p0)
  print("carril1",c12,c11,c10)
  print("carril2",c22,c21,c20)
  print("carril3",c32,c31,c30)
  print("carril4",c42,c41,c40)

def testOutputs():
  print('testing 0000')
  outputs(0,0,0,0)
  print("-----")
  print('testing 0001')
  outputs(0,0,0,1)
  print("-----")
  print('testing 0010')
  outputs(0,0,1,0)
  print("-----")
  print('testing 0011')
  outputs(0,0,1,1)
  print("-----")
  print('testing 0100')
  outputs(0,1,0,0)
  print("-----")
  print('testing 0101')
  outputs(0,1,0,1)
  print("-----")
  print('testing 0110')
  outputs(0,1,1,0)
  print("-----")
  print('testing 0111')
  outputs(0,1,1,1)
  print("-----")
  print('testing 1000')
  outputs(1,0,0,0)
  print("-----")
  print('testing 1001')
  outputs(1,0,0,1)
  print("-----")

testOutputs()

