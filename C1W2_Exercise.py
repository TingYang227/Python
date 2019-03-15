import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.5})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Store 1', 'Store 1', 'Store 2'])

print(df)
# print("The tpy of df is: ", type(df))
# print("The length of df is:", len(df))


animals = ['Tiger', 'Bear', 'Mosse']
print(pd.Series(animals))

numbers = [1, 2, 3]
print(pd.Series(numbers))