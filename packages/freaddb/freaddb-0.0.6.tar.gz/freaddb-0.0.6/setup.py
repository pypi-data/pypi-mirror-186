# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['freaddb']

package_data = \
{'': ['*']}

install_requires = \
['lmdb>=1.3.0,<2.0.0',
 'lz4>=4.0.1,<5.0.0',
 'msgpack>=1.0.4,<2.0.0',
 'numpy>=1.22.4,<2.0.0',
 'psutil>=5.9.4,<6.0.0',
 'pyroaring>=0.3.3,<0.4.0',
 'tqdm>=4.64.0,<5.0.0',
 'ujson>=5.3.0,<6.0.0']

setup_kwargs = {
    'name': 'freaddb',
    'version': '0.0.6',
    'description': 'Fast Read DB',
    'long_description': '# FReadDB\n\nFReadDB: Fast Read Database is implemented with LMDB (key-value database) as the underlying storage. We use this DB as a data storage, and RAM of [MTab system](https://mtab.kgraph.jp).\n\n## Installation\n\n```bash\npip install freaddb\n```\n\n## Usage\n\n```python\nfrom freaddb.db_lmdb import SIZE_1GB, DBSpec, FReadDB, ToBytes\n\n# Data file directory\ndata_file = "/tmp/freaddb/db_test_basic"\n# Clear old data\nshutil.rmtree(data_file, ignore_errors=True)\n\n# Define sub database schema\ndata_schema = [\n    # keys are strings, values are python objs and compress values\n    DBSpec(\n        name="data0",\n        integerkey=False,\n        bytes_value=ToBytes.OBJ,\n        compress_value=True,\n    ),\n    # key are integers, values are python objects serialized with msgpack and no compress values\n    DBSpec(name="data1", integerkey=True, bytes_value=ToBytes.OBJ),\n    # key are strings, values are python objects serialized with pickle\n    DBSpec(name="data2", integerkey=False, bytes_value=ToBytes.PICKLE),\n    # key are strings, values are bytes\n    DBSpec(name="data3", integerkey=False, bytes_value=ToBytes.BYTES),\n    # key are integers, values are list integers serialized with numpy\n    DBSpec(name="data4", integerkey=True, bytes_value=ToBytes.INT_NUMPY),\n    # key are integers, values are list integers serialized with BITMAP\n    DBSpec(name="data5", integerkey=True, bytes_value=ToBytes.INT_BITMAP),\n    # key are combination of two integers\n    DBSpec(name="data6", integerkey=True, combinekey=True),\n    # key are combination of three integers\n    DBSpec(\n        name="data7",\n        integerkey=True,\n        combinekey=True,\n        combinelen=3,\n    ),\n]\n\n# Example data\ndata = {\n    "data0": {"One": {1: "One"}, "Two": {2: "Two"}},\n    "data1": {1: "One", 2: "Two"},\n    "data2": {"One": 1, "Two": 2},\n    "data3": {"One": b"1", "Two": b"2"},\n    "data4": {i: list(range(i * 10)) for i in range(10, 20)},\n    "data5": {i: list(range(i * 10)) for i in range(10, 20)},\n    "data6": {(1, 2): "One", (2, 3): "Two"},\n    "data7": {(1, 2, 3): "One", (2, 3, 4): "Two"},\n}\nto_list_data = {"data4", "data5"}\n\n# Create data with data_file, data_schema, and buffer is 1GB\ndb = FReadDB(db_file=data_file, db_schema=data_schema, buff_limit=SIZE_1GB)\n\n# Add data to FReadDB\nfor data_name, data_items in data.items():\n    for key, value in data_items.items():\n        db.add_buff(data_name, key, value)\n# db.delete_buff("data0", "One")\n\n# Make sure save all buffer to disk\ndb.save_buff()\n\n####################################################\n# (Optional for readonly database) Compress database\ndb.compress()\ndb.close()\ndb = FReadDB(db_file=data_file, readonly=True)\n####################################################\n\n# Access data\n# Get a key\nsample = db.get_value("data1", 1)\nassert sample == "One"\n\n# Get many keys\nfor data_name, data_samples in data.items():\n    sample = db.get_values(data_name, list(data_samples.keys()))\n    if data_name in to_list_data:\n        sample = {k: list(v) for k, v in sample.items()}\n    assert sample == data_samples\n```\n',
    'author': 'Phuc Nguyen',
    'author_email': 'phucnt.ty@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/phucty/freaddb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
