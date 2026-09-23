# Yasmin Monteiro e Silva
# HMW 2.7: Numerically investigate the limit proccess

1;

#Functions
function x = p_bin(k, p, n)
  log_x = gammaln(n+1) - gammaln(k+1) - gammaln(n-k+1) + k*log(p) + (n-k)*log(1-p);
  x = exp(log_x);
endfunction

function x = p_poi(k, l)
  x = exp(-l)*l^k/factorial(k);
endfunction

function x = p_nor(k, u, s)
  x = exp(-(k-u)^2/(2*s^2))/sqrt(2*pi*s^2);
endfunction

# Binomial -> Poisson
R = 100;
lambda = 5;
N = 10:10:1000;
Var_bin_poi = [];

for n = N
  p = lambda/n;
  err = [];
  for k = 1:R
    va_b = p_bin(k, p, n);
    va_p = p_poi(k, lambda);
    err(end+1) = abs(va_b - va_p);
    endfor
  Var_bin_poi(end+1) = sum(err)/2;
endfor

subplot(1, 2, 1)
plot(N, Var_bin_poi);
xlabel("Parameter N");
ylabel("Variation Discrepancy");
title("Limit Process Binomial -> Poisson");


# Poisson -> Normal
R = 100;
lambda = 1:10:1000;
Var_poi_norm = [];

for l = lambda
  err = [];
  for k = 1:R
    va_p = p_poi(k, l);
    va_n = p_nor(k, l, l);
    err(end+1) = abs(va_p - va_n);
  endfor
  Var_poi_norm(end+1) = sum(err)/2;
endfor

subplot(1,2,2)
plot(lambda, Var_poi_norm);
xlabel("Parameter lambda");
ylabel("Variation Discrepancy");
title("Limit Process Poisson -> Normal");


