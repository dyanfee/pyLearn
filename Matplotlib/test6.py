import pandas as pd

data = pd.read_csv('./Matplotlib/data.csv')
print(data)
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
#         {'a': 100, 'b': 200, 'c': 300, 'd': 400},
#         {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]

# data = pd.DataFrame(data)

# for i in range(len(data)):
#     # data.iloc[i, 2] = (data.iloc[i, 2]-data.iloc[i, 6])/data.iloc[i, 6]
#     # data.ix[i]['open'] = (data.ix[i]['open']-data.ix[i]['pre_close'])/data.ix[i]['pre_close']
#     # data.ix[i]['high'] = (data.ix[i]['high']-data[i]['pre_close'])/data[i]['pre_close']
#     # data.ix[i]['low'] = (data[i]['low'] - data[i]['pre_close']) / data[i]['pre_close']
#     # data.ix[i]['close'] = (data.ix[i]['close'] - data[i]['pre_close']) / data[i]['pre_close']
#     # data.ix[i]['vol'] = log(data[i]['vol'] / data[i+1]['vol'])
#     # data.ix[i]['amount'] = log(data[i]['amount'] / data[i+1]['amount'])
#     # return data

data['res1'] = (data["low"] - data["pre"])/data['height']
data.eval('res2 = (height - low) / pre', inplace=True)
data.convert_objects(convert_numeric=True)
pd.to_numeric
print(data)
data.info()
