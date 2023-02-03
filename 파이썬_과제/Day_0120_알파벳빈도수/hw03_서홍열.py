import matplotlib.pyplot as plt
import operator
import platform
import os


class alphadisturb:

    def __init__(self) -> None:
        self.lowerdict = dict()
        self.upperdict = dict()
        pass

    def drawplot(self):
        # 대문자

        # 한글 폰트 사용
        if platform.system() == 'Windows':
            plt.rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin':
            # MacOS: Darwin
            plt.rc('font', family='AppleGothic')
        else:
            print('Unsupported System')

        fig, axes=plt.subplots(1, 3, figsize=(20, 10))
        fig.suptitle(f'알파벳 카운트:')

        plt.subplot(1, 2, 1)
        plt.title("대문자 개수")
        plt.bar(self.upperdict.keys(), self.upperdict.values())
        plt.xlabel('Alphabet')
        plt.ylabel("Count")

        # 소문자
        plt.subplot(1, 2, 2)
        plt.title("소문자 개수")
        plt.bar(self.lowerdict.keys(), self.lowerdict.values())
        plt.xlabel('Alphabet')
        plt.ylabel("Count")


        # 이미지 저장
        path = 'img'
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print()
        except Exception as e:
            print('Exception 발생: ', e)

        plt.savefig(path + '/' + "test"+'_count.png')
        plt.close()


    def readfiles(self):
        df = open('loremipsum.txt', "r")
        print("type(df.read) : {}".format(type(df.read())))
        print("type(df) : {}".format(type(df)))
        print("길이 : {}".format(len(df.read())))

        df.seek(0)
        print("test")

        for i in df.read():
            if i.isalpha():
                if i.isupper():
                    # 대문자라면
                    if i not in self.upperdict:
                        self.upperdict[i] = 1
                    else:
                        self.upperdict[i] += 1
                else:
                    # 소문자라면
                    if i not in self.lowerdict:
                        self.lowerdict[i] = 1
                    else:
                        self.lowerdict[i] += 1
            else:
                pass

    def sortdata(self):

        # dictionary의 값을 기준으로 정렬
        # 람다 사용

        sorted_upperlist = sorted(self.upperdict.items(
        ), key=lambda u: u[1], reverse=True)  # -1  정렬
        self.upperdict = dict(sorted_upperlist)

        sorted_lowerlist = sorted(self.lowerdict.items(
        ), key=lambda u: u[1], reverse=True)  # -1  정렬
        self.lowerdict = dict(sorted_lowerlist)

        print('*'*30)
        print(self.lowerdict)
        print('*'*30)

    def showinfo(self):
        print("대문자 : {}".format(self.upperdict))
        print("소문자 : {}".format(self.lowerdict))

    def saveimg(self):
        pass


def main():
    al = alphadisturb()
    al.readfiles()
    # al.showinfo() #데이터 정보보기
    al.sortdata()
    al.drawplot()


main()
