
  Blockly.Blocks.SArduino_main= {
    init: function() {
    this.appendDummyInput()
        .appendField("SArduino上传数据");
    this.appendValueInput("NAME")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('SArduino_blocks');
    this.setTooltip("SArduino上传数据");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.SArduino_get= {
    init: function() {
    this.appendDummyInput()
        .appendField("获取SArduino的数据");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('SArduino_blocks');
    this.setTooltip("");
    this.setHelpUrl("");
    }
  };

  