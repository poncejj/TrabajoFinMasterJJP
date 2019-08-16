from datetime import date, timedelta
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import LSTM
from keras import callbacks
from keras.callbacks import ModelCheckpoint

#Returns the timespan from a date
def get_timespan(df, dt, minus, periods, freq='D'):
    return df[pd.date_range(dt - timedelta(days=minus), periods=periods, freq=freq)]

#Return a dataset of values that are going to be used in the LTSM network.
#The first unit sales value of the date in 2017
#The mean of the unit sales in the last 3 days and the next 3 days from the date
#The mean of the unit sales in the last 7 days and the next 7 days from the date
#The mean of the unit sales in the last 14 days and the next 14 days from the date
#The mean of the unit sales in the last 30 days and the next 30 days from the date
#The mean of the unit sales in the last 60 days and the next 60 days from the date
#The mean of the unit sales in the last 140 days and the next 140 days from the date
#The sum of the unit sales in the last 14 days and the next 14 days from the date
#The sum of the unit sales in the last 60 days and the next 60 days from the date
#The sum of the unit sales in the last 140 days and the next 140 days from the date

def prepare_dataset(t2017, df_2017, is_train=True):
    X = pd.DataFrame({
        "day_1_2017": get_timespan(df_2017, t2017, 1, 1).values.ravel(),
        "mean_3_2017": get_timespan(df_2017, t2017, 3, 3).mean(axis=1).values,
        "mean_7_2017": get_timespan(df_2017, t2017, 7, 7).mean(axis=1).values,
        "mean_14_2017": get_timespan(df_2017, t2017, 14, 14).mean(axis=1).values,
        "mean_30_2017": get_timespan(df_2017, t2017, 30, 30).mean(axis=1).values,
        "mean_60_2017": get_timespan(df_2017, t2017, 60, 60).mean(axis=1).values,
        "mean_140_2017": get_timespan(df_2017, t2017, 140, 140).mean(axis=1).values,
        "promo_14_2017": get_timespan(promo_2017, t2017, 14, 14).sum(axis=1).values,
        "promo_60_2017": get_timespan(promo_2017, t2017, 60, 60).sum(axis=1).values,
        "promo_140_2017": get_timespan(promo_2017, t2017, 140, 140).sum(axis=1).values
    })
    for i in range(7):
        X['mean_4_dow{}_2017'.format(i)] = get_timespan(df_2017, t2017, 28-i, 4, freq='7D').mean(axis=1).values
        X['mean_20_dow{}_2017'.format(i)] = get_timespan(df_2017, t2017, 140-i, 20, freq='7D').mean(axis=1).values
    for i in range(16):
        X["promo_{}".format(i)] = promo_2017[
            t2017 + timedelta(days=i)].values.astype(np.uint8)
    if is_train:
        y = df_2017[
            pd.date_range(t2017, periods=16)
        ].values
        return X, y
    return X


def generateModel():
    #Load the train data from the file, but only the sales from 1/1/2016
    df_train = pd.read_csv(os.path.join(settings.LOCAL_BDD, "train.csv"), usecols=[1, 2, 3, 4, 5],dtype={'onpromotion': bool},converters={'unit_sales': lambda u: np.log1p(float(u)) if float(u) > 0 else 0},parse_dates=["date"],skiprows=range(1, 66458909))
    #Load the test data from the file, 
    df_test = pd.read_csv(os.path.join(settings.LOCAL_BDD, "test.csv"), usecols=[0, 1, 2, 3, 4],dtype={'onpromotion': bool},parse_dates=["date"]).set_index(['store_nbr', 'item_nbr', 'date'])
    #Filter the data from 1/1/2017
    df_2017 = df_train.loc[df_train.date>=pd.datetime(2017,1,1)]
    del df_train

    #The data is cleaned, in the field of on promotion, 
    promo_2017_train = df_2017.set_index(
        ["store_nbr", "item_nbr", "date"])[["onpromotion"]].unstack(
            level=-1).fillna(False)
    #Set the name of all the columns, of the train data
    promo_2017_train.columns = promo_2017_train.columns.get_level_values(1)

    #Clean the data from the test, and remove the last value
    promo_2017_test = df_test[["onpromotion"]].unstack(level=-1).fillna(False)

    #Set the name of all the columns, of the train data
    promo_2017_test.columns = promo_2017_test.columns.get_level_values(1)

    #Re index the test data, to continue from the train data
    promo_2017_test = promo_2017_test.reindex(promo_2017_train.index).fillna(False)

    #Concat the train and the test data
    promo_2017 = pd.concat([promo_2017_train, promo_2017_test], axis=1)
    del promo_2017_test, promo_2017_train

    #Clean the data in the field unit sales put 0 if is null
    df_2017 = df_2017.set_index(
        ["store_nbr", "item_nbr", "date"])[["unit_sales"]].unstack(
            level=-1).fillna(0)
    df_2017.columns = df_2017.columns.get_level_values(1)

    #Get the items that apear in 2017
    items = Item.objects.filter(item_nbr__in = df_2017.index.get_level_values(1))

    print("Preparing dataset...")
    t2017 = date(2017, 5, 31)
    X_l, y_l = [], []
    for i in range(6):
        delta = timedelta(days=7 * i)
        X_tmp, y_tmp = prepare_dataset(
            t2017 + delta, df_2017
        )
        X_l.append(X_tmp)
        y_l.append(y_tmp)
    X_train = pd.concat(X_l, axis=0)
    y_train = np.concatenate(y_l, axis=0)
    del X_l, y_l
    X_val, y_val = prepare_dataset(date(2017, 7, 26), df_2017)
    X_test = prepare_dataset(date(2017, 8, 16), df_2017, is_train=False)

    stores_items = pd.DataFrame(index=df_2017.index)
    test_ids = df_test[['id']]

    items = items.reindex( stores_items.index.get_level_values(1) )

    X_train = X_train.as_matrix()
    X_test = X_test.as_matrix()
    X_val = X_val.as_matrix()
    X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
    X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))
    X_val = X_val.reshape((X_val.shape[0], 1, X_val.shape[1]))

    model = Sequential()
    model.add(LSTM(32, input_shape=(X_train.shape[1],X_train.shape[2])))
    model.add(Dropout(.1))
    model.add(Dense(32))
    model.add(Dropout(.2))
    model.add(Dense(1))
    model.compile(loss = 'mse', optimizer='adam', metrics=['mse'])

    N_EPOCHS = 5

    val_pred = []
    test_pred = []
    # wtpath = 'weights.hdf5'  # To save best epoch. But need Keras bug to be fixed first.
    sample_weights=np.array( pd.concat([items["perishable"]] * 6) * 0.25 + 1 )
    for i in range(16):
        print("=" * 50)
        print("Step %d" % (i+1))
        print("=" * 50)
        y = y_train[:, i]
        xv = X_val
        yv = y_val[:, i]
        model.fit(X_train, y, 
                  batch_size = 512, 
                  epochs = N_EPOCHS, 
                  verbose=2, 
                  sample_weight=sample_weights, 
                  validation_data=(xv,yv), 
                  callbacks = [ModelCheckpoint("model.hdf5", save_best_only=True, period=3)] ) 
        val_pred.append(model.predict(X_val))
        test_pred.append(model.predict(X_test))
        
    n_public = 5 # Number of days in public test set
    weights=pd.concat([items["perishable"]]) * 0.25 + 1
    print("Unweighted validation mse: ", mean_squared_error(
        y_val, np.array(val_pred).squeeze(axis=2).transpose()) )
    print("Full validation mse:       ", mean_squared_error(
        y_val, np.array(val_pred).squeeze(axis=2).transpose(), sample_weight=weights) )
    print("'Public' validation mse:   ", mean_squared_error(
        y_val[:,:n_public], np.array(val_pred).squeeze(axis=2).transpose()[:,:n_public], 
        sample_weight=weights) )
    print("'Private' validation mse:  ", mean_squared_error(
        y_val[:,n_public:], np.array(val_pred).squeeze(axis=2).transpose()[:,n_public:], 
        sample_weight=weights) )
        
    y_test = np.array(test_pred).squeeze(axis=2).transpose()
    df_preds = pd.DataFrame(
        y_test, index=stores_items.index,
        columns=pd.date_range("2017-08-16", periods=16)
    ).stack().to_frame("unit_sales")
    df_preds.index.set_names(["store_nbr", "item_nbr", "date"], inplace=True)

    submission = test_ids.join(df_preds, how="left").fillna(0)
    submission["unit_sales"] = np.clip(np.expm1(submission["unit_sales"]), 0, 1000)
    submission.to_csv('lstm.csv', float_format='%.4f', index=None)

def predictSales(predict_date, df_2017):
    model = model.load(os.path.join(settings.LOCAL_BDD, "model.hdf5"))
    X_test = prepare_dataset(predict_date, df_2017 is_train=False)
    X_test = X_test.as_matrix()
    X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))
