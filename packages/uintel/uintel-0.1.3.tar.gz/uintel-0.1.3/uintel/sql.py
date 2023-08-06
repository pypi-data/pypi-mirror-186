"""Connect to SQL databases.

Connect (or create) databases on postgreSQL servers, as well as upload DataFrames to databases quickly and efficiently.
"""

__all__ = ["connect", "upload"]

import io, sqlalchemy, sqlalchemy_utils, psycopg2, pandas, warnings

def connect(database_name: str, host: str) -> dict:
    """Connect to a database.

    Connect to a given database (e.g. 'chap'), using the stored credentials for SQL for the host (e.g. encivmu-tml62). If the database does not exist, then a new database is created with this databse_name. 

    Args:
        database_name: The name of the database to connect to, or create if it does not exist.
        host: The name or address of the SQL table host.
    
    Returns:
        A dictionary containing a sqlalchemy Engine ('engine') and a psycopg2 connection ('con').
    """

    from uintel import config, save_config
    try:
        credentials = config["sql"][host]
    except KeyError:
        warnings.warn(f"Unfortunately, {host} is not in your saved SQL databases.")
        credentials[host] = {
            "port": int(input(f"What port is the SQL database on {host}? (e.g. 5002) ")),
            "username": input("What is the username to connect to SQL? (e.g. postgres) "),
            "password": input("What is the password to connect to SQL? ")
        }
        # Save this new connection to the UI configuration file
        config["sql"][host] = credentials
        save_config(config)

    db = {'engine' : sqlalchemy.create_engine(f"postgresql+psycopg2://postgres:{credentials['password']}@{credentials['host']}/{database_name}?port={credentials['port']}")}

    exists = sqlalchemy_utils.database_exists(db['engine'].url)
    if not exists:
        sqlalchemy_utils.create_database(db['engine'].url)

    db['con'] = psycopg2.connect(f"host={credentials['host']} dbname={database_name} user=postgres password='{credentials['password']}' port={str(credentials['port'])}")

    if not exists:
        db['con'].cursor().execute("CREATE EXTENSION postgis;")
        db['con'].commit()

    return db


def upload(df: pandas.DataFrame, table_name: str, db: dict, if_exists: str = "replace") -> None:
    """Upload a DataFrame.

    Upload a Pandas Dataframe to a SQL table called table_name. 

    Args:
        df: The pandas.DataFrame to upload.
        table_name: The name of the table to upload the dataframe to.
        db: A dictionary of the SQL database engine and connection.
        if_exists: The action to undertake if the table_name exists. E.g. "replace" or "append".

    Returns:
        None.
    """

    # Truncates the table and sends the column names to sql
    df.head(0).to_sql(table_name, db['engine'], if_exists=if_exists, index=False) 
    
    # Open connection to sql
    conn = db['engine'].raw_connection()
    cur = conn.cursor()
    
    # Send dataframe to stringio
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    
    # Send stringio to sql
    output.seek(0)
    cur.copy_from(output, table_name, null="") # null values become ''
    conn.commit()