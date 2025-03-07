import pandas as pd
import numpy as np


def max_and_mean(df):
    func = lambda x:pd.Series([x.max(),x.mean()],index=['max','mean'])
    frame = df.apply(func,axis=0).map(lambda x:f'{x:.2f}')
    # max_data = df.apply(np.max,axis=0)
    # mean_data = df.apply(np.mean,axis=0)
    # frame = pd.DataFrame([round(max_data,2),round(mean_data,2)],
    #                      index=['max','mean'])

    return frame


if __name__ == '__main__':
    with open('p_quiz1_data.txt','r') as f:
        data = [list(map(int,item.split(','))) for item in f]

    data = pd.DataFrame(data,
                        columns=['Ohio','Utah','Oregon','Texas'],
                        index=range(2010,2010+len(data)))
    print(data)
    print()
    max_mean_frame = max_and_mean(data)
    print(max_mean_frame)

