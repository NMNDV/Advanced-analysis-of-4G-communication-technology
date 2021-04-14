load ldpcexample.mat;
plot(0:length(error) - 1, error, 'black:*');
title('LDPCBSC example(50 errors, p=0.01)');
xlabel('Number of error');
ylabel('Number of iterations');
xticks(0:5:25)
grid on;