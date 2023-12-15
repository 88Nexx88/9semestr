import pandas as pd
def View(df, name):
    df.to_html('html\\'+name)
    return('html\\'+name)