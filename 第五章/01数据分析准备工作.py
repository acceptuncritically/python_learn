import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
df=pd.read_csv("csv_data/电影数据_100条.csv")
figure,axes=plt.subplots(nrows=2, ncols=2, figsize=(20,6),dpi=100)

