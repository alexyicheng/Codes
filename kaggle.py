import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

path = 'C:/Users/alexyang/Desktop/input/'

train = pd.read_csv(path+'sales_train_V2.csv')
items = pd.read_csv(path+'items.csv')
test = pd.read_csv(path+'test.csv')

train['date'] = pd.to_datetime(train['date'],format = '%d.%m.%Y')

train = train[train['item_cnt_day']<2000 ]
train = train[train['item_price']<300000]
price_correction = train[(train['shop_id']==32)&(train['item_id']==2973)&(train['date_block_num']==4)&(train['item_price']>0)].item_price.median()
train.loc[train['item_price']<0,'item_price'] = price_correction

train.loc[train['shop_id']==0,'shop_id']=57
test.loc[test['shop_id']==0, 'shop_id']=57

train.loc[train['shop_id']==1,'shop_id']=58
test.loc[test['shop_id']==1, 'shop_id']=58

train.loc[train['shop_id']==10,'shop_id']=11
test.loc[test['shop_id']==10, 'shop_id']=11


dataset = train.pivot_table(index = ['item_id','shop_id'],values = ['item_cnt_day'],columns = 'date_block_num', fill_value = 0)

dataset = dataset.reset_index()
dataset = pd.merge(test, dataset, on=['item_id', 'shop_id'], how='left')
dataset = dataset.fillna(0)
dataset = dataset.drop(['shop_id','item_id','ID'],axis = 1)

X_train = np.expand_dims(dataset.values[:,:-1],axis = 2)
y_train = dataset.values[:,-1:]

X_test = np.expand_dims(dataset.values[:,1:],axis = 2)

model = Sequential()
model.add(LSTM(units = 64, input_shape = (33,1)))
model.add(Dropout(0.3))
model.add(Dense(1))
model.compile(loss ='mse',optimizer='adam',metrics=['mean_squared_error'])
model.summary()

history = model.fit(X_train,y_train,batch_size=4096,epochs=10)

LSTM_prediction = model.predict(X_test)
LSTM_prediction = LSTM_prediction.clip(0,20)

erg = pd.DataFrame({'ID':test['ID'],'item_cnt_month':LSTM_prediction.ravel()})
erg.to_csv('erg.csv',index=False)