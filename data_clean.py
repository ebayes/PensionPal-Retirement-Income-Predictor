import pandas as pd
import numpy as np
import calendar
from datetime import datetime

# Define LinkedIn data as dict
data = {'MonthYear1': ['Apr-2015', 'Mar-2017'],
                'MonthYear2': ['Apr-2017', 'Mar-2019'],
                'Role': ['Policy Adviser', 'Senior Policy Adviser'],
                'Company': ['HM Treasury', 'Mayor of London'],
                'Country': ['UK', 'UK']}

# Convert the dict into DataFrame
df = pd.DataFrame(data, columns = ['MonthYear1', 'MonthYear2', 'Role', 'Company', 'Country'])

print(df)

# convert months to numbers
monthMap = dict((v,k) for k,v in enumerate(calendar.month_abbr))
df.StartMonth = df.StartMonth.map(monthMap)
df.EndMonth = df.EndMonth.map(monthMap)

# convert into dates
df['date1'] = pd.to_datetime(df[['StartYear', 'StartMonth']].assign(DAY=1))
df['date2'] = pd.to_datetime(df[['EndYear', 'EndMonth']].assign(DAY=1))

# count months
df['months'] = ((df.date2 - df.date1)/np.timedelta64(1, 'M'))
df['months'] = df['months'].astype(int)

print(df)
