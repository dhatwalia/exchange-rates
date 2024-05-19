# Keeps the rates.csv file updated
from pandas import *
from pyvalet import ValetInterpreter

# Fetch the data using Valet API
vi = ValetInterpreter()

# Step 1: Get all foreign exchange rates
# CAD to INR
cad_inr = vi.get_series_observations('FXCADINR', response_format='csv')
dates = cad_inr.date
cad_inr = cad_inr.FXCADINR.astype(float)

# USD to CAD
usd_cad = vi.get_series_observations('FXUSDCAD', response_format='csv')
usd_cad = usd_cad.FXUSDCAD.astype(float)

# EUR to CAD
eur_cad = vi.get_series_observations('FXEURCAD', response_format='csv')
eur_cad = eur_cad.FXEURCAD.astype(float)

# GBP to CAD
gbp_cad = vi.get_series_observations('FXGBPCAD', response_format='csv')
gbp_cad = gbp_cad.FXGBPCAD.astype(float)

# Step 2: Covert and round all currencies to INR
# USD to INR
usd_inr = round(usd_cad * cad_inr, 2)

# USD to INR
eur_inr = round(eur_cad * cad_inr, 2)

# USD to INR
gbp_inr = round(gbp_cad * cad_inr, 2)

# Round CAD to INR
cad_inr = round(cad_inr, 2)

print('************************ Statistics ************************\n')
print('Today\'s exchange rate \t\t= $', max(cad_inr[-1:]))
print('Highest of the last 10 days \t= $', max(cad_inr[-10:]))
print('Highest of the last 1 month \t= $', max(cad_inr[-30:]))
print('Highest of the last 1 year \t= $', max(cad_inr[-365:]))
print('Highest of the last 5 year \t= $', max(cad_inr[-365*5:]))
print('\n************************************************************\n')

# Step 3: Merge the data
merged = concat([dates, cad_inr, usd_inr, eur_inr, gbp_inr], axis=1)
merged.columns = ['date', 'CAD', 'USD', 'EUR', 'GBP']

# Step 4: Write to file
merged.to_csv('rates.csv', index=False)
