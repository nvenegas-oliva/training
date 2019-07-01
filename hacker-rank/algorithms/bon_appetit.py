def bon_appetit(n, k, costs, b):
    anna_bill = int((sum(costs) - costs[k]) / 2)
    """
    if anna_bill == b:
        print("Bon Appetit")
    else:
        print(b - anna_bill)
    """
    return 'Bon Appetit' if anna_bill == b else b - anna_bill

if __name__ == '__main__':
    std_in = input().split()
    n = int(std_in[0])
    k = int(std_in[1])
    costs = list(map(int, input().split()))
    b = int(input())
    print(bon_appetit(n, k, costs, b))