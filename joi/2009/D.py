from itertools import combinations, permutations

def main():
    n = int(input())
    k = int(input())
    cards = [input() for _ in range(n)]
    nums = []
    for comb in combinations(cards, k):
        # print(comb)
        for per in permutations(comb, k):
            nums.append(int("".join(per)))
    
    print(len(set(nums)))


if __name__ == "__main__":
    main()
