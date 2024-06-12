def infer_sql_types(data):
    """
    Infers SQL data types from a dictionary of example data.

    Args:
        data (dict): A dictionary where keys are column names and values are example data.

    Returns:
        dict: A dictionary where keys are column names and values are inferred SQL data types.
    """
    sql_types = {}
    for key, value in data.items():
        if isinstance(value, bool):
            sql_types[key] = 'bit'
        elif isinstance(value, int):
            sql_types[key] = 'int'
        elif isinstance(value, str):
            if value.lower() in ('true', 'false'):
                sql_types[key] = 'bit'
            elif is_date(value):
                sql_types[key] = 'datetime'
            else:
                sql_types[key] = 'nvarchar(100)'
        else:
            raise ValueError(f"Unsupported data type for key: {key}")
    return sql_types


    return sql_types

def is_date(string):
    """
    Checks if a string can be interpreted as a date.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string can be interpreted as a date, False otherwise.
    """
    from datetime import datetime

    try:
        datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Example usage:
op_asset_assign = {
    'id': 0,
    'opap_id': 11,
    'type': 'Mobile',
    'material': 'Mobile 1',
    'description': 'Samsung Galaxy S4',
    'area': 'AA',
    'building': 'AA',
    'owner_by': '11',
    'manger_by': '13254',
    'create_by': '1234',
    'createdate_by': '2024-06-01',
    'editdate_by': '2024-06-02',
    'track_on': 'xxxxx',
}

op_asset_type = infer_sql_types(op_asset_assign)
print(op_asset_type)
