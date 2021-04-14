%% About
clear vars;
close all;
clc;
% BSC graph analysis(Theoretical)
%% Load data
load analysis_BSC.mat;
%% Generating support matrix and theoretical values
support_matrix = [];
prob_set2 = 0:0.001:1;
for temp = 0:9
    support_matrix = [support_matrix; prob_set2.^temp .* (1 - prob_set2).^(9 - temp)]; 
end
set_selected = [ 1, 9, 4, 0, 0, 0, 0, 0, 0, 1 ];
raw_estimations2 = support_matrix' * set_selected';
%% Ploting part
figure(1);
plot(prob_set, raw_estimations, 'r')
hold on;
plot(prob_set2, raw_estimations2, 'g')
title('BSC Analysis For (9,4) Product Code');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
legend('Experimental','Theoretical');
grid on;
