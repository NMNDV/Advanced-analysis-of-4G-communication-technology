%% About
clear vars;
close all;
clc;
% Advanced analysis extracting message => more probability of success
%% Load data
load advanced_analysis2.mat;
%% Ploting part
figure(1);
plot(prob_set, raw_estimations, 'r')
hold on;
plot(prob_set, raw_estimations2, 'b');
hold on;
title('Product Code advanced Analysis For (9,4)');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
legend('With Out Extracting Message','After Extracting Message');
grid on;