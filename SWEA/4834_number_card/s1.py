import sys
sys.stdin = open('sample_input.txt')

'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
 
'''

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    cards_count = [0] * 10
    cards = int(input())

    while cards > 0:
        cards_count[cards % 10] += 1
        cards = cards // 10
    for i in range(9, -1, -1):
        if cards_count[i] == max(cards_count):
            print(f'#{testcase} {i} {max(cards_count)}')
            break
