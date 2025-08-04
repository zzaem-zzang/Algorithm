# 순서 S,D,H,C  겹치면 ERROR


T = int(input())
for Tc in range(T):
    S = []
    D = []
    H = []
    C = []
    card_set = set()
    error = False
    lst = []
    cards = input()
    for i in range(0,len(cards),3):
        card = cards[i:i+3]
        if card in card_set:
            error = True
            break
        card_set.add(card)

        chr = card[0]
        num = card[1:]

        if chr =='S':
            S.append(num)
        elif chr =='D':
            D.append(num)
        elif chr =='H':
            H.append(num)
        elif chr =='C':
            C.append(num)
        
    if error:
        print(f'#{Tc+1} ERROR')
    else:
        print(f'#{Tc+1} {13- len(S)} {13 -len(D)} {13-len(H)} {13-len(C)}')