<h1 align="center"
>Data Science Manager 👨‍💻
</h1>
<p
>
  <a
  href="#"
  target="_blank"
  >
    <img
    alt="Version"
    src="https://img.shields.io/badge/version-1.2-blue.svg?cacheSeconds=2592000"
    />
  </a>
  <a
  href="http://dsmanager.rtfd.io/"
  target="_blank"
  >
    <img
    alt="Documentation"
    src="https://img.shields.io/badge/documentation-rtfd-orange.svg"
    />
  </a>
  <a
  href="LICENSE"
  target="_blank"
  >
    <img
    alt="License: Adel Rayane Amrouche"
    src="https://img.shields.io/badge/License-Adel Rayane Amrouche-yellow.svg"
    />
  </a>
</p>

> Data Science tools to ease access and use of data and models

## Install

The easiest way to install scikit-learn is using `pip`:

```sh
pip install dsmanager
```

or `poetry`

```sh
poetry add dsmanager
```

or `conda`

```sh
conda install dsmanager
```

Multiple sub dependencies are available depending on the needs:

```sh
pip install dsmanager[sharepoint] # Add Sharepoint source handling
pip install dsmanager[salesforce] # Add SalesForce source handling
pip install dsmanager[kaggle] # Add Kaggle source handling
pip install dsmanager[snowflake] # Add Snowflkae source handling
pip install dsmanager[mysql] # Add MySQL source handling
pip install dsmanager[pgsql] # Add PostgreSQL source handling
```

## Usage

The DS Manager has 3 main components:

- A **DataManager** component
- A **Controller** component
- A **Model** component

### DataManager

The DataManager allows to manage different types of data sources among which one can mention:

- File (File locally or online)
- Http (Http requests)
- Ftp (Ftp hosted files)
- Sql (Sql database tables)
- Sharepoint (Microsoft OneDrive files)
- SalesForce (SalesForce classes)
- Kaggle (Kaggle datasets)

The first step to use the DataManager is to instance it with a metadata path.

```python
from dsmanager import DataManager
dm = DataManager("data/metadata.json")
```

The metadata file is generated if it does not exist and it consist of a dict of sources following this schema:

```json
{
  "SOURCE_NAME": {
    "source_type": "name_of_the_source",
    "args": {}
  }
}
```

Each source has a `source_type` corresponding to the name of the source. You can access this list with this command:

```python
DataManager().datasources
```

Each of these data sources has its own schema because of its own parameters requierements. You can also add additional arguments which are not required with the parameter `args`.

You can obtain the schema for a specific datasource with the following command:

```python
source_name = "file"
DataManager().datasources[source_name].schema
```

Output:

```json
{
    "source_type": "file",
    "path": "local_path | online_uri",
    "file_type": "csv | excel | text | json | ...",
    "encoding": "utf-8",
    "args": {
        "pandas_read_file_argument_keyword": "value_for_this_argument"
    }
}
```

## Development

### Source code

You can check the latest sources with the command:

```python
git clone https://gitlab.com/bigrayou/dsmanager
```

### Testing

After installation, you can launch the test suite from outside the dsmanager directory (you will need to have pytest >= 7.1.3 installed):

```python
pytest -v
```

### Dependencies

The DSManager requires:

- cryptography 38.0.4
- dash >=2.7.1,<3.0.0
- explainerdashboard >=0.4.0,<0.5.0
- llvmlite >=0.39.1,<0.40.0
- numba >=0.56.4,<0.57.0
- numexpr >=2.8.4,<3.0.0
- numpy >=1.23.3,<2.0.0
- openpyxl >=3.0.10,<4.0.0
- optuna >=3.0.5,<4.0.0
- pandas >=1.5.0,<2.0.0
- paramiko >=2.12.0,<3.0.0
- pickle-mixin >=1.0.2,<2.0.0
- python-dotenv >=0.21.0,<0.22.0
- requests >=2.28.1,<3.0.0
- scikit-learn >=1.2.0,<2.0.0
- setuptools >=65.6.3,<66.0.0
- shap >=0.41.0,<0.42.0
- sqlalchemy >=1.4.45,<2.0.0
- sweetviz >=2.1.4,<3.0.0
- tqdm >=4.64.1,<5.0.0

Optionnaly, the DSManager could require:

- azure-common >=1.1.28,<2.0.0
- azure-storage-blob >=12.14.1,<13.0.0
- azure-storage-common >=2.1.0,<3.0.0
- kaggle >=1.5.12,<2.0.0
- mysqlclient >=2.1.1,<3.0.0
- psycopg2-binary >=2.9.5,<3.0.0
- shareplum >=0.5.1,<0.6.0
- simple-salesforce >=1.12.2,<2.0.0
- snowflake-connector-python >=2.9.0,<3.0.0
- snowflake-sqlalchemy >=1.4.4,<2.0.0

## Author

👤 **Rayane Amrouche**

- Github: [@AARayane](https://github.com/AARayane)
- Gitlab: [@Bigrayou](https://gitlab.com/bigrayou)
