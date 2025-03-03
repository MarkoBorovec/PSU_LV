try:
 ocjena=float(input("Unesite jedan broj u rasponu od 0.0 do 1.0: "))

 if 0.0 <= ocjena <=1.0:
   if ocjena >= 0.9:
      print("A")
   elif ocjena >= 0.8:
      print("B")
   elif ocjena >= 0.7:
      print("C")
   elif ocjena >= 0.6:
      print("D")
   else:
      print("F")
 else :
    print("Greska: Uneseni broj nije u intervalu od 0.1 do 1.0")

except ValueError :
   print("Greška: Ponovno unesi jedan broj u rasponu od 0.0 do 1.0")