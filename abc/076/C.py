from copy import deepcopy


def main():
    S = input()
    T = input()

    import pdb; pdb.set_trace()
    for i in range(len(S)-len(T)+1):
        if S[i] == T[0]:
            ans = deepcopy(S)
            for j in range(1, len(T)):
                if S[i+j] != "?":
                    break
                print(S[i+j])
                ans[i+j] = T[j]

    print(ans)


if __name__ == "__main__":
    main()
