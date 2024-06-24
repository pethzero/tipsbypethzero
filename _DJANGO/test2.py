

def update_general_uniform(data):
    try:
        status = 20

        data_temp = data
        status_check = {
            'process_is_smock': False,
            'process_is_cap': False,
            'process_is_shoe': False,
        }
        
        if data_temp['mat_smock'] is not None:
                if data_temp['is_smock'] == False:
                    if status_check['process_is_smock']:
                        data['is_smock'] = True
                        status = 30
                              
        if data_temp['mat_esd_shoe'] is not None:
                if data_temp['is_shoe'] == False:
                    if status_check['process_is_shoe']:
                        data['is_shoe'] = True
                        status = 30

        
        if data_temp['mat_esd_cap'] is not None:
                if data_temp['is_cap'] == False:
                    if status_check['process_is_cap']:
                        data['is_cap'] = True
                        status = 30
                        
                        
                        
        if data['mat_smock'] is not None:
            if data['is_smock'] == True:
                is_valid_smock = True
            else:
                is_valid_smock = False
        else:
            is_valid_smock = True
                              
        if data['mat_esd_shoe'] is not None:
            if data['is_shoe'] == True:
               is_valid_shoe  = True
            else:
                is_valid_shoe  = False
        else:
            is_valid_shoe  = True

        
        if data['mat_esd_cap'] is not None:
            if data['is_cap'] == True:
               is_valid_cap   = True
            else:
                is_valid_cap   = False
        else:
            is_valid_cap   = True
        
        if is_valid_cap and is_valid_shoe and is_valid_smock:
            status = 100
                        
      
        print(status)
        return status
    except Exception as e:
        return e

# Example usage
# data = {
#     'is_cap': True,
#     'is_shoe': True,
#     'is_smock': True,
#     'mat_esd_cap': 'SVIXXC-M00690',
#     'mat_esd_shoe': 'SVIXXC-M00750',
#     'mat_smock': 'SVIXXC-M00610'
# }

data = {
    'is_smock': False,
    'is_cap': False,
    'is_shoe': False,
    'mat_smock': None,
    'mat_esd_cap': None,
    'mat_esd_shoe': 'SVIXXC-M00750'

}
response = update_general_uniform(data)
print(response)

