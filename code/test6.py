'''
Test for longer imputs in product code(BEC)(Failed)
Because probability that we will get solvable inputs will be decreased
1000 length : p probability for BEC will get more erasures than 100 length
chances for circuits will increase
'''

import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

n = 1600
G_H_set = matrix_generator.get_set_of_matrices_advanced(n)
prob = 1 / 10
analitical_matrix = [0] * 40
estem = []
signal = [0] * n
for _ in range(20):
        print(_)
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, prob)
        decoded_signal = decoder.decoder_for_BEC(G_H_set[1], noisy_signal)
        #print(decoder.decoder_manual.decoder_data)
        estem.append(decoder.decoder_manual.decoder_data)
scipy.io.savemat('array_BEC.mat', mdict={'error': estem})


