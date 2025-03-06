class Student:
    count = 0
    def __init__(self):
        self.name = input('이름을 입력하세요: ')
        self.scores = list(map(int,input('국어 영어 수학 점수를 입력하세요: ').split(' ')))
        Student.count += 1
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self,scores):
        if not isinstance(scores, list):  # 리스트인지 확인
            raise ValueError("scores는 리스트여야 합니다.")

        for score in scores:
            if score < 0:
                raise ValueError('not a score')

        self._scores = scores

    def print_info(self):
        print(f'name:{self.name}')
        print(f'국어:{self.scores[0]}, 영어:{self.scores[1]}, 수학:{self.scores[2]}')

    def total_score(self):
        total = 0
        for score in self.scores:
            total += score
        return total


if __name__ == '__main__':
    ch = 'y'
    students = []
    while ch == 'y':
        student = Student()
        students.append(student)
        ch = input('계속 입력하시겠습니까?(y/n) ')

    total_score = 0
    for student in students:
        student.print_info()

        total_score += student.total_score()

    print(f'총점:{total_score}\n'
          f'평균:{total_score/Student.count:.2f}')


