%% About
clear vars;
close all;
clc;
% BEC graph analysis
%% Load data
load arrdataBEC.mat;
%% Support matrix generator and ideal plot's estimation
support_matrix = [];
for temp = 0:9
    support_matrix = [support_matrix; prob_set.^temp .* (1 - prob_set).^(9 - temp)]; 
end
% matrix_analysis = raw_estimations' \ support_matrix';
set_selected = [ 1, 9, 36, 84, 117, 81, 0, 0, 0, 0 ];
raw_estimations2 = support_matrix' * set_selected';
%% Ploting part
figure(1);
plot(prob_set, raw_estimations, 'r')
hold on;
plot(prob_set, raw_estimations2, 'g');
title('BEC Analysis For (9,4) Product Code');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
legend('Experimental','Theoretical');
grid on;