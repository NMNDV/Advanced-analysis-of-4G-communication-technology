'''
Channel:
        1) BEC channel
        2) BSC channel
        3) random bit generator of probability p
'''
import random

def get_random_bit(p):
    return random.randint(0, 99) < p * 100

def insert_noise_BEC(list_item, p):
    noisy_signal = list_item
    for temp in range(len(noisy_signal)):
        if get_random_bit(p):
            noisy_signal[temp] = -1
    return noisy_signal

def insert_noise_BSC(list_item, p):
    noisy_signal = list_item
    for temp in range(len(noisy_signal)):
        if get_random_bit(p):
            noisy_signal[temp] ^= 1
    return noisy_signal

'''
Test:
signal = [0] * 10
p = 0.1
noisy_signal = insert_noise_BEC(signal, p)
print(noisy_signal)
signal = [0] * 10
p = 0.1
noisy_signal = insert_noise_BSC(signal, p)
print(noisy_signal)
'''