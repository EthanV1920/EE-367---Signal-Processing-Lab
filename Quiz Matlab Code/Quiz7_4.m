k1 = 1;
k2 = 7;
x1 = 7 + 1;
x2 = 0 + 1;
N = 8;
D = dftmtx(N);
xn = [ 3, 0, 0, 0, 0, 0, 0, 3 ];
% xn = transpose(xn);
Xk = D * xn'
magXk = abs(Xk)
phaseXk = angle(Xk) * 180 / pi

p4a = ((2 * k1) / N);
fprintf("\nProblem 4a: %f", p4a)

p4b = (((2 * k2) / N) - 2) * 500;
fprintf("\nProblem 4b: %f", p4b)

p4c = magXk(x1);
fprintf("\nProblem 4c: %f", p4c)

p4d = phaseXk(x2);
fprintf("\nProblem 4d: %f\n", p4d)