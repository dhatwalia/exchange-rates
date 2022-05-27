# Keeps the rates.csv file updated
from pandas import *
from pyvalet import ValetInterpreter

# Fetch the data using Valet API
vi = ValetInterpreter()

# Step 1: Get all foreign exchange rates
# CAD to INR
_, cad_inr = vi.get_series_observations('FXCADINR')
dates = cad_inr.loc[3:]['id']
cad_inr = cad_inr.loc[3:]['label'].astype(float)

# USD to CAD
_, usd_cad = vi.get_series_observations('FXUSDCAD')
usd_cad = usd_cad.loc[3:]['label'].astype(float)

# EUR to CAD
_, eur_cad = vi.get_series_observations('FXEURCAD')
eur_cad = eur_cad.loc[3:]['label'].astype(float)

# GBP to CAD
_, gbp_cad = vi.get_series_observations('FXGBPCAD')
gbp_cad = gbp_cad.loc[3:]['label'].astype(float)

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
print('\n************************************************************\n')

# Step 3: Merge the data
merged = concat([dates, cad_inr, usd_inr, eur_inr, gbp_inr], axis=1)
merged.columns = ['date', 'CAD', 'USD', 'EUR', 'GBP']

# Step 4: Write to file
merged.to_csv('rates.csv', index=False)
