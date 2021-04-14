import scipy.io as scio
import encoder
import decoder2
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
import random
mat = scio.loadmat('Hmatrix.mat')

k = 5056
Nsamples = 25
p = 0.04
raw_estimation = []
sumx = 0
temp = 0
'''
for p in prob_set:
    while temp < Nsamples:
        temp += 1
        signal = np.array([0] * k)
        #encoded_signal = encoder.product_code_encoder(signal)
        noisy_signal = channel.insert_noise_BEC(signal, p)
        decoded_signal = decoder2.decoder_for_BEC(mat['H'], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
        if (list(decoded_signal) == [0] * k):
            print(sumx)
            sumx += 1
        print(temp, sumx)
    print("ans = ", sumx / Nsamples)
input('')'''
'''
signal = [0] * 5056
for temp in range(50):
    signal[temp * 50 + random.randint(0, 49)] = 1
msg = decoder2.decoder_for_BSC(mat['H'], signal)
print(msg, '\n', msg.count(1))
scio.savemat('ldpcexample.mat', mdict={
    'error': decoder2.decoder_manual.decoder_data
})'''
while temp < Nsamples:
    temp += 1
    signal = np.array([0] * k)
        #encoded_signal = encoder.product_code_encoder(signal)
    noisy_signal = channel.insert_noise_BSC(signal, p)
    decoded_signal = decoder2.decoder_for_BSC(mat['H'], noisy_signal)
        #recived_message = decoder.get_message(decoded_signal, n)
    if (list(decoded_signal) == [0] * k):
        print(sumx)
        sumx += 1
    print(temp, sumx)
print("ans = ", sumx / Nsamples)
