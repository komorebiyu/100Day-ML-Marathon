#!/usr/bin/env python
# coding: utf-8

# ## 練習時間
# #### 請寫一個函式用來計算 Mean Square Error
# $ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $
# 
# ### Hint: [如何取平方](https://googoodesign.gitbooks.io/-ezpython/unit-1.html)

# # [作業目標]
# - 仿造範例的MAE函數, 自己寫一個MSE函數(參考上面公式)

# # [作業重點]
# - 注意程式的縮排
# - 是否能將數學公式, 轉換為 Python 的函式組合? (In[2], Out[2])

# In[10]:


# 載入基礎套件與代稱
import numpy as np
import matplotlib.pyplot as plt


# In[29]:


def mean_absolute_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

# 定義 mean_squared_error 這個函數, 計算並傳回 MSE
def mean_squared_error(y,yp):
    """
    請完成這個 Function 後往下執行
    """
    mse = MSE = sum((abs(y - yp) ** 2))/ len(y)
    return mse


# In[30]:


# 與範例相同, 不另外解說
w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[31]:


# 與範例相同, 不另外解說
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[32]:


# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))


# # [作業2]
# 
# 請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：
# https://www.kaggle.com/ronitf/heart-disease-uci
# 
# 1. 你選的這組資料為何重要
# 可藉此筆資料分析哪謝因素會影響心臟病患者的疾病風險
# 
# 2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
# 資料由克里夫蘭醫學中心Cleveland Clinic Foundation蒐集，移除病患的姓名及身分證號碼後發表在UCI Machine Learning Repository。
# 
# 3. 蒐集而來的資料型態為何
# 有14個欄位與303筆資料的表格。
# 
# 4. 這組資料想解決的問題如何評估
# 能否成功定義出疾病風險較高的人群。
# 
# 
# 
# 
# # [作業3]
# 
# 想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：
# 
# 1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
# 業績 = 車隊車輛數 * 營業時數 * 每小時接單數 * 每筆訂單價格
# 車隊車輛、營運時數、每筆單價在現行法規及投資下暫時無法改變。
# 提升業績應由增加接單數下手。
# 假設將車子配置在合適的地點能增加接單量。
# 
# 2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
# 初步先由公司內部現有接單狀況開始分析並進行優化，包含時間、地點、人數、需求等。
# 
# 3. 蒐集而來的資料型態為何
# 包含公司現有訂單狀況的資料集表格。
# 
# 4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
# 根據分析結果進行小規模實驗確認。
# 
