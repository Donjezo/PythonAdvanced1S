import   pandas as pd

produktet = ["Molla","Banane","Protokajt","Rrushi"]

sales = [150,20,180,90]


sales_series = pd.Series(sales, index=produktet)

print(sales_series)


print(sales_series["Molla"])


shitejetTotale = sales_series.sum()

print(shitejetTotale)

shitjaMaEMadhe = sales_series.idxmax()

print(f"Shitje me se shumti ka pasur :{shitjaMaEMadhe}")