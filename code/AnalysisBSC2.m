%% About
clear vars;
close all;
clc;
% BEC graph analysis
%% Load data
load arrdataBEC2.mat;
%% Ploting part
figure(1);
plot(prob_set, raw_estimations, 'r')
hold on;
plot(prob_set, raw_estimations2, 'g');
hold on;
plot(prob_set, raw_estimations3, 'y');
hold on;
plot(prob_set, raw_estimations4, 'b');
title('Product Code BEC Analysis: (9,4) vs (16,9) vs (25,16) vs (36,25)');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
legend('(9,4)','(16,9)','(25,16)','(36,25)');
grid on;