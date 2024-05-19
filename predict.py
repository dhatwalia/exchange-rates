# Loads the foreign exchange rates
from datetime import datetime, timedelta
from pandas import *
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the data
data = read_csv('rates.csv')
data['date'] = to_datetime(data['date'])

# Predict the foreign exchange rate
def forecast_rate(currency, days=10):
    # Filter data for the specified currency
    currency_data = data[['date', currency]].copy()

    # Build the model
    model = LinearRegression()
    model.fit([[d.timestamp()] for d in currency_data['date']], currency_data[currency])

    # Predict the result
    # Note: We are not predict today's price
    next_days = [datetime.now() + timedelta(days=i) for i in range(1, days+1)]
    forecast = model.predict([[d.timestamp()] for d in next_days])

    # Round the result
    return [round(x, 2) for x in forecast]

# Plot the forecast results
plt.figure(figsize=(10, 4))
plt.title('Foreign exchange price prediction')
plt.xlabel('Date')
plt.ylabel('Price')

cad = forecast_rate('CAD')
print('CAD/INR prediction for next few days:\n', cad)
plt.plot(cad, label='CAD')

# usd = forecast_rate('USD')
# print('USD/INR prediction for next few days:\n', usd)
# plt.plot(usd, label='USD')

# eur = forecast_rate('EUR')
# print('EUR/INR prediction for next few days:\n', eur)
# plt.plot(eur, label='EUR')

# gbp = forecast_rate('GBP')
# print('GBP/INR prediction for next few days:\n', gbp)
# plt.plot(gbp, label='GBP')

plt.legend()
plt.savefig('forecast.png')
