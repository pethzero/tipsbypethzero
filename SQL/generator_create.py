def generate_sql_create_table(table_name, column_definitions, primary_key='id', identity_column=None, collation='Thai_CI_AS'):
    sql = f"CREATE TABLE {table_name} (\n"
    columns = []

    date_now = ['create_date']
    
    for column_name, data_type in column_definitions.items():
        if column_name == identity_column:
            columns.append(f"    {column_name} {data_type} IDENTITY(1,1) NOT NULL")
        elif 'nvarchar' in data_type:
            columns.append(f"    {column_name} {data_type} COLLATE {collation}  NULL")
        elif 'datetime' in data_type and column_name in date_now:
            columns.append(f"    {column_name} {data_type}   NULL DEFAULT GETDATE()")
        else:
            columns.append(f"    {column_name} {data_type}  NULL")

    # Add primary key constraint
    columns.append(f"    PRIMARY KEY ({primary_key})")

    sql += ",\n".join(columns)
    sql += "\n);"

    return sql


def infer_sql_types(data):
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


def is_date(string):
    from datetime import datetime

    try:
        datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False



# Example usage:
op_asset_type = {'id':1,'type':'Mobile','is_active':True,'createdate_by':'2024-06-01'}
print(infer_sql_types(op_asset_type))

op_asset_part = {
  'id':11,
  'type':'Mobile',
  'material':'Mobile 1',
  'description':'Samsung Galaxy S4',
  'create_date':'2024-06-01',
  'edit_date':'2024-06-02',
}

op_asset_assign = {
      'id':0,
      'opap_id':11,	
      'type':'Mobile',
      'material':'Mobile 1',
      'description':'Samsung Galaxy S4',
      'area':'AA',
      'building':'AA',
      'owner_by':'11',
      'manger_by':'13254',
      'create_by':'1234',
      'createdate_by':'2024-06-01',
      'editdate_by':'2024-06-02',
      'track_on':'xxxxx',
  }


# print(generate_sql_create_table('op_asset_type', infer_sql_types(op_asset_type), primary_key='id', identity_column='id'))
print(generate_sql_create_table('op_asset_part', infer_sql_types(op_asset_part), primary_key='id', identity_column='id'))
# print(generate_sql_create_table('op_asset_record', infer_sql_types(op_asset_assign), primary_key='id', identity_column='id'))

