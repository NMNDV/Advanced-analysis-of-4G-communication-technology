%% About
clear vars;
close all;
clc;
% Advanded H analysis
%% Load matrix
load advanced_H_analysis.mat;
%% Support matrix generator
support_matrix = [];
for temp = 0:9
    support_matrix = [support_matrix; prob_set.^temp .* (1 - prob_set).^(9 - temp)]; 
end
%% variation analysis
set_selected = [ 1, 9, 36, 84, 117, 81, 0, 0, 0, 0 ];
raw_estimations_ideal = (support_matrix' * set_selected')';
diff14 = sum(abs(raw_estimations4 - raw_estimations1))
diff24 = sum(abs(raw_estimations4 - raw_estimations2))
diff34 = sum(abs(raw_estimations4 - raw_estimations3))
diff1i = sum(abs(raw_estimations_ideal - raw_estimations1))
diff2i = sum(abs(raw_estimations_ideal - raw_estimations2))
diff3i = sum(abs(raw_estimations_ideal - raw_estimations3))
diff4i = sum(abs(raw_estimations_ideal - raw_estimations4))
%% ploting part
figure(1);
plot(prob_set, raw_estimations1, 'y');
hold on;
plot(prob_set, raw_estimations2, 'g');
hold on;
plot(prob_set, raw_estimations3, 'b');
hold on;
plot(prob_set, raw_estimations4, 'r');
hold on;
plot(prob_set, raw_estimations_ideal, 'O');
xlabel('Probability of success');
ylabel('Probability of error');
legend('H1', 'H2', 'H3', 'H\_advanced', 'Theoretical');
title('Advanced H Analysis');