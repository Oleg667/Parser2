import pandas as pd


df = pd.DataFrame({
                    'Cod': ['1'],
                    'NAME SKU': ['2'],
                    'Prise in website': ['3'],
                    'recommended retail price list': ['4'],
                    'comparison': ['5']
                   })

df.to_excel('./bafus.xlsx', index=False)


