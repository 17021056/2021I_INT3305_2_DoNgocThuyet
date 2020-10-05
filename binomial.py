import math

def prob(n, p, N):
    fact = lambda f: 1 if f == 0 else f * fact(f - 1)
    NCK = fact(N) / (fact(n) * fact(N - n))
    result = NCK * pow(p, n) * pow(1 - p, N - n)
    return result

def infoMeasure(n, p, N):
    prb = prob(n, p, N)
    result = - math.log(prb, 2)
    return result

def sumProb(N, p):
    """ Call funtion sumProb(50, 0.5) ta được kết quả là 0.9999999999999982 
	Call funtion sumProb(101, 0.5) ta được kết quả là 0.9999999999999999 
        Call funtion sumProb(200, 0.5) ta được kết quả là 1
        Call funtion sumProb(500, 0.5) ta được kết quả là 0.9999999999999998 
        Như vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binamial bằng 1 """
    sum = 0
    for i in range(1, N):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    """ Entropy của nguồn binomial với N=100, p=1/2 là 4.369011409223017
	Entropy của nguồn binomial với N=250, p=1/2 là 5.029985788332068
        Entropy của nguồn binomial với N=500, p=1/2 là 5.529987244677518 """
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

print(sumProb(50 , 0.5))
print(sumProb(101, 0.5))
print(sumProb(200, 0.5))
print(sumProb(500, 0.5))
print(approxEntropy(100, 0.5))
print(approxEntropy(250, 0.5))
print(approxEntropy(500, 0.5))
