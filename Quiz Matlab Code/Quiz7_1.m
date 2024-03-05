k1 = 4;
k2 = 3;
x1 = 1 + 1;
x2 = 1 + 1;
N = 6;
D = dftmtx(N);
xn = [ 1, 0, 0, 2, 0, 0 ];
% xn = transpose(xn);
Xk = D * xn'
magXk = abs(Xk)
phaseXk = angle(Xk) * 180/pi
magXk = abs(Xk);
phaseXk = angle(Xk) * 180/pi;

p1a = ((2 * k1) / N) - 2;
fprintf("\nProblem 1a: %f", p1a)

p1b = (((2 * k2) / N) - 2) * 500;
fprintf("\nProblem 1b: %f", p1b)

p1c = magXk(x1);
fprintf("\nProblem 1c: %f", p1c)

p1d = phaseXk(x2);
fprintf("\nProblem 1d: %f\n", p1d)