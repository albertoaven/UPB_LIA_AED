import csv, pandas as pd

with open ("datos_empleo.csv", "r", newline="", encoding="UTF-8") as file:
  file = pd.read_csv(file)

  print(file)

  work = file[file["trabaja"] == True]
  notwork = file[file["trabaja"] == False]

  print()
  print(f"Trabajan {len(work)} personas:")
  print(work)
  print()
  print(f"No trabajan {len(notwork)} personas:")
  print()
  print(notwork)

  arg_work = file[(file["trabaja"] == True) & (file["pais"] == "Argentina")]
  arg_notwork = file[(file["trabaja"] == False) & (file["pais"] == "Argentina")]

  print()
  print(f"En Argentina, trabajan {len(arg_work)} personas:")
  print(arg_work)
  print()
  print(f"En Argentina, no trabajan {len(arg_notwork)} personas:")
  print()
  print(arg_notwork)