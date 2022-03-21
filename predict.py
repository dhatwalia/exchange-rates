# Predicts the exchange rates
from pandas import *
import matplotlib.pyplot as plt
import seaborn as sns
from autots import AutoTS

sns.set()
plt.style.use('seaborn-whitegrid')

# Load the data
data = read_csv('rates.csv')
data['date'] = to_datetime(data['date'])

# Predict the foreign exchange rate


def forecast_rate(currency, days):
    # Build the model
    model = AutoTS(forecast_length=days, frequency='infer',
                   ensemble='simple', model_list='superfast')
    model = model.fit(data, date_col='date', value_col=currency)

    # Predict the result
    prediction = model.predict()
    forecast = prediction.forecast

    return forecast


# Initial variables
days = 100

# Plot the forecast results
plt.figure(figsize=(10, 4))
plt.title('Foreign exchange price prediction')
plt.xlabel('Date')
plt.ylabel('Price')

cad = forecast_rate('CAD', days)
print('CAD/INR prediction for next', days, 'days:\n', cad)
plt.plot(cad)

# usd = forecast_rate('USD', days)
# print('USD/INR prediction for next', days, 'days:\n', usd)
# plt.plot(usd)

# eur = forecast_rate('EUR', days)
# print('EUR/INR prediction for next', days, 'days:\n', eur)
# plt.plot(eur)

# gbp = forecast_rate('GBP', days)
# print('GBP/INR prediction for next', days, 'days:\n', gbp)
# plt.plot(gbp)

plt.savefig('forecast.png')
