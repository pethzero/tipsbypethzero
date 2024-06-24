from django.http import JsonResponse
from your_app.models import GenaralUniform

def update_general_uniform(data, id_pk):
    try:
        # Get the existing object
        update_main = GenaralUniform.objects.using('op_doc_ctrl').get(id=id_pk)

        # Check conditions and update fields
        if data.get('is_cap') and data.get('mat_esd_cap') is not None:
            update_main.mat_esd_cap = data.get('mat_esd_cap')
        else:
            update_main.mat_esd_cap = None  # Clear field if condition is not met

        if data.get('is_shoe') and data.get('mat_esd_shoe') is not None:
            update_main.mat_esd_shoe = data.get('mat_esd_shoe')
        else:
            update_main.mat_esd_shoe = None  # Clear field if condition is not met

        if data.get('is_smock') and data.get('mat_smock') is not None:
            update_main.mat_smock = data.get('mat_smock')
        else:
            update_main.mat_smock = None  # Clear field if condition is not met

        # Save the updates
        update_main.save(using='op_doc_ctrl')

        # Check if all conditions are true
        if data.get('is_cap') and data.get('mat_esd_cap') is not None and \
           data.get('is_shoe') and data.get('mat_esd_shoe') is not None and \
           data.get('is_smock') and data.get('mat_smock') is not None:
            status = 100
        else:
            status = 200  # You can set another status if needed

        return JsonResponse({'status': status, 'message': 'Update successful'})
    
    except GenaralUniform.DoesNotExist:
        return JsonResponse({'status': 404, 'message': 'Object not found'})
    
    except Exception as e:
        return JsonResponse({'status': 500, 'message': str(e)})

# Example usage
data = {
    'is_cap': True,
    'is_shoe': True,
    'is_smock': False,
    'mat_esd_cap': 'SVIXXC-M00690',
    'mat_esd_shoe': 'SVIXXC-M00750',
    'mat_smock': 'SVIXXC-M00610'
}
id_pk = 1  # Replace with your actual id
response = update_general_uniform(data, id_pk)
print(response.content)
