import pandas as pd

df=pd.DataFrame({1:{'Acct':99, 'Eco':94, 'Eng':95, IP':94, 'Maths':97},2:{'Acct':94, 'Eco':94, 'Eng':89, 'IP':87, 'Maths':100}, 3:{'Acct':81, 'Eco':72,'Eng': 71, 'IP':79,'Maths':65}, 4:{'Acct':70,'Eco':67, 'Eng':69, 'IP':65, 'Maths':69}, 5:{'Acct':88,'Eco':82, 'Eng':32, 'IP':89,'Maths':86}, 6:{'Acct':79,'Eco':81, 'Eng': 79, 'IP':81, 'Maths':84}, 7:{'Acct':41,'Eco': 36, 'Eng':51, 'IP':42, 'Maths':40}, 8:{'Acct':61, 'Eco':54, 'Eng':60, 'IP':63, 'Maths':55}, 9:{'Acct':42, 'Eco':42,'Eng':45, 'IP':43,'Maths':40}, 10:{'Acct':68,'Eco':67, 'Eng':66, 'IP':64, 'Maths':69}})
print(df)
print(df.describe())
