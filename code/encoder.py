'''
Encoder:
    1) product code encoder
'''
import matrix_generator

def product_code_encoder(list_item):
    support_matrix = matrix_generator.get_set_of_matrices(len(list_item))[0]
    encoded_data = []
    for temp in support_matrix:
        encoded_data.append(sum([ list_item[x] * temp[x] for x in range(len(temp)) ]) % 2)
    return encoded_data

'''
Test:
signal = [0, 0, 0, 1]
encoded_signal = product_code_encoder(signal)
print(encoded_signal)
'''