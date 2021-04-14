'''
Test for BSC and BEC decoders(manual inputs)
'''

import encoder
import decoder2
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
'''
G_H_set = matrix_generator.get_set_of_matrices_advanced(25)
meg = [0] * 36
noise_set = []
for temp in noise_set:
    meg[temp - 1] = -1
for temp in G_H_set[1]:
    print(temp)
print('\n', decoder.decode(G_H_set[1], meg))
'''
'''
msg = [0] * 9
G_H_set = matrix_generator.get_set_of_matrices_advanced(4)
for i in range(3):
    for j in range(3):
        msg = [0] * 9
        msg[ (3 * i + j) ] = 1
        msg[3 * i + ((j + 1) % 3)] = 1
        print(i, j, decoder.decode(G_H_set[1], msg))'''
'''G_H_set = matrix_generator.get_set_of_matrices(4)
for i in range(7):
        for j in range(i + 1, 9):
                msg = [0] * 9
                msg[i] = 1
                msg[j] = 1
                decoded_message = decoder.decode(G_H_set[1], msg)
                print(i, j, decoded_message, decoded_message == [0] * 9)
                ''''''
G_H_set = matrix_generator.get_set_of_matrices_advanced(4)
msg = [0] * 9
print(decoder.decode(G_H_set[1], msg))'''
'''
G_H_set1 = matrix_generator.get_set_of_matrices(4)
G_H_set2 = matrix_generator.get_set_of_matrices_advanced(4)
for i in range(9):
        message = [0] * 9
        message[i] = 1
        print(decoder.decode(G_H_set1[1], message))
print()
for i in range(9):
        message = [0] * 9
        message[i] = 1
        print(decoder.decode2(G_H_set1[1], message))
print()
for i in range(9):
        message = [0] * 9
        message[i] = 1
        print(decoder.decode(G_H_set2[1], message))
print()
for i in range(9):
        message = [0] * 9
        message[i] = 1
        print(decoder.decode2(G_H_set2[1], message))
print()'''

G_H_set = matrix_generator.get_set_of_matrices(9)
sumx=0
for temp in range(11):
        for temp2 in range(temp + 1, 12):
                for temp3 in range(temp2 + 1, 13):
                        for temp4 in range(temp3 + 1, 14):
                                for temp5 in range(temp4 + 1, 15):
                                        for temp6 in range(temp5 + 1, 16):
                                                signal = [0] * 16
                                                signal[temp] =signal[temp2] = signal[temp3] = signal[temp4] = signal[temp5] = signal[temp6] = -1
                                                dummy2 = [x for x in signal]
                                                recevied_signal=decoder2.decoder_for_BEC(G_H_set[1], signal)
                                                if(recevied_signal == [0] * 16):
                                                        sumx=sumx+1
                                                        print(sumx)
print(sumx)