# https://www.acmicpc.net/problem/20546
# 🐜 기적의 매매법 🐜

import sys

input = sys.stdin.readline

sm_cash = jh_cash = int(input())
prices = list(map(int, input().split()))


def getAsset(stock, cash, price):
    return stock * price + cash


timing = 0
BUY_TIMING = 3
SELL_TIMING = -3
sm_stock = 0
jh_stock = 0

for idx, price in enumerate(prices):

    # 준현
    if jh_cash >= price:
        jh_buy_stock = jh_cash // price
        jh_cash -= jh_buy_stock * price
        jh_stock += jh_buy_stock

    # 성민

    if idx == 0:
        continue

    price_diff = price - prices[idx - 1]
    # 연속일 초기화
    ## 주가 상승
    if price_diff > 0:
        # 매수 타이밍을 보고있었다면
        if timing > 0:
            timing = 0
        # 연속 하락일 계산
        if timing > SELL_TIMING:
            timing -= 1
    elif price_diff < 0:
        # 매도 타이밍을 보고있었다면
        if timing < 0:
            timing = 0
        # 연속 상승일 계산
        if timing < BUY_TIMING:
            timing += 1


    # 매수
    if sm_cash >= price and timing == BUY_TIMING:
        sm_buy_stock = sm_cash // price
        sm_cash -= sm_buy_stock * price
        sm_stock += sm_buy_stock

    # 매도
    elif sm_stock and timing == SELL_TIMING:
        sm_cash += sm_stock * price
        sm_stock = 0


SM_ASSET = getAsset(sm_stock, sm_cash, prices[-1])
JH_ASSET = getAsset(jh_stock, jh_cash, prices[-1])
print("BNP" if JH_ASSET > SM_ASSET else "TIMING" if SM_ASSET > JH_ASSET else "SAMESAME")
