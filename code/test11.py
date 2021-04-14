import scipy.io as scio
import encoder
import decoder
import channel
import matrix_generator
import numpy as np
import matplotlib.pyplot as plt
mat = scio.loadmat('Hmatrix.mat')

k = 5056
p = 6 / 9
noisy_signal = channel.insert_noise_BEC([0] * k, p)
decoded_signal = decoder.decoder_for_BEC(mat['H'], noisy_signal)
print(decoder.decoder_manual)
scio.savemat('analysisLDPCBEC4.mat', mdict={"error": decoder.decoder_manual})