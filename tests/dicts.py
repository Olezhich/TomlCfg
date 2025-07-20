default_cfg = \
'''
default_field = 'text_default'
secret_field  = 'nothing'
'''

secret_cfg = \
'''
secret_field = 'text_secret'
new_secret_field = 'text2_secret'
'''

cfg_w_containers1 = \
'''
list_field = [1,2,3]
[dict_field]
    key1 = 1
    key2 = 2
'''

cfg_w_containers2 = \
'''
list_field = [4,5,6]
[dict_field]
    key2 = 22 
    key3 = 3
'''

cfg_w_containers3 = \
'''
list_field = 'str'
[dict_field]
    key2 = 22 
    key3 = 3
'''

first_case_dict = {
    'default_field' : 'text_default',
    'secret_field' : 'text_secret',
    'new_secret_field' : 'text2_secret',
}

second_case_dict = {
    'list_field' : [4,5,6],
    'dict_field' : {'key1' : 1, 'key2' : 22, 'key3' : 3},
}
