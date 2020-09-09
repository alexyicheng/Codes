Z = []

a = input("bitte, geben Sie das Anfangsintervall(0<Anfangsinervall<5) ein :")
A = int(a)


b = input("bitte, geben Sie das Endintervall(Anfangsinervall<Endintervall<5333) ein :")
B = int(b)

#main
Y = 0
X = 0
K = A

print("K ist "+ str(A))
print("B ist "+str(B))

# Procedure KONSTANT
def KONSTANT():
  print("Calls the Procedure KONSTANT")
  D = 12*K+4
  MI = (6*K-2)*K
  MA = (6*K+10)*K+3
  MIN = (6*K-1)*(6*K-1)
  MAX = (6*K+5)*(6*K+5)-2
  print("K= "+str(K)+",D:20,"+str(K)+" = "+str(D))
  print("MI = "+str(MI)+",MA =:20,"+str(MA))
  print("MIN = "+str(MIN)+",MAX=:20,"+str(MAX))
  print(" ")
  return D
  

#PROCEDURE SIEB
def SIEB(X):
    print("Calls the procedure SIEB")
    for N in range(0,D-1):
        Z.append(N)
    print(" ")

# Procedure P1
def P1(X):
    print("Calls the procudeure P1")
    J1 = int((MI+I)/N1)
    P = N1+J1-I
    if P < MI:
        P = N1+P
    N = X
    while N < int(D):
        Z[N]= 0
        N = N+N1
    print(" ")


#PROCEDURE SIEBEN
def SIEBEN(A):
    print("Calls the procedure SIEBEN")
    X  = A
    MI = (6*K-2)*K
    Y = 0
    I = 1
    N = 0
    for I in range(I,K):
      N1 = 6*I-1
      N2 = 6*I+1
      print("I = "+str(I))
      print("N1 = "+str(N1)+" N2 = "+str(N2))
      P1(N)
    for N in range(N,D-1):
      print(Z[N])
      if Z[N]!=0:
        X = X+1
        Y = Y+1
        erg = N+MI 
        erg1 = 6*erg-1
        erg2 = 6*erg+1
        print(str(X)+","+str(Y)+":5,("+str(N)+"+"+str(MI)+"):15,"+str(erg)+":15,"+str(erg1)+":15:,"+str(erg2))
    print(" ")


if B <= 1300:
  while K < B :
    print("starts the main function")
    print("Summe "+str(K-1)+" = "+str(X)+" PZZP:10 "+str(K-1)+" = "+str(Y))
    KONSTANT()
    D = KONSTANT()
    SIEB(D)
    SIEBEN(X)
    K += 1
  print(" ")
else:
  while K < B:
    print("starts the main function")
    print("Summe "+str(K-1)+" = "+str(X)+" PZZP:10 "+str(K-1)+" = "+str(Y))
    D = 3*K
    MA = 6*K*K-2+K-1 # (6*K-2)*K-1
    while MA < (6*K+10)*K+3:
      MI = MA+1
      MA = MI+D
      SIEB()
      SIEBEN(X)
    K += 1
  print(" ")
 



  




















