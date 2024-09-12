function plateLoaderMenuControl(s)
%plateLoaderMenuControl allows for control of Plate Loader robot from
%MATLAB nested menu.
while(1)
choice = menu('Choose Command','RESET','X-AXIS','Z-AXIS','GRIPPER','MOVE','STATUS','ANKLE BREAKER','EXIT');
if choice == 1
    writeline(s,'RESET');
elseif choice == 2
    choiceX = menu('Choose location to move to','1','2','3','4','5');
    if choiceX == 1
        writeline(s,'X-AXIS 1');
    elseif choiceX == 2
        writeline(s,'X-AXIS 2');
    elseif choiceX == 3
        writeline(s,'X-AXIS 3');
    elseif choiceX == 4
        writeline(s,'X-AXIS 4');
    elseif choiceX == 5
        writeline(s,'X-AXIS 5');
    else
    end
elseif choice == 3
    choiceZ = menu('Z-AXIS:','EXTEND','RETRACT');
    if choiceZ == 1
        writeline(s,'Z-AXIS EXTEND');
    elseif choiceZ == 2
        writeline(s,'Z-AXIS RETRACT');
    else
    end
elseif choice == 4
    choiceG = menu("Gripper Command:",'OPEN','CLOSE');
    if choiceG == 1
        writeline(s,'GRIPPER OPEN');
    elseif choiceG == 2
        writeline(s,'GRIPPER CLOSE');
    else
    end
elseif choice == 5
    choiceM = inputdlg({'Move plate from:','Move plate to:'},'MOVE MENU',[1 35]);
    choiceM = cell2mat(choiceM);
    stringToSend = ['MOVE ',choiceM(1),' ',choiceM(2)];
    writeline(s,stringToSend);
elseif choice == 6
    writeline(s,'LOADER_STATUS');
elseif choice == 7
    writeline(s,'X-AXIS 1');
    readline(s);
    writeline(s,'GRIPPER OPEN');
    readline(s);
    writeline(s,'Z-AXIS EXTEND');
    readline(s);
    writeline(s,'GRIPPER CLOSE');
    readline(s);
    writeline(s,'Z-AXIS RETRACT');
    readline(s);
    writeline(s,'X-AXIS 5');
    readline(s);
    writeline(s,'X-AXIS 1');
    readline(s);
    writeline(s,'GRIPPER OPEN');
elseif choice == 8
    fprintf("Goodbye\n");
    break
else
end
response = readline(s);
pause(.5);
fprintf(response);
end

