k1 = 0;
k2 = 1;
x1 = 0 + 1;
x2 = 1 + 1;
N = 2;
D = dftmtx(N);
xn = [ 2, 4 ];
xn = transpose(xn);
Xk = D * xn
magXk = abs(Xk)
phaseXk = angle(Xk) * 180 / pi


p3a = ((2 * k1) / N);
fprintf("\nProblem 3a: %f", p3a)

p3b = (((2 * k2) / N)) * 500;
fprintf("\nProblem 3b: %f", p3b)

p3c = magXk(x1);
fprintf("\nProblem 3c: %f", p3c)

p3d = phaseXk(x2);
fprintf("\nProblem 3d: %f\n", p3d)