import pandas as pd
import json

obj ="""
{
    "name":"wes",
    "place_lived":["United States","Spain","Germany"],
    "siblings" :[{"name":"scott","age":25,"pet":"zuko"}]
}
"""


data = json.loads(obj)
print(data)
print(type(data))
print()
print(data["siblings"])
print()

frame = pd.DataFrame(data['siblings'])
print(frame)
