import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import headers

DB_NAME = ""
DB_USER = ""
DB_PASS = ""
DB_HOST = ""
DB_PORT = 5432 # default
BLOB_TABLE_NAME = "pipeline_blobs"
_cached_objects = {}
def init_session(db_name, db_user, db_pass, db_host, db_port=5432):
    """ Initialises Database parameters for connection to postgres """
    global DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT 
    DB_NAME = db_name
    DB_USER = db_user
    DB_PASS = db_pass
    DB_HOST = db_host
    DB_PORT = db_port
    print(DB_USER,DB_PASS, DB_HOST, DB_PORT)
    print('init session invoked')

def _connect():
    """ Connect to postgres and retrieve all cached variables back into the script """
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print('_connect invoked')
    return conn


def insert(df, source_db_table, destination_db_table):
    """ Inserts a given dataframe into postgres """
    try:
        conn_string = f"postgrcache_back.send_blob('script.ipynb', 'init_nb')esql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        print(conn_string)
        db = create_engine(conn_string)
        conn = db.connect()
        df.to_sql(destination_db_table, con=conn, if_exists='replace', index=False)
        print(f"Cached Dataframe successfully to table: {destination_db_table}")
    except Exception as e:
        print(e.args[0])

def _execute_as_plpython(notebook_path, function_name):
    """ Takes a jupyter notebook and runs it as a plpython function on Postgres Server """
    try:
        plpython_query = headers.generate_query(notebook_path, function_name)
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)

        cur = conn.cursor()
        cur.execute(plpython_query)

        cur.execute(f"SELECT {function_name}();")
        res = cur.fetchall()
        print(res)
    except Exception as e:
        print(e.args[0])

def add_to_cache(object, name):
    _cached_objects[name] =  object
    print(f"Object added to cache. Current Cache: {_cached_objects.keys()}")

def view_cache():
    print(_cached_objects)

def remove_from_cache(object_name):
    if object_name in _cached_objects.keys():
        del _cached_objects[object_name]
        print(f"Removed {object_name}")
    else:
        raise Exception(f"{object_name} not found.")

def send_blob(notebook_path, file_name):
    _create_blob_table()
    try:
        conn = _connect()
        cur = conn.cursor()
        file_data = read_notebook_as_binary(notebook_path)
        plpython_script = headers.generate_query(notebook_path, 'script_plpy', is_query=True)
        print('generated query')
        print(plpython_script)
        blob = psycopg2.Binary(file_data)
        print('file read as binary')
        query = f"INSERT INTO {BLOB_TABLE_NAME} (file_name, source_notebook, plscript) VALUES('{file_name}',{blob},'''{plpython_script}''')"
        print(query)
        cur.execute(query)
        print('Blob inserted')
        _execute_as_plpython(notebook_path, 'execute_plpython')
        conn.commit()
        cur.close()
    except Exception as e:
        print(e.args[0])

def _create_blob_table():
    try:
        conn = _connect()
        cur = conn.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {BLOB_TABLE_NAME} (id SERIAL PRIMARY KEY, upload_date TIMESTAMP default current_timestamp, file_name TEXT, source_notebook BYTEA, plscript TEXT, updated_notebook BYTEA);"
        print(query)
        cur.execute(query)
        conn.commit() 
        cur.close()
    except Exception as e:
        print(e.args[0])


def read_notebook_as_binary(notebook_path):
    with open(notebook_path, 'rb') as file:
        data = file.read()
    return data

def translate_notebook_on_postgres(notebook_path):
    # Runs a query to fetch notebook from postgres, use our library (already installed on postgres) and translate notebook 
    # Fetch the most recent notebook
    query_fetch_latest_nb = f"SELECT source_notebook, id FROM pipeline_blobs  WHERE upload_date = (SELECT MAX(upload_date) FROM {BLOB_TABLE_NAME});"
    conn = _connect()
    cur = conn.cursor()
    res = cur.execute(query_fetch_latest_nb)
    print(res.fetchall())
    # 
    pass

def cache_from_list():
    for df_name, df in _cached_objects.items():
        insert(df,source_db_table="reviews_data",destination_db_table=df_name)
