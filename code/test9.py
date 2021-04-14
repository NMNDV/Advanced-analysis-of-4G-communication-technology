''' Advanced analysis (Extraction of message => more probability of success) '''
'''
Graph analysis for BSC(generates matrices only)
'''


import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io


def transpose(list_item):
    l1 = [ [] for _ in range(len(list_item[0]))]
    for y in range(len(list_item[0])):
        for x in range(len(list_item)):
            l1[y].append(list_item[x][y])
    return l1
k = 4
Nsamples = 5000
G_H_set = matrix_generator.get_set_of_matrices_advanced(k)
prob_set = np.linspace(0, 1, 21, endpoint=True)
signal = [0] * k
raw_estimation = []
iteration = 0
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BSC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if (decoded_signal == [0] * 9):
            sumx += 1
    print(sumx)
    raw_estimation.append([sumx / Nsamples])
raw_estimation = np.array(raw_estimation)

raw_estimation2 = []
iteration = 0
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BSC(encoded_signal, p)
        decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
        recived_message = decoder.get_message(decoded_signal, k)
        if (recived_message == [0] * k):
            sumx += 1
    print(sumx)
    raw_estimation2.append([sumx / Nsamples])
raw_estimation2 = np.array(raw_estimation2)


scipy.io.savemat('advanced_analysis2.mat', mdict={
    'raw_estimations': raw_estimation,
    'raw_estimations2': raw_estimation2,
     'prob_set': prob_set
    })

'''
plt.plot(prob_set, raw_estimation, prob_set, raw_estimation2)
plt.show()
'''
