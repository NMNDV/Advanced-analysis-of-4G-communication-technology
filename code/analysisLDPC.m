%% About
clear vars;
close all;
clc;
% Advanded H analysis
%% Load matrix
load analysisLDPCBEC3.mat
%% ploting part
figure(1);
plot(0:length(error.decoder_data) - 1, error.decoder_data);
title('LDPC code number of erasures vs iterations(p=4/9)');
xlabel('Iterations');
ylabel('Number of erasures');
grid on;
%% Load matrix
load analysisLDPCBEC4.mat
%% ploting part
figure(2);
plot(0:length(error.decoder_data) - 1, error.decoder_data);
title('LDPC code number of erasures vs iterations(p=6/9)');
xlabel('Iterations');
ylabel('Number of erasures');
grid on;