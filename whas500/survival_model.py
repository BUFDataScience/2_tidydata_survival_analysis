import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from lifelines.estimation import KaplanMeierFitter, CoxPHFitter

matplotlib.style.use('ggplot')

df = pd.read_csv('data/whas500.csv')

# print(df.head())

print(df['lenfol'].describe())

# look at how long a patient lives
dead = df[df['fstat'] > 0]
dead.hist(bins=20, column='lenfol')
plt.show()

#plot the cumulative hazard (cdf)
dead.hist(bins=100, column='lenfol',
          cumulative=True, normed=1)
plt.show()

#plot survival curve
kaplen_meier = KaplanMeierFitter()
time_of_event = df['lenfol'];
event = df['fstat'];
time = np.linspace(0, 2500, 100)

kaplen_meier.fit(time_of_event, timeline=time, event_observed=event, label='All patients')
kaplen_meier.plot()
plt.show()

#stratify Congestive Heart Complications
history = df['chf'] == 1;

kaplen_meier = KaplanMeierFitter()
kaplen_meier.fit(time_of_event[history], timeline=time, event_observed=event[history], label='Congestive heart complications')
ax = kaplen_meier.plot()

kaplen_meier.fit(time_of_event[~history], timeline=time, event_observed=event[~history], label='No congestive heart complications')
kaplen_meier.plot(ax=ax, c="b")

plt.show()

#Cox proportional hazard
ph_data = df[["fstat", "lenfol", "bmi", "age"]]

ph = CoxPHFitter()
ph.fit(ph_data, 'lenfol', event_col='fstat')
ph.print_summary()

print(ph.baseline_hazard_.head())

#use predict_survival_function to get probability
x = ph_data[ph_data.columns.difference(['lenfol', 'fstat'])].ix[23:25]
print(x)
ph.predict_survival_function(x).plot()
plt.show()