

Blockly.Blocks.Dfrobot_UNIHIKER_drawtext= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("TEXTS")
        .setCheck(null)
        .appendField("显示文字");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("SIZE")
        .setCheck(null)
        .appendField("字号");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示文字");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_digit= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("TEXTS")
        .setCheck(null)
        .appendField("显示仿数码管字体");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("SIZE")
        .setCheck(null)
        .appendField("字号");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示仿数码字体");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_image= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("IMAGE")
        .setCheck(null)
        .appendField("显示图片");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示图片");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_emoji= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendDummyInput()
        .appendField("显示内置动态表情")
        .appendField(new Blockly.FieldDropdown([["愤怒","Angry"],["紧张","Nerve"],["平静","Peace"],["惊讶","Shock"],["睡觉","Sleep"],["微笑","Smile"],["冒汗","Sweat"],["思考","Think"],["眨眼","Wink"]]), "NAME");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("TIME")
        .setCheck(null)
        .appendField("间隔");
    this.appendDummyInput()
        .appendField("秒");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示内置动态表情");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_add_button= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("TEXTS")
        .setCheck(null)
        .appendField("增加按钮");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("W")
        .setCheck(null)
        .appendField("宽");
    this.appendValueInput("H")
        .setCheck(null)
        .appendField("高");
    this.appendValueInput("CK")
        .setCheck(null)
        .appendField("点击回调函数");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上增加按钮");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_clock= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示时钟")
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("半径");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示时钟");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_fill_clock= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示填充时钟")
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("半径");
    this.appendDummyInput()
        .appendField("边框颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "BCOLOR");
    this.appendDummyInput()
        .appendField("填充颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "TCOLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示时钟");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_qr_code= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("TEXT")
        .setCheck(null)
        .appendField("显示二维码 内容");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("边长");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("显示二维码");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_line= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示线段 起点X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("EX")
        .setCheck(null)
        .appendField("终点X");
    this.appendValueInput("EY")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("线宽");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示线条");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_rect= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示矩形 在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("W")
        .setCheck(null)
        .appendField("宽");
    this.appendValueInput("H")
        .setCheck(null)
        .appendField("高");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("线宽");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示矩形");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_fill_rect= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示填充矩形 在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("W")
        .setCheck(null)
        .appendField("宽");
    this.appendValueInput("H")
        .setCheck(null)
        .appendField("高");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示填充矩形");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_round_rect= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示圆角矩形 在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("W")
        .setCheck(null)
        .appendField("宽");
    this.appendValueInput("H")
        .setCheck(null)
        .appendField("高");
    this.appendValueInput("R")
        .setCheck(null)
        .appendField("圆角半径");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("线宽");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示圆角矩形");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_fill_round_rect= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示圆角矩形 在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("W")
        .setCheck(null)
        .appendField("宽");
    this.appendValueInput("H")
        .setCheck(null)
        .appendField("高");
    this.appendValueInput("R")
        .setCheck(null)
        .appendField("圆角半径");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示圆角矩形");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_draw_circle= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示圆形 在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("R")
        .setCheck(null)
        .appendField("半径");
    this.appendValueInput("L")
        .setCheck(null)
        .appendField("线宽");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示圆形");
    this.setHelpUrl("");
    }
  };
  
  Blockly.Blocks.Dfrobot_UNIHIKER_fill_circle= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("对象");
    this.appendValueInput("X")
        .setCheck(null)
        .appendField("显示填充圆形 在X");
    this.appendValueInput("Y")
        .setCheck(null)
        .appendField("Y");
    this.appendValueInput("R")
        .setCheck(null)
        .appendField("半径");
    this.appendDummyInput()
        .appendField("颜色")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("在行空板上显示填充圆形");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新对象");
    this.appendDummyInput()
        .appendField("的数字参数")
        .appendField(new Blockly.FieldDropdown([["x","x"],["y","y"],["宽","w"],["高","h"],["半径","r"],["线宽","width"],["起始点x","x0"],["起始点y","y0"],["终止点x","x1"],["终止点y","y1"],["字体大小","font_size"]]), "MOD");
    this.appendValueInput("NUM")
        .setCheck(null)
        .appendField("为");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新对象的参数");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_text= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新对象");
    this.appendValueInput("TEXT")
        .setCheck(null)
        .appendField("的文本内容参数为");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新对象的文本");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_color= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新对象");
    this.appendDummyInput()
        .appendField("的颜色为")
        .appendField(new Blockly.FieldColour("#ff6600"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新对象的颜色");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_color_RGB= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新对象");
    this.appendValueInput("R")
        .setCheck(null)
        .appendField("的颜色为 红");
    this.appendValueInput("G")
        .setCheck(null)
        .appendField("绿");
    this.appendValueInput("B")
        .setCheck(null)
        .appendField("蓝");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新对象的颜色");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_clock= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新时钟对象");
    this.appendValueInput("H")
        .setCheck(null)
        .appendField("的时间为");
    this.appendValueInput("M")
        .setCheck(null)
        .appendField("时");
    this.appendValueInput("S")
        .setCheck(null)
        .appendField("分");
    this.appendDummyInput()
      .appendField("秒")
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新对象的时间");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_click= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新对象");
    this.appendValueInput("DEF")
        .setCheck(null)
        .appendField("的点击调用函数为");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("绑定单击对象的回调函数");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_image= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新图片对象");
    this.appendValueInput("IMAGE")
        .setCheck(null)
        .appendField("图片源为");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新对象的图片");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_emoji= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新表情对象");
        this.appendDummyInput()
        .appendField("表情源为")
        .appendField(new Blockly.FieldDropdown([["愤怒","Angry"],["紧张","Nerve"],["平静","Peace"],["惊讶","Shock"],["睡觉","Sleep"],["微笑","Smile"],["冒汗","Sweat"],["思考","Think"],["眨眼","Wink"]]), "NAME");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新表情");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_Up_config_button_state= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("更新按钮对象");
    this.appendDummyInput()
        .appendField("为")
        .appendField(new Blockly.FieldDropdown([["启用","normal"],["禁用","disable"]]), "NAME");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("更新按钮状态");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_del= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("删除对象");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("删除对象");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_del_all= {
    init: function() {
    this.appendDummyInput()
      .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
      .appendField("删除所有对象")
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("删除所有对象");
    this.setHelpUrl("");
    }
  }; 

  Blockly.Blocks.Dfrobot_UNIHIKER_mouse_move= {
    init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("当鼠标移动,绑定回调函数");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("当鼠标移动,绑定回调函数,函数需要两个参数x,y");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_AB_click= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("当按下")
        .appendField(new Blockly.FieldDropdown([["A","a"],["B","b"]]), "AB");
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("执行回调函数");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("当鼠标移动,绑定回调函数");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_KEY_click= {
    init: function() {
    this.appendValueInput("KEY")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("当键盘按键");
    this.appendDummyInput()
        .appendField("被按下,")
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("执行回调函数");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("当鼠标移动,绑定回调函数");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_wait_AB= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("等待直到按键")
        .appendField(new Blockly.FieldDropdown([["A","a"],["B","b"]]), "AB");
        this.appendDummyInput()
        .appendField("被按下")
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("等待到A/B被按下");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_start_thread= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("启动多线程对象");
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("运行回调函数");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("启动多线程对象,运行回调函数");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_stop_thread= {
    init: function() {
    this.appendValueInput("NAMES")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("停止多线程对象");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("停止多线程对象");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_button_is_pressed= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("按钮")
        .appendField(new Blockly.FieldDropdown([["A","a"],["B","b"]]), "AB");
    this.appendDummyInput()
        .appendField("被按下？");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("判断板载按钮是否被按下");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_light_read= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("读取环境光强度")
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("读取环境光强度");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_read= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("读取麦克风声音强度")
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("读取麦克风声音强度");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_accelerometer= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("读取加速度的")
        .appendField(new Blockly.FieldDropdown([["x","x"],["y","y"],["z","z"],["强度","strength"]]), "AB");
    this.appendDummyInput()
        .appendField("值");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("读取加速度的值");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_gyroscope= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("读取陀螺仪的")
        .appendField(new Blockly.FieldDropdown([["x","x"],["y","y"],["z","z"]]), "AB");
    this.appendDummyInput()
        .appendField("值");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("读取陀螺仪的值");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_buzzer_play= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("播放音乐")
        .appendField(new Blockly.FieldDropdown([["DADADADUM","DADADADUM"],["ENTERTAINER","ENTERTAINER"],["PRELUDE","PRELUDE"],["ODE","ODE"],["NYAN","NYAN"],["RINGTONE","RINGTONE"],["FUNK","FUNK"],["BLUES","BLUES"],["BIRTHDAY","BIRTHDAY"],["WEDDING","WEDDING"],["FUNERAL","FUNERAL"],["PUNCHLINE","PUNCHLINE"],["BADDY","BADDY"],["CHASE","CHASE"],["BA_DING","BA_DING"],["WAWAWAWAA","WAWAWAWAA"],["JUMP_UP","JUMP_UP"],["JUMP_DOWN","JUMP_DOWN"],["POWER_UP","POWER_UP"],["POWER_DOWN","POWER_DOWN"]]), "NAME")
        .appendField("重复")
        .appendField(new Blockly.FieldDropdown([["播放一次","Once"],["无限循环","Forever"],["在后台播放一次","OnceInBackground"],["在后台无限循环","ForeverInBackground"]]), "MOD");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("板载蜂鸣器播放音乐");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_buzzer_set_tempo= {
    init: function() {
    this.appendValueInput("O")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("播放音符");
    this.appendValueInput("P")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("拍");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("播放指定音符");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_buzzer_pitch= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("播放音符")
        .appendField(new Blockly.FieldDropdown([["C3","131"],["D3","147"],["E3","165"],["F3","175"],["G3","196"],["A3","220"],["B3","247"],["C4","262"],["D4","294"],["E4","330"],["F4","349"],["G4","392"],["A4","440"],["B4","494"],["C5","532"],["D5","587"],["E5","659"],["F5","698"],["G5","784"],["A5","880"],["B5","988"],["C6","1047"],["D6","1175"],["E6","1319"],["F6","1397"],["G6","1568"],["A6","1760"],["B6","1976"],["C7","2093"],["D7","2349"],["E7","2637"],["F7","2794"],["G7","3136"],["A7","3520"],["B7","3951"]]), "NAME")
        .appendField(new Blockly.FieldDropdown([["1/4","1"],["1/2","2"],["3/4","3"],["1","4"],["3/2","6"],["2","8"],["3","12"],["4","16"]]), "PAI");
    this.appendDummyInput()
        .appendField("拍");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("播放指定音符");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_buzzer_pitch_d= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("后台播放音符")
        .appendField(new Blockly.FieldDropdown([["C3","131"],["D3","147"],["E3","165"],["F3","175"],["G3","196"],["A3","220"],["B3","247"],["C4","262"],["D4","294"],["E4","330"],["F4","349"],["G4","392"],["A4","440"],["B4","494"],["C5","532"],["D5","587"],["E5","659"],["F5","698"],["G5","784"],["A5","880"],["B5","988"],["C6","1047"],["D6","1175"],["E6","1319"],["F6","1397"],["G6","1568"],["A6","1760"],["B6","1976"],["C7","2093"],["D7","2349"],["E7","2637"],["F7","2794"],["G7","3136"],["A7","3520"],["B7","3951"]]), "NAME");
    this.appendDummyInput();
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("播放指定音符");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_buzzer_pitch_stop= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("停止后台播放");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("停止播放");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_buzzer_redirect= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("蜂鸣器重定向到指定引脚")
        .appendField(new Blockly.FieldDropdown([["P21(~A)","P21"],["P22(~A)","P22"],["P23(~)","P23"],["P0(~A)","P0"],["P2(~A)","P2"],["P3(~A)","P3"],["P8(~)","P8"],["P9(~)","P9"],["P10(~A)","P10"],["P16(~)","P16"]]), "NAME");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("停止播放");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_pin_pin= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("行空板引脚")
        .appendField(new Blockly.FieldDropdown([["P25(L)","P25"],["P21(~A)","P21"],["P22(~A)","P22"],["P23(~)","P23"],["P24","P24"],["P26(Buzzer)","P26"],["P27(A键)","P27"],["P28(B键)","P28"],["P0(~A)","P0"],["P1(A)","P1"],["P2(~A)","P2"],["P3(~A)","P3"],["P4(A)","P4"],["P5","P5"],["P6","P6"],["P7","P7"],["P8(~)","P8"],["P9(~)","P9"],["P10(~A)","P10"],["P11","P11"],["P12","P12"],["P13","P13"],["P14","P14"],["P15","P15"],["P16(~)","P16"],["P19","P19"],["P20","P20"]]), "NAME");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("引脚编号");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_pin_read= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("读取数字引脚")
        .appendField(new Blockly.FieldDropdown([["P21(~A)","P21"],["P22(~A)","P22"],["P23(~)","P23"],["P24","P24"],["P0(~A)","P0"],["P1(A)","P1"],["P2(~A)","P2"],["P3(~A)","P3"],["P4(A)","P4"],["P5","P5"],["P6","P6"],["P7","P7"],["P8(~)","P8"],["P9(~)","P9"],["P10(~A)","P10"],["P11","P11"],["P12","P12"],["P13","P13"],["P14","P14"],["P15","P15"],["P16(~)","P16"]]), "NAME");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("引脚编号");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_pin_readADC= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("读取模拟引脚(ADC)")
        .appendField(new Blockly.FieldDropdown([["P21(~A)","P21"],["P22(~A)","P22"],["P0(~A)","P0"],["P1(A)","P1"],["P2(~A)","P2"],["P3(~A)","P3"],["P4(A)","P4"],["P10(~A)","P10"]]), "NAME");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("读取模拟引脚");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_pin_set= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("设置数字引脚")
        .appendField(new Blockly.FieldDropdown([["P21(~A)","P21"],["P22(~A)","P22"],["P23(~)","P23"],["P24","P24"],["P0(~A)","P0"],["P1(A)","P1"],["P2(~A)","P2"],["P3(~A)","P3"],["P4(A)","P4"],["P5","P5"],["P6","P6"],["P7","P7"],["P8(~)","P8"],["P9(~)","P9"],["P10(~A)","P10"],["P11","P11"],["P12","P12"],["P13","P13"],["P14","P14"],["P15","P15"],["P16(~)","P16"]]), "NAME")
        .appendField("输出")
        .appendField(new Blockly.FieldDropdown([["低电平","0"],["高电平","1"]]), "MOD");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("设置数字引脚输出高/低电平");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_pin_setPWM= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("设置模拟引脚")
        .appendField(new Blockly.FieldDropdown([["P21(~A)","P21"],["P22(~A)","P22"],["P23(~)","P23"],["P0(~A)","P0"],["P2(~A)","P2"],["P3(~A)","P3"],["P8(~)","P8"],["P9(~)","P9"],["P10(~A)","P10"],["P16(~)","P16"]]), "NAME");
    this.appendValueInput("NUM")
        .setCheck(null)
        .appendField("输出(PWM)");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("模拟引脚输出PWM");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_record= {
    init: function() {
    this.appendValueInput("TIME")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("录音");
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("秒直到结束，文件名");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("录音输出到文件");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_play= {
    init: function() {
    this.appendValueInput("URL")
        .setCheck(null)
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("开始后台播放音频文件");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("后台播放音频文件");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_play_time_remain= {
    init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("获取后台播放音频的剩余时长(秒)");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("获取后台播放音频的剩余时长(秒)");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_pause= {
    init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("暂停后台播放");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("暂停后台播放");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_resume= {
    init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("重新开始后台播放");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("重新开始后台播放");
    this.setHelpUrl("");
    }
  };

  Blockly.Blocks.Dfrobot_UNIHIKER_audio_stop= {
    init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldImage("./static/media/ulogo.png", 20, 20, "*"))
        .appendField("结束后台播放");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setStyle('UNIHIKER_blocks');
    this.setTooltip("结束后台播放");
    this.setHelpUrl("");
    }
  };