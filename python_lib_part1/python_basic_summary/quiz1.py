# 파일을 읽어 객체로 데이터를 돌려주는 함수

def get_list_data(f):
    # score = []
    # for line in f.readlines():
    #     score.append(int(line))
    score = list(map(int,[line for line in f]))
    return score


# 리스트를 받아 조건에 맞는 값을 추출하고 출력하는 함수
def grade_out_func(score):
    n_data = len(score)
    total_score = 0
    for s in score:
        total_score += s
    mean_score = round(total_score/n_data,1)
    n = 0
    for s in score:
        if s > mean_score:
            n += 1

    print(f'{n_data} {mean_score} {round((n/n_data)*100,2)}')


if __name__ == '__main__':
    fd = open('quizdata1.txt','r')
    scores = get_list_data(fd)
    fd.close()
    # print(scores)
    grade_out_func(scores)
