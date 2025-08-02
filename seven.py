# Pandasd
# Series    - 1D
# Data Frame - 2D

# import numpy as np
# import pandas as pd

# data = [10, 20, 30, 40, 50]

# print(data)

# arr = np.array(data)

# print(arr)

# ser = pd.Series(data)
# print(ser)

# df = pd.DataFrame(arr)
# print(df)

# arr = np.array(data)
# print(arr)

# ser = pd.Series(data)
# print(ser)

# df = pd.DataFrame(arr)
# print(df)


# dataset = {"SiNo": [1,2,3,4,5], "Name": ["Arun", "kumar", "kannan", "Ganesh", "Vignesh"], "Age": [21, 23, 45, 43, 21], "Place": ["Nagercoil", "Maduri", "Trichy", "Salam", "Coimbatore"]}
# df1 = pd.DataFrame(dataset)
# print(df1)


# -------------------------------------------------

# import pandas as pd

# data = {"SINO" : [1, 2, 3, 4, 5],
#         "Name" : ["Arun", "Kumar", "Kannan", "Senthil", "Raja", ],
#         "Dept" : ["Computer", "Civil", "Mech", "ECE", 'EEE'],
#         "Year" : ["Second", "Final", "Third", "First", "Second"],
#         "Marks": [490, 450, 430, 390, 385]
#         }

# df = pd.DataFrame(data)
# print(df)
# print()

# # Slicing the data 
# print(df[["Name", "Marks"]])
# print()
# print(df[["SINO", "Name", "Dept"]])

# -------------------------------


# import pandas as pd
# import numpy as np

# data = {
#     "SINO" : [1, 2, 3, 4, 5],
#     "Sub_M1" : [89, 67, 87, 89, 98],
#     "Sub_M2" : [76, np.nan, 66, 67, 89],
#     "Sub_M3" : [87, 68, 45, np.nan, 66],
#     "Sub_M4" : [56, 77, 56, 85, 98]
# }

# df = pd.DataFrame(data)
# print(df)
# print()
# print(df.isnull)

# print()
# print(df.fillna(0))

# print()
# print(df.dropna())
# ----------------------------------------------------

# Working with series items and function

# import pandas as pd

# data = pd.Series(["Apple", "Orange", "Banana", "Pine", "Jack", "Fruit123@info"
#                   ])

# print(data)

# print(data.str.len())

# -----------------------------------------------------
# import pandas as pd

# data = pd.Series(["APPle", "OraNGe", "BaNAna", "PiNe", "JACk", "FrUIt123@info"
#                   ])

# print(data)
# print()
# print(data.str.upper())
# print()
# print(data.str.lower())
# --------------------------------------------------------------------------------------

# import pandas as pd

# data = pd.Series(["Apple", "Orange", "Banana", "Pine", "Jack", "Fruit123@info"
#                   ])

# print(data)
# #case sensitive
# print()
# print(data.str.startswith("A"))
# print()
# print(data.str.startswith("P"))
# print()
# print(data.str.endswith('e'))
# print()
# print(data.str.endswith('ana'))

# -------------------------------------------------------

# import pandas as pd

# data = pd.Series(["  Apple   ", "   Orange   ", "Banana", "Pine", "     Jack    ", "Fruit123@info"
#                   ])

# print(data)
# print()
# print(data.str.len())
# print()

# str1 = data.str.strip()
# print(str1)
# print()
# print(str1.str.len())
# -------------------------------------------------------------
import pandas as pd

data = pd.Series(["Apple", "Orange", "Banana", "Pine", "Jack", "Fruit123@info"])

print(data)
print()
print(data.str.split())


