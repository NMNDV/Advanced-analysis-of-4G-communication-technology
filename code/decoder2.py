'''
1) LDPC_decoder_for_BSC (iteration = 50)
2) LDPC_decoder_for_BEC (iteration = 50)
3) Decode
'''
import matrix_generator
import math


class data:
    def __init__(self, data):
        self.decoder_data = data
decoder_manual = data([])


def decoder_for_BSC(mat, list_item):
    syndrome = [1]
    iteration = 0
    #list_item_dumy = [[x] for x in list_item]
    while syndrome != [0] * len(syndrome) and iteration != 50:
        print(iteration)
        syndrome = []
        var_estm = [ [x] for x in list_item ]
        for temp in mat:
            check_mat = [x for x in range(len(temp)) if temp[x] == 1]
            temp3 = sum([ list_item[x] for x in check_mat])
            temp3 %= 2
            syndrome.append(temp3)
            for temp2 in check_mat:
                var_estm[temp2].append((temp3 + list_item[temp2]) % 2)
        for y in range(len(var_estm)):
            temp = var_estm[y].count(list_item[y])
            if temp < len(var_estm[y]) / 2:
                list_item[y] ^= 1 
        iteration += 1
    return list_item

def decoder_for_BEC(mat, list_item):
    quary_list = [ x for x in range(len(list_item)) if list_item[x] == -1]
    iteration = 0
    has_not_changed = False
    #sumx = len(quary_list)
    decoder_manual.decoder_data = [0] * 50
    while quary_list != [] and iteration != 50 and not has_not_changed : # and sumx > 0 :
        #print(iteration)
        has_not_changed = True
        #decoder_manual.decoder_data[iteration] = sumx
        for index_of_error in quary_list:
            for temp in range(len(mat)):
                if mat[temp][index_of_error] == 1:
                    check_mat = [ mat[temp][x] * list_item[x] for x in range(len(mat[temp])) if x != index_of_error ]
                    if -1 not in check_mat:
                        #print('#', index_of_error, 'iter:', iteration)
                        list_item[index_of_error] = sum(check_mat) % 2
                        has_not_changed = False
                        #sumx -= 1
                        break
        quary_list = [ x for x in range(len(list_item)) if list_item[x] == -1]
        iteration += 1
        #print(iteration)
    return list_item


def get_message(list_item, n):
    return list_item[0 : n]

def decode(mat, list_item):
    if -1 in list_item:
        return decoder_for_BEC(mat, list_item)
    else:
        return decoder_for_BSC(mat, list_item)


def decoder_for_BEC2(mat, list_item):
    quary_list = [ x for x in range(len(list_item)) if list_item[x] == -1]
    iteration = 0
    has_not_changed = False
    #sumx = len(quary_list)
    decoder_manual.decoder_data = [0] * 50
    while quary_list != [] and iteration != 50 and not has_not_changed : # and sumx > 0 :
        #print(iteration)
        has_not_changed = True
        #decoder_manual.decoder_data[iteration] = sumx
        for index_of_error in quary_list:
            temp2 = len(mat)
            temp = 0
            while temp < temp2:
                if mat[temp][index_of_error] == 1:
                    check_mat = [ mat[temp][x] * list_item[x] for x in range(len(mat[temp])) if x != index_of_error ]
                    if -1 not in check_mat:
                        #print('#', index_of_error, 'iter:', iteration)
                        list_item[index_of_error] = sum(check_mat) % 2
                        has_not_changed = False
                        quary_list.remove(index_of_error)
                        #sumx -= 1
                        break
                temp += 1
        #quary_list = [ x for x in range(len(list_item)) if list_item[x] == -1]
        iteration += 1
        #print(iteration)
    return list_item

def decode2(mat, list_item):
    if -1 in list_item:
        return decoder_for_BEC2(mat, list_item)
    else:
        return decoder_for_BSC(mat, list_item)

'''
Tests are test.py, test2-11.py
'''