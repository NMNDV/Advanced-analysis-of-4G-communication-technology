'''
Test for LDPC
'''


import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import LDPC_support_matrices

'''for i in range(3):
    signal = [0] * len(LDPC_support_matrices.matrix_01[0])
    signal[i] = 1
    noisy_signal = signal 
    print(noisy_signal)
    decoded_signal = decoder.decode(LDPC_support_matrices.matrix_01, noisy_signal)
    print(decoded_signal, '\n')'''
parity_check_matrix = LDPC_support_matrices.matrix_01
msg = [0] * len(parity_check_matrix[0])
msg[len(msg) - 1] = 1
print(decoder.decode(parity_check_matrix, msg))
msg = [0] * len(parity_check_matrix[0])
msg[2] = 1
print(decoder.decode(parity_check_matrix, msg))



