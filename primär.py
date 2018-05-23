def PrimFaktorZerlegung(n):

  for p in range(len(Primen)):
    while n % p == 0:
      Teiler.append(p)
       n = n/p
  return Teiler
