# Loads the foreign exchange rates
from pandas import *
import matplotlib.pyplot as plt
from autots import AutoTS

plt.style.use('seaborn-v0_8-darkgrid')

# Load the data
data = read_csv('rates.csv')
data['date'] = to_datetime(data['date'])

# Predict the foreign exchange rate
def forecast_rate(currency, days=10):
    # Build the model
    model = AutoTS(forecast_length=days, frequency='infer',
                   ensemble='simple', model_list='superfast', verbose=0)
    model = model.fit(data, date_col='date', value_col=currency)

    # Predict the result
    prediction = model.predict()
    forecast = prediction.forecast

    return forecast

# Plot the forecast results
plt.figure(figsize=(10, 4))
plt.title('Foreign exchange price prediction')
plt.xlabel('Date')
plt.ylabel('Price')

cad = forecast_rate('CAD')
print('CAD/INR prediction for next few days:\n', cad)
plt.plot(cad)

# usd = forecast_rate('USD')
# print('USD/INR prediction for next few days:\n', usd)
# plt.plot(usd)

# eur = forecast_rate('EUR')
# print('EUR/INR prediction for next few days:\n', eur)
# plt.plot(eur)

# gbp = forecast_rate('GBP')
# print('GBP/INR prediction for next few days:\n', gbp)
# plt.plot(gbp)

plt.savefig('forecast.png')
