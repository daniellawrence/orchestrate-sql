# orchestrate-sql

Imports a SQL database into Orchestrate (or vice versa) either as a CLI or in other Python scripts.

When importing, `orchestrate-sql` maps SQL tables to Orchestrate [collections](http://orchestrate.io/docs/apiref#collections), and rows to [key-values](http://orchestrate.io/docs/apiref#keyvalue). For example, a table named `users` will be copied to a collection by the same name; each row within will be converted to a JSON document and inserted into the collection under the same key as their primary key in the SQL database.

When exporting, the tool maps likewise but in the other direction: copying collection contents to rows within tables in the destination database.

## Install

Just use [pip](https://pip.pypa.io/en/latest/):

```shell
pip install orchestrate-sql
```

Then, use the CLI to copy a SQL database into Orchestrate:

```shell
orchestrate-sql import --api-key ORCHESTRATE_APP_KEY --sql-uri sql://URI_FOR_YOUR_DATABASE
```

Or, import it into other Python scripts:

```python
import orchestrate_sql

orchestrate_sql.import(ORCHESTRATE_APP_KEY, URI_FOR_YOUR_DATABASE)
```

## Usage

### CLI

Both commands use the same option flags:

* `--api-key, -a`: the Orchestrate API key for whatever application you want to sync with.
* `--sql-uri, -s`: the connection URI for the SQL database you want to sync with.

#### import

Import data from a SQL database into Orchestrate.

#### export

Export data from Orchestrate into a SQL database.

### Library

Both methods take the same arguments:

```python
def import (ORCHESTRATE_API_KEY, SQL_URI):
    ...

def export (ORCHESTRATE_API_KEY, SQL_URI):
    ...
```

#### import

Import data from a SQL database into Orchestrate.

#### export

Export data from Orchestrate into a SQL database.

## Tests

    git clone https://github.com/garbados/orchestrate-sql.git
    cd orchestrate-sql
    python setup.py test

## License

[Apache-2.0](http://opensource.org/licenses/Apache-2.0)
