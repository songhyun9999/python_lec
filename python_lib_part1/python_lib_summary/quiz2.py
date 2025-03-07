import numpy as np


def get_sum_multi(data):
    # 아래와 똑같이 동작
    sum_arr = np.cumsum(data,axis=0)
    mul = np.cumprod(data,axis=1)
    # sum_arr = []
    # mul = []
    # for col in data.T:
    #     m=0
    #     tmp = []
    #     for item in col:
    #         m = m + item
    #         tmp.append(m)
    #     sum_arr.append(tmp)
    # sum_arr = np.array(sum_arr, dtype=np.int32).T
    #
    #
    # for row in data:
    #     m = 1
    #     tmp =[]
    #     for item in row:
    #         m = m*item
    #         tmp.append(m)
    #     mul.append(tmp)
    # mul = np.array(mul,dtype=np.int32)

    return sum_arr,mul

def count_func(sum_arr,mul):
    # count = 0
    # for i in range(len(sum_arr)):
    #     for j in range(len(sum_arr[i])):
    #         if sum_arr[i][j] < mul[i][j]:
    #             count +=1

    count = sum_arr < mul
    print(count)
    count = np.sum(count)
    return count


if __name__ == '__main__':
    with open('n_quiz2_data.txt','r') as f:
        arr = [item.split(' ') for item in f]

    arr = np.array(arr,dtype=np.int32).reshape(3,3)

    print(arr,'\n')
    s_arr,m_arr = get_sum_multi(arr)
    print(s_arr,'\n\n',m_arr,'\n')
    print(count_func(s_arr,m_arr))