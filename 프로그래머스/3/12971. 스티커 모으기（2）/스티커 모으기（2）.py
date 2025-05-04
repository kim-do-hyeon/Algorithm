def solution(sticker):
    answer = 0
    n = len(sticker)    
    if n == 1 :
        return sticker[0]
    
    def solve(dp_stickers) :
        dp = [0] * len(dp_stickers)
        dp[0] = dp_stickers[0]
        if len(dp_stickers) > 1 :
            dp[1] = max(dp_stickers[0], dp_stickers[1])
        for i in range(2, len(dp_stickers)) :
            dp[i] = max(dp[i - 1], dp[i - 2] + dp_stickers[i])
        return dp[-1]
    
    q1 = solve(sticker[:-1])
    q2 = solve(sticker[1:])
    answer = max(q1, q2)
    return answer