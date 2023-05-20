import random

screen=[]
num=[2,4,8]

def screen_into():#               
    for i in range(4):
        list_width = []
        for j in range(4):
            list_width.append('0')
        screen.append(list_width)

def screen_print():#            
    #print('      ' * 13)
    for i in range(4):
        #print('|',end='0')
        for j in range(4):
            sn = 4-len(str(screen[i][j]))
            print(' '*sn+screen[i][j],end='')
        print()
        #print('      '*13)

def produce_chess():#                  
    global screen
    while True:
        x=random.randint(0,3)
        y=random.randint(0,3)
        if screen[x][y]=='0':
            screen[x][y]=str(num[random.randint(0,2)])
            break

def referee():#      
    dete=False
    for i in range(4):
        for j in range(4):
            if screen[i][j]=='0':
                dete=True
    if not dete:
        for i in range(4):
            for j in range(3):
                if screen[i][j]==screen[i][j+1]:
                    dete=True
        for j in range(4):
            for i in range(3):
                if screen[i][j]==screen[i+1][j]:
                    dete=True
    return dete

def move_w():#      
    global screen
    dete=False
    for k in range(3):
        for i in range(1,4):#                        
            for j in range(4):
                if screen[i][j]!=screen[i-1][j] and screen[i-1][j]=='0':
                    screen[i][j],screen[i-1][j]=screen[i-1][j],screen[i][j]
                    dete=True
                    if i>1:
                        if screen[i-1][j]!=screen[i-2][j] and screen[i-2][j]=='0':
                            screen[i-1][j],screen[i-2][j]=screen[i-2][j],screen[i-1][j]
                            if i>2:
                                if screen[i-2][j]!=screen[i-3][j] and screen[i-3][j]=='0':
                                    screen[i-2][j],screen[i-3][j]=screen[i-3][j],screen[i-2][j]
        for i in range(1,4):#                                              
            for j in range(4):
                if screen[i][j]==screen[i-1][j] and screen[i][j]!='0':
                    screen[i-1][j]=str(int(screen[i][j])+int(screen[i-1][j]))
                    screen[i][j]='0'
                    dete = True
                    if i>1:
                        if screen[i][j]==screen[i-1][j] and screen[i][j]!='0':
                            screen[i-1][j]=str(int(screen[i][j])+int(screen[i-1][j]))
                            screen[i][j]='0'
                            screen[i-1][j],screen[i-2][j]=screen[i-2][j],screen[i-1][j]
                            if i>2:
                                if screen[i][j]==screen[i-1][j] and screen[i][j]!='0':
                                    screen[i-1][j]=str(int(screen[i][j])+int(screen[i-1][j]))
                                    screen[i][j]='0'
                                    screen[i-1][j],screen[i-2][j]=screen[i-2][j],screen[i-1][j]
                                    screen[i-2][j],screen[i-3][j]=screen[i-3][j],screen[i-2][j]
    if dete:
        produce_chess()
    screen_print()

def move_s():#      
    global screen
    dete=False
    for k in range(3):
        for i in range(2,-1,-1):
            for j in range(4):
                if screen[i][j]!=screen[i+1][j] and screen[i+1][j]=='0':
                    screen[i][j],screen[i+1][j]=screen[i+1][j],screen[i][j]
                    dete = True
                    if i<2:
                        if screen[i+1][j]!=screen[i+2][j] and screen[i+2][j]=='0':
                            screen[i+1][j],screen[i+2][j]=screen[i+2][j],screen[i+1][j]
                            if i<1:
                                if screen[i+2][j]!=screen[i+3][j] and screen[i+3][j]=='0':
                                    screen[i+2][j],screen[i+3][j]=screen[i+3][j],screen[i+2][j]
        for i in range(2,-1,-1):
            for j in range(4):
                if screen[i][j]==screen[i+1][j] and screen[i][j]!='0':
                    screen[i+1][j]=str(int(screen[i][j])+int(screen[i+1][j]))
                    screen[i][j]='0'
                    dete = True
                    if i<2:
                        if screen[i][j]==screen[i+1][j] and screen[i][j]!='0':
                            screen[i+1][j]=str(int(screen[i][j])+int(screen[i+1][j]))
                            screen[i][j]='0'
                            screen[i+1][j],screen[i+2][j]=screen[i+2][j],screen[i+1][j]
                            if i<2:
                                if screen[i][j]==screen[i+1][j] and screen[i][j]!='0':
                                    screen[i+1][j]=str(int(screen[i][j])+int(screen[i+1][j]))
                                    screen[i][j]='0'
                                    screen[i+1][j],screen[i+2][j]=screen[i+2][j],screen[i+1][j]
                                    screen[i+2][j],screen[i+3][j]=screen[i+3][j],screen[i+2][j]
    if dete:
        produce_chess()
    screen_print()

def move_a():#      
    global screen
    dete = False
    for k in range(3):
        for i in range(4):
            for j in range(1,4):
                if screen[i][j]!=screen[i][j-1] and screen[i][j-1]=='0':
                    screen[i][j],screen[i][j-1]=screen[i][j-1],screen[i][j]
                    dete = True
                    if j>1:
                        if screen[i][j-1]!=screen[i][j-2] and screen[i][j-2]=='0':
                            screen[i][j-1],screen[i][j-2]=screen[i][j-2],screen[i][j-1]
                            if j>2:
                                if screen[i][j-2]!=screen[i][j-3] and screen[i][j-3]=='0':
                                    screen[i][j-2],screen[i][j-3]=screen[i][j-3],screen[i][j-2]
        for i in range(4):
            for j in range(1,4):
                if screen[i][j]==screen[i][j-1] and screen[i][j]!='0':
                    screen[i][j-1]=str(int(screen[i][j])+int(screen[i][j-1]))
                    screen[i][j]='0'
                    dete = True
                    if j>1:
                        if screen[i][j]==screen[i][j-1] and screen[i][j]!='0':
                            screen[i][j-1]=str(int(screen[i][j])+int(screen[i][j-1]))
                            screen[i][j]='0'
                            screen[i][j-1],screen[i][j-2]=screen[i][j-2],screen[i][j-1]
                            if j>2:
                                if screen[i][j]==screen[i][j-1] and screen[i][j]!='0':
                                    screen[i][j-1]=str(int(screen[i][j])+int(screen[i][j-1]))
                                    screen[i][j]='0'
                                    screen[i][j-1],screen[i][j-2]=screen[i][j-2],screen[i][j-1]
                                    screen[i][j-2],screen[i][j-3]=screen[i][j-3],screen[i][j-2]
    if dete:
        produce_chess()
    screen_print()

def move_d():#      
    global screen
    dete = False
    for k in range(3):
        for i in range(4):
            for j in range(2,-1,-1):
                if screen[i][j]!=screen[i][j+1] and screen[i][j+1]=='0':
                    screen[i][j],screen[i][j+1]=screen[i][j+1],screen[i][j]
                    dete = True
                    if j<2:
                        if screen[i][j+1]!=screen[i][j+2] and screen[i][j+2]=='0':
                            screen[i][j+1],screen[i][j+2]=screen[i][j+2],screen[i][j+1]
                            if j<1:
                                if screen[i][j+2]!=screen[i][j+3] and screen[i][j+3]=='0':
                                    screen[i][j+2],screen[i][j+3]=screen[i][j+3],screen[i][j+2]
        for i in range(4):
            for j in range(2,-1,-1):
                if screen[i][j]==screen[i][j+1] and screen[i][j]!='0':
                    screen[i][j+1]=str(int(screen[i][j])+int(screen[i][j+1]))
                    screen[i][j]='0'
                    dete = True
                    if j<2:
                        if screen[i][j]==screen[i][j+1] and screen[i][j]!='0':
                            screen[i][j+1]=str(int(screen[i][j])+int(screen[i][j+1]))
                            screen[i][j]='0'
                            screen[i][j+1],screen[i][j+2]=screen[i][j+2],screen[i][j+1]
                            if j<3:
                                if screen[i][j]==screen[i][j+1] and screen[i][j]!='0':
                                    screen[i][j+1]=str(int(screen[i][j])+int(screen[i][j+1]))
                                    screen[i][j]='0'
                                    screen[i][j+1],screen[i][j+2]=screen[i][j+2],screen[i][j+1]
                                    screen[i][j+2],screen[i][j+3]=screen[i][j+3],screen[i][j+2]
    if dete:
        produce_chess()
    screen_print()

def score():#         
    score_sum=0
    for i in range(4):
        for j in range(4):
            score_sum+=int(screen[i][j])
    return score_sum

def main():
    screen_into()
    produce_chess()
    screen_print()
    while referee():
        user=input('input:')
        if user=='w' or user=='8':
            move_w()
        elif user=='s' or user=='2':
            move_s()
        elif user=='a' or user=='4':
            move_a()
        elif user=='d' or user=='6':
            move_d()
        else:
            print('WRONG')
    print('SCORE   ',score())
    input('exiting')

#if __name__=='__main__':
main()