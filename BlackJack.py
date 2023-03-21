#text_game

'''
블랙잭 ♠♥♦♣

*룰의 정의
A부터 J,Q,K까지 합하여 21 또는 21에 가까운 수를 가진 측이 승리. 21을 넘기면(버스트) 플레이어의 패배
사용하는 카드는 Joker를 제외한 52장, 1벌 또는 그 이상을 사용 가능
Ace는 1 또는 11. 플레이어의 편의로 선택 또는 룰에 따라 하나의 점수로 설정(1차적으로 Ace는 1점으로 간주하고 작성)
spade(♠,S), diamond(♦,D), heart(♥,H), club(♣,C)
J,Q,K는 10으로 간주

*룰의 구현을 위해 필요한 변수와 함수
게임에 사용할 카드
플레이어의 패
딜러의 패
플레이어와 딜러의 패에서 계산한 포인트
점수 테이블
'''
import random
import os
import platform
from time import sleep
#from IPython.display import clear_output
runningSystem=platform.system() #구동환경 확인

#화면 지우기
def clear(time):
    sleep(time)
    if runningSystem=="Windows":
        os.system('cls') #windows os
    elif runningSystem=="Darwin":
        os.system('clear') #mac os
    #elif runningSystem=="Linux":
        #os.system('clear') #linux os #실제 구동 미확인
    #clear_output()

#메인 화면
def gameMain():
    #안내 화면
    #R=규칙 안내, S=게임 시작, D=종료
    print('♠ ♥ ♦ ♣ Wellcome Blackjack ♠ ♥ ♦ ♣\n')
    print('키를 입력하여 주세요','\nR:규칙 S:게임시작 D:종료')
    command=str(input('\n입력: '))
    clear(0.5)
    return command

#종료
def displayEnd():
    input('\n임의의 키를 입력하면 게임이 종료됩니다.')
    clear(0.5)
    print(' ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣\n플레이 해주셔서 감사합니다\nThank you\n ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣')
    clear(3)

#룰 출력
def printRule():
    print('♠ ♥ ♦ ♣ Rule of Blackjack ♠ ♥ ♦ ♣\n')
    print('Joker를 제외한 52장의 카드, 1벌 또는 그 이상을 사용 가능',
          '\nA(1)부터 J,Q,K(10)까지 합하여 21 또는 21에 가까운 수를 가진 경우 승리.',
          '\n21을 넘기면(버스트) 패배')
    print('\n임의의 키를 입력하면 화면을 종료하고 메인 화면으로 돌아갑니다.')
    command=input('입력:')
    clear(0.5)
    return command

#카드의 무늬 표시
def printMark(lista):
    remark=[]
    for a in lista:
        if a[0]=='S':
            remark.append('♠ '+a[1:])
        elif a[0]=='D':
            remark.append('♦ '+a[1:])
        elif a[0]=='H':
            remark.append('♥ '+a[1:])
        else:
            remark.append('♣ '+a[1:])
    return remark

#카드패 가리기
def printMask(lista):
    lista=printMark(lista)
    remark=[]
    for a in range(len(lista)):
        if a == 0 :
            remark.append(lista[0])
        else:
            remark.append('▣ ?')
    return remark

#분배된 카드의 포인트 계산
def countPoint(lista):
    point=0
    for a in lista:
        point=point+pointTable[a[-1]]
    return point

#포인트 확인
def checkPoint(lista): #카드 배분후 21이 넘는지 확인하여 넘을경우 bust로 패배하고 게임 종료. 아니라면 진행. 21일 경우 자동 승리?(미구현)
    point=countPoint(lista) #A의 포인트를 1로 계산할 경우로 최소 bust 확인
    if point>21:
        return False
    else:
        return True

#최초 카드 분배 #player, dealer 순으로 한장씩 분배
def firstDistribution(lista,listb):
    i=0
    while i<4:
        distribution=stackOfCard.pop(0)
        if i%2==0:
            lista.append(distribution)
        else:
            listb.append(distribution)
        i+=1
    return lista

#카드 추가 분배
def callDistribution(lista):
    distribution=stackOfCard.pop(0)
    lista.append(distribution)
    return lista

#게임에 사용할 카드뭉치의 수 설정
def settingCard(num):
    socNum=num
    stackOfCard=oneStack*socNum
    return stackOfCard

#플레이어가 원할 경우 'A'를 11점으로 바꿀 수 있도록
#점수 계산 단계에서 플레이어에게 유리하게 계산되도록 설정
#def changeAce(listA):

#승부 판정
def comparePoint(player,dealer): #21점을 오버한 경우 자동 패배
    printResult()
    if countPoint(player)<=21 and countPoint(dealer)<=21:
        if countPoint(player)>countPoint(dealer):
            print('player의 승리')
        elif countPoint(player)==countPoint(dealer):
            print('무승부')
        else:
            print('player의 패배')
    else:
        if countPoint(player)>21:
            print('player Bust')
            print('player의 패배')
        elif countPoint(dealer)>21 and countPoint(player)<=21:
            print('dealer Bust')
            print('player의 승리')
        else:
            pass
            #확인된 이상 상태를 판정하여 룰을 추가

def printResult():
    playerPoint=countPoint(playerHand)
    dealerPoint=countPoint(dealerHand)
    print('dealer: ',printMark(dealerHand), dealerPoint,
          '\nplayer: ',printMark(playerHand), playerPoint)
    

#게임 종료
def gameEnd(result): #점수 비교 외 게임 종료 경우 호출
    if result=='D':
        print('게임 포기')
        sleep(1)
    elif result=='pB':
        printResult()
        print('player Bust\nplayer의 패배')
    elif result=='dB':
        printResult()
        print('dealer Bust\nplayer의 승리')

#플레이어의 분배가 완료되면 딜러는 17점 이상이 될때까지 한장씩 패를 추가
#16점 이하라면 의무적으로 한장씩, 17점이 넘으면 무조건 Stay
def dealerTurn():
    print('dealer의 패: ', printMask(dealerHand),
        '\nplayer의 패: ', printMark(playerHand),
        '\n\ndealer의 차례입니다.')
    clear(3)
    limit=17#의무 패 추가 기준
    while True:
        print('dealer의 패: ', printMark(dealerHand),
              '\nplayer의 패: ', printMark(playerHand),
              '\n\ndealer의 차례입니다.')
        clear(3)
        if checkPoint(dealerHand)==False:
            break
        if countPoint(dealerHand)<limit:
            callDistribution(dealerHand)
        elif countPoint(dealerHand)>=limit:
            break
    print('dealer의 패: ', printMark(dealerHand),
          '\nplayer의 패: ', printMark(playerHand))
    clear(2)

def gameStand():
    try:
        print('몇 벌의 카드뭉치를 사용할까요?')
        useNum=int(input('입력: '))#1벌을 사용할 경우 서렌더와 같은 세부 규칙이 없도록 할 수 있을까?
        stackOfCard=settingCard(useNum)
        clear(1)
        print(str(useNum)+' 벌의 카드뭉치로 게임을 시작합니다.')
        clear(3)
    except:
        stackOfCard=settingCard(int(1))
        clear(1)
        print('1 벌의 카드뭉치로 게임을 시작합니다.')
        clear(3)
    random.shuffle(stackOfCard)
    return stackOfCard

def gameStart():
    firstDistribution(playerHand,dealerHand)
    while True:
        print('dealer의 패: ', printMask(dealerHand),
              '\nplayer의 패: ',printMark(playerHand))
        if checkPoint(playerHand)==False:
            end='pB'
            clear(1)
            gameEnd(end)
            break
        print('\n카드를 더 받으시겠습니까?(Hit:H, Stay:S, Surrender:D)')
        playerChoice=str(input('입력(H/S/D): '))
        clear(1)
        if playerChoice=='H' or playerChoice=='h':
            #카드를 한 장 추가 분배
            callDistribution(playerHand)
        elif playerChoice=='S' or playerChoice=='s': #분배를 종료하고 딜러에게 차례를 넘김
            dealerTurn()
            comparePoint(playerHand,dealerHand)
            break
        elif playerChoice=='D' or playerChoice=='d':
            #게임을 포기
            end='D'
            gameEnd(end)
            break
        else:
            print('올바른 입력이 아닙니다.')
            clear(1)

#game standby
pointTable={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':10,'J':10,'Q':10,'K':10}
oneStack=['SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK',
          'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',
          'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK',
          'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK']
def gameInitialize():
    playerHand=[]
    dealerHand=[]
    playerPoint=0
    dealerPoint=0
    return playerHand, dealerHand, playerPoint, dealerPoint

#player in
clear(0)
while True:
    com=gameMain()
    if com=='S' or com=='s':
        #게임 준비
        playerHand, dealerHand, playerPoint, dealerPoint = gameInitialize() #초기화
        stackOfCard=gameStand() #새로 셔플하는 기능 구현 필요 or 게임 시작 시 한번만 셔플
        #게임 시작
        gameStart()
        input('임의의 키를 입력하여 계속 진행')
        clear(0.5)
    elif com=='R' or com=='r':
        #규칙 출력
        printRule()
    elif com=='D' or com=='d':
        displayEnd()
        break

#21이면 바로 승리로 할 수 있는가?
#이후 Ace의 점수 변경 및 세부 규칙을 적용할 것
