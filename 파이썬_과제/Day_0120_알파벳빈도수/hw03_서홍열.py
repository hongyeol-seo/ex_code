import matplotlib.pyplot as plt
import operator 
import platform 
import os 

class alphadisturb :
    
    
    def __init__(self) -> None:
        self.lowerdict = dict() 
        self.upperdict = dict()
        pass

    def drawplot(self):
        print(self.lowerdict.keys())
        print("t1")
        plt.bar(self.lowerdict.keys(), self.lowerdict.values())
        plt.show()


    def readfiles(self):
        df = open('loremipsum.txt',"r")
        print("type(df.read) : {}".format(type(df.read())))
        print("type(df) : {}".format(type(df)))
        print("길이 : {}".format(len(df.read())))
        
        df.seek(0)
        print("test")
               
        for i in df.read():
            if i.isalpha():
                if i.isupper():
                    #대문자라면
                    if i not in self.upperdict:
                        self.upperdict[i] = 1
                    else :
                        self.upperdict[i] += 1
                else :
                    #소문자라면
                    if i not in self.lowerdict:
                        self.lowerdict[i] = 1
                    else :
                        self.lowerdict[i] += 1
            else:
                pass        
        
    def sortdata():
        pass 

        # dictionary의 값을 기준으로 정렬 
        # 람다 사용 
        
        sorted_upperlist = sorted(upperdict.items(), key = lambda u : u[1], reverse=True) #-1  정렬
        sorted_upperdict = dict(sorted_upperlist)


    def showinfo(self):
        print("대문자 : {}".format(self.upperdict))
        print("소문자 : {}".format(self.lowerdict))

def main():
    al = alphadisturb()
    al.readfiles()
    al.showinfo() #데이터 정보보기
    al.sortdata()

    al.drawplot()
main()

    