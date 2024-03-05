k1 = 7;
k2 = 5;
x1 = 2 + 1;
x2 = 1 + 1;
N = 8
D = dftmtx(N);
xn = [ 2, 0, 0, 0, 0, 0, 2, 0 ];
% xn = transpose(xn);
Xk = D * xn'
magXk = abs(Xk);
phaseXk = angle(Xk) * 180/pi;

p2a = ((2 * k1) / N) - 2;
fprintf("\nProblem 2a: %f", p2a)

p2b = (((2 * k2) / N) - 2) * 500;
fprintf("\nProblem 2b: %f", p2b)

p2c = magXk(x1);
fprintf("\nProblem 2c: %f", p2c)

p2d = phaseXk(x2);
fprintf("\nProblem 2d: %f\n", p2d)