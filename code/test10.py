''' Advanced analysis message-division => more probability of success) '''
'''
Graph analysis for BSC
'''


import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import scipy.io


k = 16
Nsamples = 20000
G_H_set = matrix_generator.get_set_of_matrices_advanced(k)
prob_set = np.linspace(0, 1, 41, endpoint=True)
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
        if (decoded_signal == [0] * 25):
            sumx += 1
    print(sumx)
    raw_estimation.append([sumx / Nsamples])
raw_estimation = np.array(raw_estimation)


k = 4
G_H_set = matrix_generator.get_set_of_matrices_advanced(k)
signal = [0] * k
raw_estimation2 = []
iteration = 0
for p in prob_set:
    sumx = 0
    print(iteration)
    iteration += 1
    for temp in range(Nsamples):
        sumy = 0
        for temp2 in range(4):
            encoded_signal = encoder.product_code_encoder(signal)
            noisy_signal = channel.insert_noise_BSC(encoded_signal, p)
            decoded_signal = decoder.decode(G_H_set[1], noisy_signal)
            #recived_message = decoder.get_message(decoded_signal, n)
            if (decoded_signal == [0] * 9):
                sumy += 1
        if sumy == 4:
            sumx += 1
    print(sumx)
    raw_estimation2.append([sumx / Nsamples])
raw_estimation2 = np.array(raw_estimation2)

scipy.io.savemat('advanced_analysis3.mat', mdict={
    'raw_estimations': raw_estimation,
    'raw_estimations2': raw_estimation2,
     'prob_set': prob_set
    })

'''
plt.plot(prob_set, raw_estimation, prob_set, raw_estimation2)
plt.show()'''
