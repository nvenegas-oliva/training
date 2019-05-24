
def no_idea(N, A, B):
    return sum(1 for n in N if n in A) - sum(1 for n in N if n in B)


if __name__ == "__main__":
    n, m = input().split()
    N = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(no_idea(N, A, B))
    file = open("hacker-rank/no-idea-input05.txt", mode="r").readlines()
    n, m = file[0].split()
    n, m
    N = list(map(int, file[1].split()))
    A = set(map(int, file[2].split()))
    B = set(map(int, file[3].split()))
    print(no_idea(N, A, B))
