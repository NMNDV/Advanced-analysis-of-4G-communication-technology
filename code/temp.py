import channel
import matplotlib.pyplot as plt
import scipy.io as scio
Nsemp = 200000
n = 20
p = 0.2
estem = [0] * (n + 1)
i = 0
while i < Nsemp:
    i += 1
    signal = [0] * n
    noisy_signal = channel.insert_noise_BEC(signal, p)
    estem[noisy_signal.count(-1)] += 1 / Nsemp

scio.savemat('pmf.mat', mdict={"array":estem})
