
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('-elephant', 'relev-ant'), ('AAAGAATTCA', 'AAA---T-CA')] #Elements in the third pair is swapped. 

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return min(MED(S[1:],T)+1, min(MED(S, T[1:])+1, MED(S[1:], T[1:])))
        else:
            return min(MED(S[1:],T)+1, min(MED(S, T[1:])+1, MED(S[1:], T[1:])+1))

def fast_MED(S, T, MED={}):
    dp = [[0] * (len(S)+1) for _ in range(len(T)+1) ]
    for i in range(len(S)+1): dp[0][i] = i
    for i in range(len(T)+1): dp[i][0] = i
    
    for i in range(1,len(T)+1):
        for j in range(1, len(S)+1):
            if S[j-1] == T[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[-1][-1]

def fast_align_MED(S, T, MED={}): # Classmate Zeyi Chen contributed greatly to this function. 
    if (S, T) in MED:
        return MED[(S, T)][0], MED[(S, T)][1]
    if (S == ""):
        MED[(S,T)] = ("-"*len(T),T, len(T))
        return "-"*len(T),T
    elif (T == ""):
        MED[(S, T)] = (S, "-"*len(S), len(S))
        return S, "-"*len(S)
    else:
        if (S[0] == T[0]):
            a = fast_align_MED(S[1:], T, MED)
            b = fast_align_MED(S, T[1:], MED)
            c = fast_align_MED(S[1:], T[1:], MED)
            cnt1 = MED[(S[1:], T)][2] + 1
            cnt2 = MED[(S, T[1:])][2] + 1
            cnt3 = MED[(S[1:], T[1:])][2]
            a = (S[0]+a[0], "-"+a[1])
            b = ("-"+b[0], T[0]+b[1])
            c = (S[0]+c[0], T[0]+c[1])
            if cnt3 <= cnt2 and cnt3 <= cnt1:
                MED[(S, T)] = (c[0], c[1], cnt3)
            elif cnt2 <= cnt3 and cnt2 <= cnt1:
                MED[(S, T)] = (b[0], b[1], cnt2)
            else:
                MED[(S, T)] = (a[0], a[1], cnt1)
            return MED[(S, T)][0], MED[(S, T)][1]
        else:
            a = fast_align_MED(S[1:], T, MED)
            b = fast_align_MED(S, T[1:], MED)
            c = fast_align_MED(S[1:], T[1:], MED)
            cnt1 = MED[(S[1:], T)][2] + 1
            cnt2 = MED[(S, T[1:])][2] + 1
            cnt3 = MED[(S[1:], T[1:])][2] + 1
            a = (S[0]+a[0], "-" + a[1])
            b = ("-" + b[0], T[0]+b[1])
            c = (S[0] + c[0], T[0] + c[1])
            if cnt3 <= cnt2 and cnt3 <= cnt1:
                MED[(S, T)] = (c[0], c[1], cnt3)
            elif cnt2 <= cnt3 and cnt2 <= cnt1:
                MED[(S, T)] = (b[0], b[1], cnt2)
            else:
                MED[(S, T)] = (a[0], a[1], cnt1)
            return MED[(S, T)][0], MED[(S, T)][1]

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
