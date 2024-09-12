function mqttCallback(topic,message)
messageCell = jsondecode(message)
messageType = messageCell.type
messagePayload = messageCell.payload
% app.ReceivedText.Text = messagePayload
end

