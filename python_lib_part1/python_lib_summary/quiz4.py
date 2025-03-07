import pandas as pd
import numpy as np

def city_group_data(frame):
    rframe = frame.T.groupby({'ohio':'us','seoul':'kor',
                           'daegu':'kor','texas':'us'})
    return rframe.mean().T.map(lambda x:f'{x:.1f}')


if __name__ == '__main__':
    df = pd.read_csv('p_quiz2_data.txt')
    print(df,'\n\n')
    print(city_group_data(df))
