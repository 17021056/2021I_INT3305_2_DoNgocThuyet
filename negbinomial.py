import math

def prob(n, p, r):
    fact = lambda f:1 if f==0 else f*fact(f-1)
    NCK = fact(n-1) / (fact(r-1) * fact(n-r))
    result = NCK * pow(p, r) * pow(1 - p, n - r)
    return result

def infoMeasure(n, p, r):
    pro = prob(n, p, r)
    result = - math.log(pro, 2)
    return result

def sumProb(N, p, r):
    """ Call funtion sumProb(50, 0.5 , 2) ta được kết quả là 0.9999999999999112 ~ 1
	Call funtion sumProb(101, 0.5 , 2) ta được kết quả là 0.9999999999999999 ~ 1
        Call funtion sumProb(200, 0.5 , 2) ta được kết quả là 0.9999999999999999 ~ 1
        Call funtion sumProb(500, 0.5 , 2) ta được kết quả là 0.9999999999999999 ~ 1
            Như vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố negative binomial bằng 1 """
    sum = 0
    for i in range(r, N):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
    """ Entropy của nguồn negative binomial với N=100, p=1/2, r=2 là 2.711468724220612
        Entropy của nguồn negative binomial với N=250, p=1/2, r=2 là 2.711468724220612
	Entropy của nguồn negative binomial với N=500, p=1/2, r=2 là 2.711468724220612 """
    entropy = 0
    for i in range(r, N):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy

print(sumProb(50 , 0.5 , 2))
print(sumProb(101, 0.5 , 2))
print(sumProb(200, 0.5 , 2))
print(sumProb(500, 0.5 , 2))
print(approxEntropy(100, 0.5 , 2))
print(approxEntropy(250, 0.5 , 2))
print(approxEntropy(500, 0.5 , 2))