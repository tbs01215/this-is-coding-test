N = 3   # 요소의 갯수(3층짜리 트리)
arr = [1, 2, 3]
sel = [0] * N   # 부분집합 담을 그릇(0, 1 깜빡이)


def powerset(idx):  # 몇 층을 보고있는가
    if idx == N:    # 끝에 도착 했을 때 실행되는 부분
        print(sel, " : ", end=" ")
        # 출력: '[1, 1, 1] : '
        # 출력: '[1, 1, 0] : '
        for i in range(N):  # 0 1 2
            if sel[i]:
                # (13~) 1 / 1 / 1
                # (18~) 1 / 1 / 0
                print(arr[i], end=' ')
                # (13~) 출력: '1' / '2' / '3'
                # (18~) 출력: '1' / '2'
        print()
        return  # 없으면 계속 호출만 하고 탈출을 못해서 인덱스에러 나지롱(백지 복습에서 안써서 당함;)

    sel[idx] = 1
    # (3) [`1, 0, 0] / (6) [1, `1, 0] / (9) [1, 1, `1]
    powerset(idx+1)     # 다음 층
    # 이 분기가 이해가 되지 않는다면 그려놓은 .png 파일을 보세용
    sel[idx] = 0        # (14)3층 [1, 1, `0] / (19)2층
    powerset(idx+1)


powerset(0)     # (1)
