#Task6
Pavlo = dict( math = "150", Mova = "124", English = "100" )
Ne_Pavlo = dict( math = "131", Mova = "122", English = "182" )
Zahar = dict( math = "15", Mova = "14", English = "10" )
Spanch_Bob = dict( math = "100", Mova = "100", English = "200" )
Patric = dict( math = "300", Mova = "300", English = "300" )
Lev = dict( math = "200", Mova = "200", English = "200" )


def nmt_sum(*args):
  a = dict()
  math = 0
  Mova = 0
  English = 0
  for name in args:
    for key,value in name.items():
      if key == "math":
        math += int(value)
      elif key == "Mova":
        Mova += int(value)
      elif key == "English":
        English += int(value)
  print(f"Math: {math}")
  print(f"Mova: {Mova}")
  print(f"English: {English}")


nmt_sum(Pavlo,Ne_Pavlo,Lev,Patric)
