def neg(n):
  if (n==1):
    return 0
  elif (n==0):
    return 1
  else:
    return -100

def priorizador (a1, a2, a3, a4, cm1, cm0):
  na1 = neg(a1)
  na2 = neg(a2)
  na3 = neg(a3)
  na4 = neg(a4)
  ncm1 = neg(cm1)
  ncm0 = neg(cm0)

  cp1=(na1 & na2 & a3) | (na1 & na2 & a4) | (na1 & na2 & cm1) | (a3 & cm1 & ncm0) | (a4 & cm1 & cm0)
  cp0=(na1 & na2 & a4 & cm1) | (na1 & a2 & na3) | (na1 & na3 & a4) | (na1 & na3 & cm0) | (na1 & a2 & ncm1) | (na1 & a2 & cm0) | (a2 & cm1 & ncm0) | (a4 & cm1 & cm0)

  return [cp1, cp0]

def tester():
  for ta1 in range(2):
    for ta2 in range(2):
      for ta3 in range(2):
        for ta4 in range(2):
          for tcm1 in range(2):
            for tcm0 in range(2):
              [tcp1, tcp2] = priorizador(ta1, ta2, ta3, ta4, tcm1, tcm0)


              if (ta1==1 and ta2==0 and ta3==0 and ta4==0):
                if (tcp1==0 and tcp2==0):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")
              

              if (ta1==0 and ta2==1 and ta3==0 and ta4==0):
                if (tcp1==0 and tcp2==1):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")


              if (ta1==0 and ta2==0 and ta3==1 and ta4==0):
                if (tcp1==1 and tcp2==0):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")


              if (ta1==0 and ta2==0 and ta3==0 and ta4==1):
                if (tcp1==1 and tcp2==1):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")
              

              if (ta1==0 and ta2==0 and ta3==0 and ta4==0 and tcm1==0 and tcm0==0):
                if (tcp1==0 and tcp2==0):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")

              if (ta1==0 and ta2==0 and ta3==0 and ta4==0 and tcm1==1 and tcm0==0):
                if (tcp1==0 and tcp2==1):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")

              if (ta1==0 and ta2==0 and ta3==0 and ta4==0 and tcm1==1 and tcm0==0):
                if (tcp1==1 and tcp2==0):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")

              if (ta1==0 and ta2==0 and ta3==0 and ta4==0 and tcm1==1 and tcm0==1):
                if (tcp1==1 and tcp2==1):
                  pass
                else:
                  print(ta1, ta2, ta3, ta4, tcm1, tcm0, "failed")
  print("all tests completed")

tester()