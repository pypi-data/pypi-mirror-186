Blockly.Python['XGO_init'] = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name = this.getFieldValue('NAME')
    var code ='xgolib.XGO("/dev/'+name+'")'
    return [code,Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python.XGO_action = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m = this.getFieldValue('M')
    var code =name+'.action('+m+')\n'
    return code;
};

Blockly.Python.XGO_reset = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var code =name+'.reset()\n'
    return code;
};

Blockly.Python.XGO_move_x = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.move("x",'+step+')\n'
    return code;
};

Blockly.Python.XGO_move_y = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.move("y",'+step+')\n'
    return code;
};

Blockly.Python.XGO_mark_time = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.mark_time('+step+')\n'
    return code;
};

Blockly.Python.XGO_translation_z = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.translation("z",'+step+')\n'
    return code;
};

Blockly.Python.XGO_stop = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var code =name+'.stop()\n'
    return code;
};

Blockly.Python.XGO_translation_x = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.translation("x",'+step+')\n'
    return code;
};

Blockly.Python.XGO_translation_y = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.translation("y",'+step+')\n'
    return code;
};

Blockly.Python.XGO_periodic_tran = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m=this.getFieldValue('M')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.periodic_tran("'+m+'",'+step+')\n'
    return code;
};

Blockly.Python.XGO_attitude = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m=this.getFieldValue('M')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.attitude("'+m+'",'+step+')\n'
    return code;
};

Blockly.Python.XGO_periodic_rot = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m=this.getFieldValue('M')
    var step=Blockly.Python.valueToCode(this,'STEP',Blockly.Python.ORDER_ASSIGNMENT);
    var code =name+'.periodic_rot("'+m+'",'+step+')\n'
    return code;
};

Blockly.Python.XGO_imu = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m=this.getFieldValue('M')
    var code =name+'.imu('+m+')\n'
    return code;
};

Blockly.Python.XGO_perform = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m=this.getFieldValue('M')
    var code =name+'.perform('+m+')\n'
    return code;
};

Blockly.Python.XGO_read_battery = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var code =name+'.read_battery()'
    return [code,Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python.XGO_read_imu = function () {
    Blockly.Python.definitions_['xgolib'] = 'from Mx import xgolib';
    var name=this.getFieldValue('NAME')
    var m=this.getFieldValue('M')
    var code =name+'.'+m
    return [code,Blockly.Python.ORDER_ATOMIC];
};

