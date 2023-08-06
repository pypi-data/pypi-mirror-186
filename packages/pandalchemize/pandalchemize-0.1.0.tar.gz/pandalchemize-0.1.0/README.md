
# pandalchemize: an intuitive combination of Pandas and sqlalchemy to manipulate sql databases with pandas

## What is it?

**pandalchemize** is a Python package that lets Data Scientists create and manipulte sql databases with the Pandas package 
that they know and love without needing to learn the ins and outs of sqlalchemy.

## Main Features
Here are just a few of the things that pandalchemize does:

  - Pulls down any sql table as a Pandas DataFrame with sqlalchemy and maintains all data types, keys, and indexes
    after you push your changes.
  - Make changes to Pandas DataFrame as you normally would then push any changes (new columns, delete columns, new rows, updated rows) to sql database.
  - Add or change primary keys in database table.
  - Add or delete columns in a database table thanks to alembic.

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/eddiethedean/pandalchemize

```sh
# PyPI
pip install pandalchemize
```

## Dependencies
- [pandas](https://pandas.pydata.org/)
- [tabulize]
        
# Example code
```sh
from sqlalchemy import create_engine 
import pandalchemize as pz 
        
# Use sqlalchemy to create an engine to connect to existing database 
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase') 
        
# Initialize a pandalchemy SqlDataFrame object 
sdf = pz.SqlDataFrame('test_table', engine) 
        
# Make changes to the SqlDataFrame just like you would a Pandas DataFrame 
sdf['age'] = [11, 12, 13, 14, 15] 
        
# Use the push method to push all your changes to your database 
sdf.push() 
```