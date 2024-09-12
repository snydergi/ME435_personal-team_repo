clear all;
clc

fprintf('Connecting to robot...');
portStr = '/dev/tty.usbserial';
s = serialport('COM3', 19200, "Timeout", 15);
writeline(s,'INITIALIZE');
readline(s)
fprintf('Ready\n');

plateLoaderMenuControl(s);
