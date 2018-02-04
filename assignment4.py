
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys, os
from datetime import datetime
import time

os.chdir(r"F:\pythonGames\PythonGames\Intro - Python Plotting")

#my datasets - load and clean
we = pd.read_csv(r"data\london2014dailyWeather.csv") #generated by another python file from DarkSKy API
we.columns = ['time', 'mon', 'day', 'hour', 'apparentTemperatureHigh',
       'apparentTemperatureLow', 'precipType', 'icon', 'humidity',
       'windSpeed']
#new column with time
we['date'] = pd.to_datetime(we['time'], unit='d')
we['date'] = we['date'].apply( lambda x: x.replace(hour=0, minute=0) ) #here we clear dates to 0 hour

bi = pd.read_csv(r"data\bicyclesRentalsDaily.csv") #generated by another python file from London TFL
bi.columns = ['day', 'Duration', 'Rental Id']
bi = bi[2:]
#here (after 3 hours of fight) we change our dates to python
bi['date2'] = bi['day'].apply(datetime.strptime, args=('%d/%m/%Y',))

df = pd.merge (we, bi, how = 'inner', left_on = 'date', right_on = "date2")
df['av_duration_min'] = pd.to_numeric(df['Duration'])/ pd.to_numeric(df['Rental Id'])/60
df['rental'] = df['Rental Id']
columns = ['time', 'mon', 'day_x', 'hour','date_x', 'day_y','Duration','date_y', 'Rental Id']
df.drop(columns, inplace=True, axis=1)

### plotting ###

dates = np.array(df.date2, dtype='datetime64[D]')
plt.plot(dates, df['windSpeed'], "-r", dates, df['rental'], "-b", alpha=0.4)