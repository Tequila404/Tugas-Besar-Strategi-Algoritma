profit   = [15,25,30,40,55,60]
bobot    = [1,3,5,7,9,10]
maxBerat = 18
total    = len(profit)

def knapsack(maxBerat, bobot, profit, total):
    K = []
    for i in range(total+1):
        K.append([0]*(maxBerat+1))

    for i in range(total + 1):
        for w in range(maxBerat + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif bobot[i - 1] <= w:
                K[i][w] = max(profit[i - 1]+ K[i - 1][w - bobot[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    maxProfit = K[total][maxBerat]
    print("Maks Profit : ", maxProfit)

    W = maxBerat
    print("Barang Yang Dibawa : ")
    for i in range(total, 0, -1):
        if maxProfit <= 0:
            break
        if maxProfit == K[i - 1][W]:
            continue
        else:
            print(bobot[i - 1])
            maxProfit -= profit[i - 1]
            W -= bobot[i - 1]

knapsack(maxBerat, bobot, profit, total)
