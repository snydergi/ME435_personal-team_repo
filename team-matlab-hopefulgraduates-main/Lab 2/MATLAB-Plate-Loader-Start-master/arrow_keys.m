clc;
clear all;
close all;
rng('shuffle');

% useful command, waits here until all keys on the keyboard are released
KbReleaseWait;

% lets define out target keys, this also gets the ASCII or numeric index for they key
k1 = 'a';
k2 = 'l';
keyOne = KbName(k1);
keyTwo = KbName(k2);

% start an infinite loop
while 1
      
      % read the current status of the keyboard
      [keyIsDown, secs, keyCode] = KbCheck;
​      % this returns some key information
      % keyIsDown is a variable that is a 1 if a key is pressed and 0 if no key is pressed
      % secs is the time of the key press
      % keyCode is a vector for each key, a 1 will appear in the vector for the key that has been pressed

     % this is a logic test, if the value of keyCode corresponding to 'a' is pressed
     if keyCode(keyOne) == 1
           disp([k1 ' was pressed']);
           break;
     end
     if keyCode(keyTwo) == 1
           disp([k2 ' was pressed']);
           break;
    end

end 
