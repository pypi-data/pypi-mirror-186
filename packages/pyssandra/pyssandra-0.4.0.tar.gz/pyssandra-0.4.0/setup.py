# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyssandra']

package_data = \
{'': ['*']}

install_requires = \
['case-switcher>=1.3.4,<2.0.0',
 'cassandra-driver>=3.25.0,<4.0.0',
 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'pyssandra',
    'version': '0.4.0',
    'description': 'Use pydantic models to create basic CQL queries.',
    'long_description': '# Pyssandra\n\nBuild simple CQL queries from Pydantic models.\n\n### Example\n\n```python\nimport uuid\n\nfrom cassandra.auth import PlainTextAuthProvider\nfrom cassandra.cluster import Cluster\nfrom pydantic import BaseModel, Field\n\nfrom pyssandra import Pyssandra\n\ncloud_config = {"secure_connect_bundle": "/path/to/secure-connect-dbname.zip"}\nauth_provider = PlainTextAuthProvider(username="user", password="pass")\ncluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)\nsession = cluster.connect()\n\nkeyspace = "test"\ndb = Pyssandra(session, keyspace)\n\n\n@db.table(keys=["id"])\nclass User(BaseModel):\n    """Test user model."""\n\n    id: uuid.UUID = Field(default_factory=uuid.uuid4)\n    first: str\n    last: str\n\n\nuser = User(first="Test", last="User")\nawait db[User].insert(user)\nawait db[User].find_one(uuid.uuid4())\nawait db[User].update(user)\n```\n',
    'author': 'Matthew Burkard',
    'author_email': 'matthewjburkard@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/mburkard/pyssandra',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
