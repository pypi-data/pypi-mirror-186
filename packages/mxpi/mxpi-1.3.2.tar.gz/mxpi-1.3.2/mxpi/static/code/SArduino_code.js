Blockly.Python.SArduino_main=function(a){
    Blockly.Python.definitions_['SArduino'] = 'from Mx import SArduino';
    var data = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code= 'SArduino.send_to('+data+')\n';
    return code;
}


Blockly.Python.SArduino_get=function(a){
    Blockly.Python.definitions_['SArduino'] = 'from Mx import SArduino';
    var code= 'SArduino.send_get()\n';
    return [code,Blockly.Python.ORDER_ATOMIC];
}