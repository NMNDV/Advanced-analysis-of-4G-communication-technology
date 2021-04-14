LDPC_BSC = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
prob_set = 0:0.1:1;
plot(prob_set, LDPC_BSC, 'b:*');
title('LDPCBSC approximated');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
xticks(0:0.1:1)
grid on;