load pmf.mat
p = 0.2;
pestem = [];
for n = 0:20
    pestem = [ pestem, p ^ n * (1 - p) ^ (20 - n) * nchoosek(20, n)];
end
figure(1);
plot(0:length(array) - 1, array);
hold on;
plot(0:length(pestem) - 1, pestem, 'd');
title('PMF n=20 p=0.2');
xlabel('number');
ylabel('Probability of getting a number');
legend('channel','theoretical');
grid on;