def neg(n):
  if (n==1):
    return 0
  elif (n==0):
    return 1
  else:
    return -100

def nextState(Q3, Q2, Q1, Q0, P, NV, A, CP1, CP0, COUNT3, COUNT30, COUNT90):
  nQ3 = neg(Q3)
  nQ2 = neg(Q2)
  nQ1 = neg(Q1)
  nQ0 = neg(Q0)

  nP = neg(P)
  nNV = neg(NV)
  nA = neg(A)
  nCP1 = neg(CP1)
  nCP0 = neg(CP0)
  nCOUNT3 = neg(COUNT3)
  nCOUNT30 = neg(COUNT30)
  nCOUNT90 = neg(COUNT90)

  # Estas expresiones comentadas son equivalentes a las de más abajo pero tienen un par de terminos más.
  # Q3next = (nQ3 & nQ2 & nQ1 & nQ0 & P & NV) | (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & nA) | (nQ3 & Q2 & Q1 & Q0 & COUNT90) | (Q3 & nQ2 & nQ1 & nQ0 & nCOUNT3) | (Q3 & nQ2 & nQ1 & Q0 & nCOUNT30)

  # Q2next = (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & A & CP1 & nCP0) | (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & A & CP1 & CP0) | (nQ3 & nQ2 & nQ1 & nQ0 & nP & CP1 & nCP0) | (nQ3 & nQ2 & nQ1 & nQ0 & nP & CP1 & CP0) | (nQ3 & nQ2 & Q1 & Q0 & COUNT90) | (nQ3 & Q2 & nQ1 & nQ0 & nCOUNT3) | (nQ3 & Q2 & nQ1 & Q0) | (nQ3 & Q2 & Q1 & nQ0 & nCOUNT3) | (nQ3 & Q2 & Q1 & Q0 & nCOUNT90)

  # Q1next = (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & A & nCP1 & CP0) | (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & A & CP1 & CP0) | (nQ3 & nQ2 & nQ1 & nQ0 & nP & nCP1 & CP0) | (nQ3 & nQ2 & nQ1 & nQ0 & nP & CP1 & CP0) | (nQ3 & nQ2 & nQ1 & Q0 & COUNT90) | (nQ3 & nQ2 & Q1 & nQ0 & nCOUNT3) | (nQ3 & nQ2 & Q1 & Q0 & nCOUNT90) | (nQ3 & Q2 & nQ1 & Q0 & COUNT90) | (nQ3 & Q2 & Q1 & nQ0 & nCOUNT3) | (nQ3 & Q2 & Q1 & Q0 & nCOUNT90)
  
  # Q0next = (nQ3 & nQ2 & nQ1 & nQ0) | (nQ3 & nQ2 & nQ1 & Q0 & nCOUNT90) | (nQ3 & nQ2 & Q1 & Q0 & nCOUNT90) | (nQ3 & Q2 & nQ1 & Q0 & nCOUNT90) | (nQ3 & Q2 & Q1 & Q0 & nCOUNT90) | (Q3 & nQ2 & nQ1 & Q0 & nCOUNT30)


  Q3next = (nQ3 & nQ2 & nQ1 & nQ0 & P & NV) | (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & nA) | (nQ3 & Q2 & Q1 & Q0 & COUNT90) | (Q3 & nQ2 & nQ1 & nQ0 & nCOUNT3) | (Q3 & nQ2 & nQ1 & Q0 & nCOUNT30)

  Q2next = (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & A & CP1) | (nQ3 & nQ2 & nQ1 & nQ0 & nP & CP1) | (nQ3 & nQ2 & Q1 & Q0 & COUNT90) | (nQ3 & Q2 & nQ1 & nQ0 & nCOUNT3) | (nQ3 & Q2 & nQ1 & Q0) | (nQ3 & Q2 & Q1 & nQ0 & nCOUNT3) | (nQ3 & Q2 & Q1 & Q0 & nCOUNT90)

  Q1next = (nQ3 & nQ2 & nQ1 & nQ0 & P & nNV & A & CP0) | (nQ3 & nQ2 & nQ1 & nQ0 & nP & CP0) | (nQ3 & nQ2 & nQ1 & Q0 & COUNT90) | (nQ3 & nQ2 & Q1 & nQ0 & nCOUNT3) | (nQ3 & nQ2 & Q1 & Q0 & nCOUNT90) | (nQ3 & Q2 & nQ1 & Q0 & COUNT90) | (nQ3 & Q2 & Q1 & nQ0 & nCOUNT3) | (nQ3 & Q2 & Q1 & Q0 & nCOUNT90)
    
  Q0next = (nQ3 & nQ2 & nQ1 & nQ0) | (nQ3 & nQ2 & nQ1 & Q0 & nCOUNT90) | (nQ3 & nQ2 & Q1 & Q0 & nCOUNT90) | (nQ3 & Q2 & nQ1 & Q0 & nCOUNT90) | (nQ3 & Q2 & Q1 & Q0 & nCOUNT90) | (Q3 & nQ2 & nQ1 & Q0 & nCOUNT30)

  return [Q3next, Q2next, Q1next, Q0next]

def fuzzer():
  for tq3 in range(2):
    for tq2 in range(2):
      for tq1 in range(2):
        for tq0 in range(2):
          for tp in range(2):
            for tnv in range(2):
              for ta in range(2):
                for tcp1 in range(2):
                  for tcp0 in range(2):
                    for tcount3 in range(2):
                      for tcount30 in range(2):
                        for tcount90 in range(2):
                          ns = nextState(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90)
                          
                          # path 1
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==1 and	tnv==1):
                            if(ns[0]==1 and ns[1]==0 and ns[2]==0 and ns[3]==1):
                              pass
                              # print(tq3, tq2, tq1,	tq0,	tp,	tnv,"||", ns, "Passed")
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 1")
                          
                          # path 2
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==1 and	tnv==0 and ta==0):
                            if(ns[0]==1 and ns[1]==0 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 2")
                          
                          # path 3
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==1 and	tnv==0 and ta==1 and tcp1==0 and tcp0==0):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 3")

                          #path 4    
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==1 and	tnv==0 and ta==1 and tcp1==0 and tcp0==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==1 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 4")
                          
                          # path 5
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==1 and	tnv==0 and ta==1 and tcp1==1 and tcp0==0):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 5")

                          # path 6
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==1 and	tnv==0 and ta==1 and tcp1==1 and tcp0==1):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==1 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 6")
                          
                          # path 7
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==0 and tcp1==0 and tcp0==0):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 7")

                          # path 8
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==0 and tcp1==0 and tcp0==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==1 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 8")

                          # path 9
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==0 and tcp1==1 and tcp0==0):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 9")

                          # path 10
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==0 and	tp==0 and tcp1==1 and tcp0==1):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==1 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 10")

                          # -- de aquí en adelante son los que actuan con timers (de B en adelante)

                          # path 11
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==1 and tcount90==0):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 11")
                          
                          # path 12
                          if (tq3==0 and	tq2==0 and	tq1==0 and	tq0==1 and tcount90==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==1 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, "|" , tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 12")

                          # path 13
                          if (tq3==0 and	tq2==0 and	tq1==1 and	tq0==0 and tcount3==0):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==1 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 13")
                          
                          # path 14
                          if (tq3==0 and	tq2==0 and	tq1==1 and	tq0==0 and tcount3==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 14")

                          # path 15
                          if (tq3==0 and	tq2==0 and	tq1==1 and	tq0==1 and tcount90==0):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==1 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 15")

                          # path 16
                          if (tq3==0 and	tq2==0 and	tq1==1 and	tq0==1 and tcount90==1):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 16")

                          # path 17
                          if (tq3==0 and	tq2==1 and	tq1==0 and	tq0==0 and tcount3==0):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 17")

                          # path 18
                          if (tq3==0 and	tq2==1 and	tq1==0 and	tq0==0 and tcount3==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 18")
                          
                          # path 19
                          if (tq3==0 and	tq2==1 and	tq1==0 and	tq0==1 and tcount90==0):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 19")

                          # path 20
                          if (tq3==0 and	tq2==1 and	tq1==0 and	tq0==1 and tcount90==1):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==1 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0,"|", tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 20")
                            
                          # path 21
                          if (tq3==0 and	tq2==1 and	tq1==1 and	tq0==0 and tcount3==0):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==1 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 21")

                          # path 22
                          if (tq3==0 and	tq2==1 and	tq1==1 and	tq0==0 and tcount3==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 22")
                            
                          # path 23
                          if (tq3==0 and	tq2==1 and	tq1==1 and	tq0==1 and tcount90==0):
                            if(ns[0]==0 and ns[1]==1 and ns[2]==1 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 23")

                          # path 24
                          if (tq3==0 and	tq2==1 and	tq1==1 and	tq0==1 and tcount90==1):
                            if(ns[0]==1 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0, tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 24")

                          # path 25
                          if (tq3==1 and	tq2==0 and	tq1==0 and	tq0==0 and tcount3==0):
                            if(ns[0]==1 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0,"|" , tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 25")

                          # path 26
                          if (tq3==1 and	tq2==0 and	tq1==0 and	tq0==0 and tcount3==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0,"|", tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 26")
                            
                          # path 27
                          if (tq3==1 and	tq2==0 and	tq1==0 and	tq0==1 and tcount30==0):
                            if(ns[0]==1 and ns[1]==0 and ns[2]==0 and ns[3]==1):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0,"|" , tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 27")

                          # path 28
                          if (tq3==1 and	tq2==0 and	tq1==0 and	tq0==1 and tcount30==1):
                            if(ns[0]==0 and ns[1]==0 and ns[2]==0 and ns[3]==0):
                              pass
                            else:
                              print(tq3,tq2,tq1,tq0,"|" , tp, tnv, ta, tcp1, tcp0, tcount3, tcount30, tcount90,"||", ns, "Failed, path 28")
  

  print("All tests completed.")
  return 0

fuzzer()