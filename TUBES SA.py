biaya = [20,30,25,15,40]
berat = [1,3,5,7,8]
maxBerat = 14
total = len(biaya)

def knapsack(maxBerat, berat, biaya, total):
    K = []
    for i in range(total+1):
        K.append([0]*(maxBerat+1))

    for i in range(total + 1):
        for w in range(maxBerat + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif berat[i - 1] <= w:
                K[i][w] = max(biaya[i - 1]+ K[i - 1][w - berat[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    maxProfit = K[total][maxBerat]
    print("Keuntungan Maksimal : ", maxProfit)

    W = maxBerat
    print("Barang Yang Dibawa : ")
    for i in range(total, 0, -1):
        if maxProfit <= 0:
            break
        if maxProfit == K[i - 1][W]:
            continue
        else:
            print(berat[i - 1])
            maxProfit -= biaya[i - 1]
            W -= berat[i - 1]

knapsack(maxBerat, berat, biaya, total)
