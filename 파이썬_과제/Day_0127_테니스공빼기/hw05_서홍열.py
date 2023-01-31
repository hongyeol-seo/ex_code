
class stackBall:

    def __init__(self):
        
        #저장공간
        self.stack = []
        self.ballcount = 0

    def input(self):
        if (self.ballcount == 5) :
            print(f'케이스가 꽉 찼습니다.')

        else :
            self.ballcount += 1
            self.stack.append(self.ballcount)            
            self.showInfo()

    def output(self):
        if self.ballcount == 0:
            print("케이스가 비었습니다.")
        
        else :
            del self.stack[-1]
            self.ballcount -= 1
            self.showInfo()

    def showInfo(self):
        if self.ballcount == 0:
            print("케이스가 비었습니다.")

        else :
            print(f'[공의 개수] : {self.ballcount}')
            print(self.stack[::-1])


def showList():
    
    print("-"*20)
    print(f'1.테니스 공 넣기')
    print(f'2.테니스 공 꺼내기')
    print(f'3.테니스 공 개수 출력')
    print(f'4.종료')

    try :
        choice = int(input("메뉴를 선택해주세요."))
        return choice

    except :
        print("잘못된 입력입니다. 다시 선택해주세요.")

def main():
    stb = stackBall()
    while True :
        num = showList()    
        #종료
        if (num == 4) : 
            print("프로그램을 종료합니다.")
            break

        #넣기
        elif (num == 1):
            stb.input()

        #빼기
        elif (num == 2):
            stb.output()

        #정보
        elif (num == 3):
            stb.showInfo()

main()




