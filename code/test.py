'''
Test for matrix_generators(capability):
1) matrix_generator.get_set_of_matrices
2) matrix_generator.get_set_of_matrices_advanced
'''


import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

H1 = [
    [1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1]
]

H2 = [
    [1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1]
]
H3 = [
    [1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1]
]
'''
signal = [0] * 4
p = 0
encoded_signal = encoder.product_code_encoder(signal)
noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
decoded_signal = decoder.decode(H1, noisy_signal)
print(decoded_signal)
        #recived_message = decoder.get_message(decoded_signal, n)'''
n = 4
Nsamples = 25000
prob_set = np.linspace(0, 1, 11, endpoint=True)
signal = [0] * n

raw_estimation1 = []
raw_estimation2 = []
raw_estimation3 = []
raw_estimation4 = []

for p in prob_set:
    sumx = 0
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(H1, noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * 9 :
            sumx += 1
        print(sumx)
    raw_estimation1.append(sumx / Nsamples)

for p in prob_set:
    sumx = 0
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(H2, noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * 9 :
            sumx += 1
    raw_estimation2.append(sumx / Nsamples)

for p in prob_set:
    sumx = 0
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(H3, noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * 9 :
            sumx += 1
    raw_estimation3.append(sumx / Nsamples)



G_H_set = matrix_generator.get_set_of_matrices_advanced(n)
signal = [0] * n
for p in prob_set:
    sumx = 0
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * 9 :
            sumx += 1
    raw_estimation4.append(sumx / Nsamples)

scipy.io.savemat('advanced_H_analysis.mat', mdict={
    'raw_estimations1': raw_estimation1, 
    'raw_estimations2': raw_estimation2, 
    'raw_estimations3': raw_estimation3, 
    'raw_estimations4': raw_estimation4, 
    'prob_set': prob_set
    })

plt.plot(prob_set, raw_estimation1, prob_set, raw_estimation2, prob_set, raw_estimation3, prob_set, raw_estimation4)
plt.show()
'''
Graph is in advanced_H_analysis.m
'''