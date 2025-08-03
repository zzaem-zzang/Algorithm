def solution(before, after):
    Flag = 0
    before = list(before)
    after = list(after)
    before.sort()
    after.sort()
    if after == before:
        return 1
    else :
        return 0
