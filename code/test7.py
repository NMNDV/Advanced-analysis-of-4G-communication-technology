'''
Graph analysis for product code(BEC)(generates matrices only)
'''

import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import math


n = 4
tot_size = int((math.sqrt(n) + 1)** 2)
Nsamples = 5000
G_H_set = matrix_generator.get_set_of_matrices_advanced(n)
prob_set = np.linspace(0, 1, 21, endpoint=True)
signal = [0] * n
raw_estimation = []
iteration = 1
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * tot_size :
            sumx += 1
    raw_estimation.append(sumx / Nsamples)

n = 9
tot_size = int((math.sqrt(n) + 1)** 2)
Nsamples = 5000
G_H_set = matrix_generator.get_set_of_matrices_advanced(n)
prob_set = np.linspace(0, 1, 21, endpoint=True)
signal = [0] * n
raw_estimation2 = []
iteration = 1
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * tot_size :
            sumx += 1
    raw_estimation2.append(sumx / Nsamples)

n = 16
tot_size = int((math.sqrt(n) + 1)** 2)
Nsamples = 5000
G_H_set = matrix_generator.get_set_of_matrices_advanced(n)
prob_set = np.linspace(0, 1, 21, endpoint=True)
signal = [0] * n
raw_estimation3 = []
iteration = 1
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * tot_size :
            sumx += 1
    raw_estimation3.append(sumx / Nsamples)

n = 25
tot_size = int((math.sqrt(n) + 1)** 2)
Nsamples = 5000
G_H_set = matrix_generator.get_set_of_matrices_advanced(n)
prob_set = np.linspace(0, 1, 21, endpoint=True)
signal = [0] * n
raw_estimation4 = []
iteration = 1
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if decoded_signal == [0] * tot_size :
            sumx += 1
    raw_estimation4.append(sumx / Nsamples)
scipy.io.savemat('arrdataBEC2.mat', mdict={
    'raw_estimations': raw_estimation,
    'raw_estimations2': raw_estimation2,
    'raw_estimations3': raw_estimation3,
    'raw_estimations4': raw_estimation4,
    'prob_set': prob_set
    })