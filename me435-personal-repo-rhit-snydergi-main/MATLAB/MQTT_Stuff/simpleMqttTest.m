function simpleMqttTest()
clc
mqClient = mqttclient("tcp://broker.hivemq.com");
subscribe(mqClient,'my_messages',"Callback",@myCallback);
for k = 1:3
    message = sprintf('{"type": "chat", "payload": "snydergi %d"}', k);
    write(mqClient,'my_messages',message);
    pause(2);
    
end
unsubscribeAll(mqClient);
end

function myCallback(topic,message)
messageCell = jsondecode(message);
messageType = messageCell.type;
messagePayload = messageCell.payload;
% fprintf(messagePayload);
end