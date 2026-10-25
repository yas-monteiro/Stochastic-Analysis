x = 0;
N = 10000;
sigma = 6;
burn_in = 2000;

a_val=10;
b_val=12;

f = @(x)exp(-x^2/a_val)/exp(-x^2/b_val);

sum_f = 0;
count = 0;
samples = [];
rate_a = 0;

for k = 1:N
  eps_val = sigma*randn();
  x_new = x+eps_val;
  if x_new >= -10 && x_new <= 10
    delta_sq = (x_new^2) - (x^2);

    if delta_sq <= 0
      x = x_new;
      rate_a = rate_a + 1;

    else
      accept = rand();
      if accept <= exp(-delta_sq/b_val)
        x = x_new;
        rate_a = rate_a + 1;
      endif
    endif

samples = [samples, x];

  if k > burn_in
    sum_f = sum_f + f(x);
    count = count + 1;
  endif
 endif

endfor

running_mean = cumsum(samples) ./ (1:length(samples));
plot(running_mean)

result = sum_f/count;

true_result = integral(@(x) exp(-x.^2/a_val), -10, 10) / integral(@(x) exp(-x.^2/b_val), -10, 10);
fprintf('Estimated value: %.6f\n', result);
fprintf('True value: %.6f\n', true_result);
fprintf('Absolute Error: %.6f\n', abs(true_result - result));

fprintf('Rate of Acceptance: %.2f\n', rate_a/N);
