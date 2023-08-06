from decimal import Decimal, ROUND_HALF_UP
import pandas as pd

def reverse_list(lst):
    lst_new = []
    for i in range(1, len(lst) + 1):
        lst_new.append(lst[-i])
    return lst_new

def sort_values(ls, reverse=False):
    if all([':' in str(x) for x in ls]):
        ls = pd.DataFrame({'lst': ls})
        try:
            ls['num'] = ls['lst'].apply(lambda x: float(x.split(':')[0]))
            ls = ls.sort_values(by=['num'])
        except:
            ls = ls.sort_values(by=['lst'])
        ls = ls['lst'].tolist()
    else:
        ls.sort()
    if reverse is True:
        ls = reverse_list(ls)
    return ls

def sort_trace_name(string):
    if ':' in str(string):
        return string.split(':')[1].strip()
    else:
        if type(string) == str:
            return string.title()
        else:
            return string

def sort_df_dimension(df, dimension, reverse=False):
    df = df.sort_values(by=[dimension])
    if all([':' in str(x) for x in df[dimension].unique().tolist()]):
        try:
            df['sortD'] = df[dimension].apply(lambda x: int(float(x.split(':')[0])))
            df = df.sort_values(['sortD'], ascending=not reverse)
            df[dimension] = df[dimension].apply(lambda x: x.split(':')[1].strip())
        except:
            pass
    return df

def round2(n):
    n = Decimal(str(n)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    return float(n)
