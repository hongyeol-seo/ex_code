'''
스택 자료구조를 활용한 테니스 공 추가, 삭제 기능 구현
스택 크기: 3

'''

class Stack:

    def __init__(self, stack_size):
        '''

        :param stack_size: 스택의 크기
        '''
        self.stack = []
        self.max_stack_size = stack_size
        self.top = -1 
        self.coin_count = 1

    def push(self):
        if(self.top < self.max_stack_size):
            self.top = self.top + 1
            self.stack.append(self.coin_count)
            print(f'몇 개 {self.stack}')
            self.coin_count += 1
            self.show_stack()
        else:
            print("Stack is full.")

    def pop(self):
        '''
            Pop from stack
        :return: null
        '''
        if(self.top > 0):
            item = self.stack[self.top]
            print("Pop(", item, ")")
            self.top = self.top - 1
            self.show_stack()
        else:
            print("Stack is empty")

    def show_stack(self):

        if(self.top < 0):
            print("Stack is empty. No item in stack.")
            return

        print("[Stack size]: ", self.top+1)
        for index in range(self.top, -1, -1):
            print(self.stack[index], end=" ")
        print()

def show_menu():
    print("------------------------------")
    print("1. 테니스 공 넣기")
    print("2. 테니스 공 꺼내기")
    print("3. 테니스 공 개수 출력")
    print("4. 종료")
    opt = int(input("메뉴를 선택하세요: "))
    return opt

def main():
    STACK_SIZE = 3
    coinstack = Stack(STACK_SIZE)
    option = 0
    while(True):
        option = show_menu()
        if(option == 1):
            coinstack.push()
        elif(option == 2):
            coinstack.pop()
        elif(option == 3):
            coinstack.show_stack()
        elif(option == 4):
            break
        else:
            print("잘못된 메뉴 선택입니다.")



main()