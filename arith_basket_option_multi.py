""" --------------- Arithmetic Basket Options  ---------------"""
from math import *
from scipy import *
from scipy import stats
import scipy
import numpy 
# from option_pricer_gui import *

def arith_basket_option_multi(S, sigma, r, T, K, ro_matrix, option_type, path_num, method):
    # S = []
    print(S, sigma, r, T, K, ro_matrix, option_type, path_num, method)
    ro_matrix2 = []
    matrix = [[0 for i in range(3)] for i in range(3)]
    for i in range(len(S)):
        ro_matrix2.append([])
        for j in range(len(S)):
            if j == i:
                ro_matrix2[i].append(1)
            elif j > i:
                ro_matrix2[i].append(ro_matrix[i]) 
            else:
                ro_matrix2[i].append(ro_matrix[j])
    ro_matrix = ro_matrix2           
    arith_basket_payoff = numpy.empty(path_num)
    geo_basket_payoff = numpy.empty(path_num)
    S_sum = 0
    for i in range(path_num):
        for j in range(len(S)):
            # numpy.random.multivariate_normal()
            Z = random.multivariate_normal([0]*len(S), ro_matrix, path_num).T
            print(Z)
            growthFactor = exp(
                (r - 0.5 * sigma[j - 1] * sigma[j - 1]) * T + sigma[j - 1] * sqrt(T) * (Z[j - 1]))
            # a[j-1] = S[j-1]*growthFactor
            # S_sum += a[j-1]
            S_sum += S[j-1]*growthFactor
        arith_basket_mean = numpy.mean(S_sum)
        print((1.0 / len(S)) * sum(numpy.log(S_sum)))
        geo_basket_mean = exp((1.0 / len(S)) * sum(numpy.log(S_sum)))

        if (option_type == 'call'):
            arith_basket_payoff[i] = exp(-r * T) * \
                max(arith_basket_mean - K, 0)
            geo_basket_payoff[i] = exp(-r * T) * max(geo_basket_mean - K, 0)
        elif (option_type == 'put'):
            arith_basket_payoff[i] = exp(-r * T) * \
                max(K - arith_basket_mean, 0)
            geo_basket_payoff[i] = exp(-r * T) * max(K - geo_basket_mean, 0)

    if (method == 'standard'):
        pmean = np.mean(arith_basket_payoff)
        pstd = np.std(arith_basket_payoff)
        confmc = (pmean - 1.96 * pstd / sqrt(path_num),
                  pmean + 1.96 * pstd / sqrt(path_num))
        return pmean, confmc
    elif (method == 'control variate'):
        covxy = numpy.mean(arith_basket_payoff * geo_basket_payoff) - numpy.mean(arith_basket_payoff) * numpy.mean(
            geo_basket_payoff)
        theta = covxy / numpy.var(geo_basket_payoff)

        # Control Variate Version
        geo = geo_basket_option_multi(
            S, sigma, r, T, K, ro_matrix, option_type)
        # z = [x + y for x, y in zip(arith_basket_payoff, map(lambda x: theta * (geo - x), geo_basket_payoff))]
        z = arith_basket_payoff + theta * (geo - geo_basket_payoff)
        zmean = numpy.mean(z)
        zstd = numpy.std(z)
        zconfvc = (zmean - 1.96 * zstd / sqrt(path_num),
                   zmean + 1.96 * zstd / sqrt(path_num))
        print(zmean, zconfvc)
        return zmean, zconfvc


def geo_basket_price_multi(S, sigma, r, T, K, ro_matrix, option_type):
    sigma_bg = 0
    for i in range(len(S)):
        for j in range(len(S)):
            sigma_bg += sigma[i] * S[j].sigma[i] * ro_matrix[i][j]
    sigma_bg = sqrt(sigma_bg) / len(S)
    miu_bg = r + 0.5 * sigma_bg * sigma_bg
    bg0 = 1
    for i in range(len(S)):
        miu_bg -= 0.5 * S[i].v * S[i].v / len(S)
        bg0 *= S[i]
    bg0 **= (1 / float(len(S)))

    d1 = (log(bg0 / K) + (miu_bg + 0.5 * sigma_bg ** 2) * T) / \
        (sigma_bg * sqrt(T))
    d2 = d1 - sigma_bg * sqrt(T)

    if option_type == 'call':
        value = exp(-r * T) * (bg0 * exp(miu_bg * T) *
                               stats.norm.cdf(d1) - K * stats.norm.cdf(d2))
    elif option_type == 'put':
        value = exp(-r * T) * (K * stats.norm.cdf(-d2) -
                               bg0 * exp(miu_bg * T) * stats.norm.cdf(-d1))
    return value

# arith_sum = 0
# geo_sum=1
# for i in range(path_num):
#     for j in range(len(S)):
#         Z = random.multivariate_normal([0]*len(S), ro_matrix, path_num).T
#         growthFactor = exp((r - 0.5 * sigma[j - 1] * sigma[j - 1]) * T + sigma[j - 1] * sqrt(T) * (Z[j - 1]))
#         S[j-1] = S[j-1]*growthFactor
#         arith_sum += S[j-1]
#         geo_sum *= S[j-1]

#     arith_basket_mean = np.mean(arith_sum)
#     geo_basket_mean = power(geo_sum, 1/len(S))

# def arith_basket_option_three(s1=100, s2=100, s3=100,v1=0.3, v2=0.3, v3=0.3, r=0.05, T=3, k=100, correlation_1and2=0.5,correlation_1and3=0.5,
#                      correlation_2and3=0.5,option_type="call", M=100000,method="standard"):
#     s = [s1, s2, s3]
#     sigma = [v1, v2, v3]
#     result = arith_basket_option_multi(s, sigma, r, T, K, [ro_1and2, ro_1and3, ro_2and3], option_type, path_num, method))
#     return basket.get_basket_price_arith(M, method)

print(arith_basket_option_multi([100, 100, 100], [
      0.3, 0.3, 0.3], 0.05, 3, 100, [0.5, 0.5, 0.5], "put", 100000, "standard"))

# theta = np.cov(arithPayoff_seq, geoPayoff_seq)[0][1] / np.var(geoPayoff_seq)
# Target = []
# for i in range(0, len(arith_basket_payoff_seq)):
#     T_value = arithPayoff_seq[i] + theta * (geo_expected - geoPayoff_seq[i])
#     Target.append(T_value)
# Tmean = np.mean(Target)
# Tstd = np.std(Target)
# confcv_lower = Tmean - 1.96 * Tstd / sqrt(path_num)
# confcv_upper = Tmean + 1.96 * Tstd / sqrt(path_num)
# return Tmean, confcv_lower, confcv_upper


# for i in range(len(S)):
#     for j in range(i, len(S)):
#         ro_matrix[i][j] = 0
#
#
#
#
# ro=request.form.getlist('g')
# rau1=rau[0].split(",,")
# rau2=[]
# for i in range(1,len(rau1)):
#     rau2.append(rau1[i].split(","))
# for i in range(len(rau2)):
#     for j in range(len(rau2)):
#         rau2[i][j]=float(rau2[i][j])
#
# print( arith_basket_option_multi(([100,100,100], [0.3,0.3,0.3], 0.05,3,100,a,call,10000,'standard')))


# def arith_basket_option_three(S1, S2, S3, sigma1, sigma2, sigma3, r, T, K, ro_matrix, option_type, path_num,
#                               method):
#     # drift1 = (r - 0.5 * sigma1 * sigma1) * T
#     # drift2 = (r - 0.5 * sigma2 * sigma2) * T
#     # sigma1_sqrt = sigma1 * math.sqrt(T)
#     # sigma2_sqrt = sigma2 * math.sqrt(T)
#     # exp_rT = math.exp(-r * T)
#
#     for i in range(1, asset_no + 1):
#         for j in range(i + 1, asset_no + 1):
#             ro_matrix[i - 1][j - 1] = 0
#     ro_matrix = np.mat(ro_matrix)
#
#
#     arith_basket_payoff = numpy.empty(path_num)
#     geo_basket_payoff = numpy.empty(path_num)
#
#     for i in range(path_num):
#         Z1 = numpy.random.normal(0, 1)
#         Z2 = ro * Z1 + sqrt(1 - ro * ro) * numpy.random.normal(0, 1)
#         a1 = S1 * exp((r - 0.5 * sigma1 ** 2) * T + sigma1 * sqrt(T) * Z1)
#         a2 = S2 * exp((r - 0.5 * sigma2 ** 2) * T + sigma2 * sqrt(T) * Z2)
#         # a1 = S1 * math.exp(drift1 + sigma1_sqrt * Z1)
#         # a2 = S2 * math.exp(drift2 + sigma2_sqrt * Z2)
#         arith_basket_mean = (a1 + a2) / 2
#
#         # geo_basket_mean = math.exp(math.log(arith_basket_mean))
#         geo_basket_mean = math.sqrt(a1 * a2)
#
#         if option_type == 'call':
#             # arith_basket_payoff_call = math.exp(-r * T) * max(arith_basket_mean - K, 0)
#             arith_basket_payoff_call = exp(-r * T) * max(arith_basket_mean - K, 0)
#             arith_basket_payoff[i] = arith_basket_payoff_call
#             # geo_basket_payoff_call = math.exp(-r * T) * max(geo_basket_mean - geo_K, 0)
#             geo_basket_payoff_call = exp(-r * T) * max(geo_basket_mean - K, 0)
#             geo_basket_payoff[i] = geo_basket_payoff_call
#         elif option_type == 'put':
#             # arith_basket_payoff_put = math.exp(-r * T) * max(K - arith_basket_mean, 0)
#             arith_basket_payoff_put = exp(-r * T) * max(K - arith_basket_mean, 0)
#             arith_basket_payoff[i] = arith_basket_payoff_put
#             # geo_basket_payoff_put = math.exp(-r * T) * max(geo_K - geo_basket_mean, 0)
#             geo_basket_payoff_put = exp(-r * T) * max(K - geo_basket_mean, 0)
#             geo_basket_payoff[i] = geo_basket_payoff_put
#
# ,
#     if method == "standard":
#         # Standard Monte Carlo
#         pmean = numpy.mean(arith_basket_payoff)
#         pstd = numpy.std(arith_basket_payoff)
#         confmc = (pmean - 1.96 * pstd / sqrt(path_num), pmean + 1.96 * pstd / sqrt(path_num))
#         return pmean, confmc
#
#     elif method == "control variate":
#         # Control Variate
#         # covxy = numpy.mean([x * y for x, y in zip(geo_basket_payoff, arith_basket_payoff)]) - numpy.mean(
#         #     arith_basket_payoff) * numpy.mean(geo_basket_payoff)
#         covxy = numpy.mean(arith_basket_payoff * geo_basket_payoff) - numpy.mean(arith_basket_payoff) * numpy.mean(
#             geo_basket_payoff)
#         theta = covxy / numpy.var(geo_basket_payoff)
#
#         # Control Variate Version
#         geo = geometric_basket_option(S1, S2, sigma1, sigma2, r, T, K, ro, option_type)
#         # z = [x + y for x, y in zip(arith_basket_payoff, map(lambda x: theta * (geo - x), geo_basket_payoff))]
#         z = arith_basket_payoff + theta * (geo - geo_basket_payoff)
#         zmean = numpy.mean(z)
#         zstd = numpy.std(z)
#         zconfvc = (zmean - 1.96 * zstd / math.sqrt(path_num), zmean + 1.96 * zstd / math.sqrt(path_num))
#         return zmean, zconfvc
#
# def geometric_basket_option(S1, S2, sigma1, sigma2, r, T, K, rou, option_type):
#     bg0 = sqrt(S1 * S2)
#     sigma_bg = sqrt(sigma1 * sigma1 + sigma1 * sigma2 * rou + sigma2 * sigma1 * rou + sigma2 * sigma2) / 2
#     miu_bg = r - 0.5 * (sigma1 * sigma1 + sigma2 * sigma2) / 2 + 0.5 * sigma_bg * sigma_bg
#
#     d1 = (log(bg0 / K) + (miu_bg + 0.5 * sigma_bg ** 2) * T) / (sigma_bg * sqrt(T))
#     d2 = d1 - sigma_bg * sqrt(T)
#
#     if option_type == 'call':
#         value = exp(-r * T) * (bg0 * exp(miu_bg * T) * stats.norm.cdf(d1) - K * stats.norm.cdf(d2))
#     elif option_type == 'put':
#         value = exp(-r * T) * (K * stats.norm.cdf(-d2) - bg0 * exp(miu_bg * T) * stats.norm.cdf(-d1))
#     return value
