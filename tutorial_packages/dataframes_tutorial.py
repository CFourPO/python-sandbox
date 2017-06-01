import pandas as pd

dict = {
  "first": ["Chris", "Tommy", "alex", "Jarrod"],
  "last": ["Smith", "Bart", "Trebek", "Subway"],
  "city": ["New York", "Boston", "Pheonix", "Istanbul"],
  "score": [90, 85, 99, 78],
  "fav_movie": ["The Outsiders", "Pirates of the Carribean", "Harry Potter", "Elf"]
}

ind = 0
names = []
firsts = dict['first']
lasts = dict['last']
for i in dict['first']:
    full_name = lasts[ind] + ', ' + firsts[ind]
    names.append(full_name)
    ind += 1

df = pd.DataFrame(dict)

df.index = names
print("DataFrame:\n %s" % df)
