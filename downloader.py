import pandas as pd
import requests
import os


#path to current folder
root_folder = '/Users/syn/PycharmProjects/pythonProject2/pokemons_images/'
im_extension = '.jpg'


#path to csv
df = pd.read_csv('/Users/syn/PycharmProjects/pythonProject2/pokemon.csv')


print(df.columns.values)


def download(row):
    _name = str(row.name) + im_extension
    print(_name)
    filename = os.path.join(root_folder,
                            '_'.join([row['pokemon'],
                                      row['type'],
                                     _name]))

    print(filename)

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    url = row.image
    print(f"Downloading {url} to {filename}")
    r = requests.get(url, allow_redirects=True)
    with open(filename, 'wb') as f:
        f.write(r.content)


df.apply(download, axis=1)