import pandas as pd
import os
import os
from pathlib import Path
p = Path(os.getcwd())

df = pd.read_csv(str(p)+"\\database\\dados.csv", encoding="UTF-8", sep=";")
print(df.head())