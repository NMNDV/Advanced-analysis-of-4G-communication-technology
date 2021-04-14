%% About
clear vars;
close all;
clc;
% Advanced analysis deviding message => more probability of success
%% Load data
load advanced_analysis3.mat;
%% Support matrix generator (9,4)
support_matrix = [];
for temp = 0:9
    support_matrix = [support_matrix; prob_set.^temp .* (1 - prob_set).^(9 - temp)]; 
end
set_selected = [ 1, 9, 4, 0, 0, 0, 0, 0, 0, 1 ];
raw_estimations_ideal94 = (support_matrix' * set_selected')';
%% Support matrix generator (25,16)
support_matrix2 = [];
for temp = 0:25
    support_matrix2 = [support_matrix2; prob_set.^temp .* (1 - prob_set).^(25 - temp)]; 
end
set_selected2 = zeros(1,26);
set_selected2(1,1) = 1;
set_selected2(1,2) = 25;
set_selected2(1,3) = 16;
set_selected2(1,26) = 1;
raw_estimations_ideal2516 = (support_matrix2' * set_selected2')';
%% Ploting part
figure(1);
plot(prob_set, raw_estimations, 'r')
title('Exitement of student during CT111');
xlabel('Time');
ylabel('Enthusiasm');


figure(2);
plot(prob_set, raw_estimations2, 'r')
hold on;
plot(prob_set, raw_estimations_ideal94.^4, 'b');
hold on;
title('Product Code advanced Analysis For 4x(9,4)');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
legend('4x(9,4)', '4x(9,4) theoretical');
grid on;

figure(3);
plot(prob_set, raw_estimations, 'r')
hold on;
plot(prob_set, raw_estimations_ideal2516, 'g');
hold on;
title('Product Code advanced Analysis For (25,16)');
xlabel('Probability of error');
ylabel('Probability of successful decoding');
legend('(25,16)','(25,16) theoretical');
grid on;