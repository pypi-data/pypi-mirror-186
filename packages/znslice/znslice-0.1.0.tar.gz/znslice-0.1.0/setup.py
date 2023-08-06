# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['znslice']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'znslice',
    'version': '0.1.0',
    'description': 'Cache, advanced slicing and lazy loading for __getitem__',
    'long_description': '# ZnSlice\n\nA lightweight library  (without external dependencies) for:\n- advanced slicing.\n- cache `__getitem__(self, item)`\n- lazy load `__getitem__(self, item)`\n\n# Installation\n\n```bash\npip install znslice\n```\n\n# Usage\n\n## Advanced Slicing and Cache\n```python\nimport znslice\nimport collections.abc\n\nclass MapList(collections.abc.Sequence):\n    def __init__(self, data, func):\n        self.data = data\n        self.func = func\n    \n    @znslice.znslice\n    def __getitem__(self, item: int):\n        print(f"Loading item = {item}")\n        return self.func(self.data[item])\n    \n    def __len__(self):\n        return len(self.data)\n\ndata = MapList([0, 1, 2, 3, 4], lambda x: x ** 2)\n\nassert data[0] == 0\nassert data[[1, 2, 3]] == [1, 4, 9]\n# calling data[:] will now only compute data[4] and load the remaining data from cache\nassert data[:] == [0, 1, 4, 9, 16]\n```\n\n## Lazy Database Loading\n\nYou can use `znslice` to lazy load data from a database. This is useful if you have a large database and only want to load a small subset of the data.\n\nIn the following we will use the `ase` package to generate `Atoms` objects stored in a database and load them lazily.\n\n```python \nimport ase.io\nimport ase.db\nimport znslice\nimport tqdm\nimport random\n\n# create a database\nwith ase.db.connect("data.db", append=False) as db:\n    for _ in range(10):\n        atoms = ase.Atoms(\'CO\', positions=[(0, 0, 0), (0, 0, random.random())])\n        db.write(atoms, group="data")\n        \n# load the database lazily\nclass ReadASEDB:\n    def __init__(self, file):\n        self.file = file\n    \n    @znslice.znslice(\n        advanced_slicing=True, # this getitem supports advanced slicingn\n        lazy=True # we want to lazy load the data\n    )\n    def __getitem__(self, item):\n        data = []\n        with ase.db.connect(self.file) as database:\n            if isinstance(item, int):\n                print(f"get {item = }")\n                return database[item + 1].toatoms()\n            for idx in tqdm.tqdm(item):\n                data.append(database[idx + 1].toatoms())\n        return data\n            \n    def __len__(self):\n        with ase.db.connect(self.file) as db:\n            return len(db)\n\ndb = ReadASEDB("data.db")\n\ndata = db[::2] # LazySequence([<__main__.ReadASEDB>], [[0, 2, 4, 6, 8]])\ndata.tolist() # list[ase.Atoms] \n\n# supports addition, advanced slicing, etc.\ndata = db[::2] + db[1::2]\n```\n',
    'author': 'zincwarecode',
    'author_email': 'zincwarecode@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
