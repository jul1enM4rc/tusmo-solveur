import pandas as pd
from unidecode import unidecode

def get_base(file, taille, fisrt_lettre=None):
    df = pd.read_csv(file)["1_ortho"]
    if fisrt_lettre is not None:
        df = df[df.str.startswith(fisrt_lettre, na = False)]
    df = list(df[df.str.len() == taille])
    for i in range(len(df)):
        df[i] = unidecode(df[i])
    df = list(set(df))

    return df