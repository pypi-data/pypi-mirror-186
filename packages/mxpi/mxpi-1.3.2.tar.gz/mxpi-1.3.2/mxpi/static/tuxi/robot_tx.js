Blockly.Blocks.XGO_init= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("XGO初始化，连接串口")
        .appendField(new Blockly.FieldDropdown([["Serial","ttyS0"],["Serial1","ttyAMA1"],["Serial2","ttyAMA2"],["Serial3","ttyAMA3"],["Serial4","ttyAMA4"]]), "NAME")
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("初始化XGO连接");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_action= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 执行")
        .appendField(new Blockly.FieldDropdown([["趴下","1"],["站起","2"],["匍匐前进","3"],["转圈","4"],["原地踏步","5"],["蹲起","6"],["转动Roll","7"],["转动Pitch","8"],["转动Yaw","9"],["三轴转动","10"],["撒尿","11"],["坐下","12"],["招手","13"],["伸懒腰","14"],["波浪","15"],["左右摇摆","16"],["求食","17"],["觅食","18"],["握手","19"]]), "M")
        .appendField(" 动作");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO执行内置动作");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_reset= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 恢复初始状态");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO初始化状态");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_move_x= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 前后运动 步幅");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("mm");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO前后移动，步幅范围:-25mm~25mm");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_move_y= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 左右运动 步幅");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("mm");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO前后移动，步幅范围:-18mm~18mm");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_mark_time= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 腿抬高");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("mm 进行原地踏步");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO的腿抬高指定高度在原地踏步,抬腿范围:10mm~25mm");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_translation_z= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 站立高度");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("mm");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO的站立高度,高度范围:60mm~110mm");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_stop= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 停止运动");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("停止XGO的运动(前后、左右、转向、踏步、往复运动)");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_translation_x= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 前后平动");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("mm");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO前后平动，范围:-25mm~25mm");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_translation_y= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 左右平动");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("mm");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("XGO前后平动，范围:-18mm~18mm");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_periodic_tran= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 在 ")
        .appendField(new Blockly.FieldDropdown([["X轴","x"],["Y轴","y"],["Z轴","z"]]), "M")
        .appendField(" 方向以");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("秒周期运动");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("使XGO周期性平动,周期范围:1.5~8s");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_attitude= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 绕")
        .appendField(new Blockly.FieldDropdown([["X轴(-12°-12°)","r"],["Y轴(-20°-20°)","p"],["Z轴(-12°-12°)","y"]]), "M");
    this.appendValueInput("STEP")
        .setCheck(null)
        .appendField("旋转");
    this.appendDummyInput()
        .appendField(" °");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("使XGO足端不动，身体进行三轴转动");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_periodic_rot= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 绕 ")
        .appendField(new Blockly.FieldDropdown([["X轴","r"],["Y轴","p"],["Z轴","y"]]), "M")
        .appendField(" 以");
    this.appendValueInput("STEP")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("秒周期转动");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("使XGO周期性转动,周期范围:1.5~8s");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_imu= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 设置陀螺仪(自稳功能) ")
        .appendField(new Blockly.FieldDropdown([["打开","1"],["关闭","0"]]), "M");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("开启/关闭XGO自稳状态");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_perform= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" ")
        .appendField(new Blockly.FieldDropdown([["打开","1"],["关闭","0"]]), "M")
        .appendField(" 表演模式");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("开启/关闭XGO的表演模式");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_read_battery= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 的电量");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("获取XGO的电量");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.XGO_read_imu= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/luwu.png", 20, 20, "*"))
        .appendField("")
        .appendField(new Blockly.FieldTextInput("xgo"), "NAME")
        .appendField(" 陀螺仪")
        .appendField(new Blockly.FieldDropdown([["X轴","read_roll()"],["Y轴","read_pitch()"],["Z轴","read_yaw()"]]), "M")
        .appendField("的值");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('robot_blocks');
    this.setTooltip("获取XGO陀螺仪的角度");
    this.setHelpUrl("");
    }
  };


