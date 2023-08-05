# Pyssandra

Build simple CQL queries from Pydantic models.

### Example

```python
import uuid

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from pydantic import BaseModel, Field

from pyssandra import Pyssandra

cloud_config = {"secure_connect_bundle": "/path/to/secure-connect-dbname.zip"}
auth_provider = PlainTextAuthProvider(username="user", password="pass")
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

keyspace = "test"
db = Pyssandra(session, keyspace)


@db.table(keys=["id"])
class User(BaseModel):
    """Test user model."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    first: str
    last: str


user = User(first="Test", last="User")
await db[User].insert(user)
await db[User].find_one(uuid.uuid4())
await db[User].update(user)
```
