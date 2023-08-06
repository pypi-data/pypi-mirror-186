import json

def get_code_from_notebook(filename):
    f = open(filename, "r")
    data = json.loads(f.read())
    code = ''
    for cell in data['cells']:
        for line in cell['source']:   
            code = code + line
        code = code + '\n'
    return code

def add_headers(codebase, function_name, is_query=False):
    head_before = f"CREATE FUNCTION {function_name}() " + '''
    RETURNS TEXT
    AS $$ '''
    head_after = '''$$ LANGUAGE plpython3u;
    '''
    enable_cache = 'cache_back.cache_from_list()'
    final_query = head_before + '\n' + codebase + '\n' + enable_cache + '\n' + head_after
    if is_query:
        final_query = final_query.replace("'", "''")
    return final_query

def generate_query(notebook, function_name):
    return add_headers(get_code_from_notebook(notebook), function_name)