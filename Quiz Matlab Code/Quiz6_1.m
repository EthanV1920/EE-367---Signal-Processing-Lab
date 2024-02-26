% Filter Coefficients
coeff = [-0.2926, 0.325, -0.2926];

% Sampling Frequency
Fs = 1000;

% Vector for plotting
f = linspace(0, Fs/2, 1000);

% Frequency Response
[H, w] = freqz(coeff, 1, f, Fs);

% Find magnitude
magH = abs(H);
peakMag = max(magH);

% Find cutoff frequency
cutoff = find(magH >= peakMag/sqrt(2), 1, 'first');
cutoffFreq = f(cutoff)
cutoffFreqNorm = cutoffFreq / (Fs/2)

% Plot the magnitude response
figure();
hold on;
plot(f, abs(H));
title('Magnitude Response of the Filter');
xlabel('Frequency (Hz)');
ylabel('Magnitude');
grid on;

% Find the first zero crossing
[~, idx] = min(abs(H));
f1 = f(idx)

plot(f1, abs(H(idx)), 'ro');
legend('Magnitude Response', 'First Zero Crossing');

plot(cutoffFreq, magH(cutoff), 'go');
legend('Magnitude Response', 'First Zero Crossing', 'Cutoff Frequency');

% Percent error in cutoff frequency
theoreticalCutoff = 375;
error = (( cutoffFreq - theoreticalCutoff) / theoreticalCutoff ) * 100