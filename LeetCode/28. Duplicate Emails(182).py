import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    s=set()
    duplicate=set()
    for i in person['email']:
        if i in s:
            duplicate.add(i)
        else:
            s.add(i)
    df=pd.DataFrame({'Email': list(duplicate)})
    return df
