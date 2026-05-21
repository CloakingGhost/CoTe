# 시간 관리
# 시간과 몬스터의 공격의 시간을 비교
## 시간은 1씩 계속 증가
## 어텍배열 인덱스 변수를 선언
## 시간과 어택시간이 맞으면 배열의 값 사용
## 사용 이후 어택배열 인덱스 증가
### 인덱스가 배열의 길이보다 작은경우에만 동작하도록

# 몬스터의 공격이 최우선
## 공격당하면 체력 깍고 다음으로
## 연속성공횟수 0
## 시간 +1


# 마지막에 체력이 0보다 작은지 확인
## 작으면 멈추고 아니면 반복
def solution(bandage, health, attacks):
    max_bandage_cnt, recovery_per_second, add_recovery = bandage
    time, max_time = 0, attacks[-1][0]
    bandage_cnt = 0
    attacks_idx = 0
    attack_time, attack_amount = attacks[attacks_idx]
    hp = health
    while hp > 0 and time < max_time:
        time += 1
        if time == attack_time:
            hp -= attack_amount
            bandage_cnt = 0
            if attacks_idx + 1 < len(attacks):
                attacks_idx += 1
                attack_time, attack_amount = attacks[attacks_idx]
        else:
            # 회복
            hp += recovery_per_second
            
            bandage_cnt += 1
            # 추가 회복
            if bandage_cnt == max_bandage_cnt:
                hp += add_recovery
                # 초기화
                bandage_cnt = 0
                
            # 최대값 초과 방지
            if hp > health:
                hp = health
                
    return hp if hp > 0 else -1