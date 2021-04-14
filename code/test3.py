'''
Test for BSC and BEC decoders(auto generated inputs)
'''

import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

k = 4
p = 0
loop_variant = 5
G_H_set = matrix_generator.get_set_of_matrices(k)
for temp in range(loop_variant):
    print("\n#", temp)
    message_signal = [0] * k
    print("message:", message_signal)
    encoded_signal = encoder.product_code_encoder(message_signal)
    print("encoded message:", encoded_signal)
    noisy_signal = encoded_signal
    print("noisy encoded message:", encoded_signal)
    decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
    print("decoded message:", decoded_signal)
    recieved_signal = decoder.get_message(decoded_signal, k)
    print("recieved message:", recieved_signal)
