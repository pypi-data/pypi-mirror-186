Blockly.Python.Dfrobot_UNIHIKER_drawtext = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=Blockly.Python.valueToCode(this,'TEXTS',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var size=Blockly.Python.valueToCode(this,'SIZE',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_text(text='+name+',x='+x+',y='+y+',font_size='+size+', color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_digit = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=Blockly.Python.valueToCode(this,'TEXTS',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var size=Blockly.Python.valueToCode(this,'SIZE',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_digit(text='+name+',x='+x+',y='+y+',font_size='+size+', color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_image = function() {
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var image=Blockly.Python.valueToCode(this,'IMAGE',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.draw_image(image='+image+',x='+x+',y='+y+')\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_emoji = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=this.getFieldValue('NAME')
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var time=Blockly.Python.valueToCode(this,'TIME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.draw_emoji(emoji="'+name+'",x='+x+',y='+y+',duration='+time+')\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_add_button = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=Blockly.Python.valueToCode(this,'TEXTS',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var w=Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h=Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var ck=Blockly.Python.valueToCode(this,'CK',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.add_button(text='+name+',x='+x+',y='+y+',w='+w+',h='+h+',onclick='+ck+')\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_clock = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_clock(x='+x+',y='+y+',r='+l+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_fill_clock = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var bcolor=this.getFieldValue('BCOLOR')
    var tcolor=this.getFieldValue('TCOLOR')
    var code='UNIHIKER_gui.fill_clock(x='+x+',y='+y+',r='+l+',color="'+bcolor+'",fill="'+tcolor+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_qr_code = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var text=Blockly.Python.valueToCode(this,'TEXT',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.draw_qr_code(text='+text+',x='+x+',y='+y+',w='+l+')\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_line = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var ex=Blockly.Python.valueToCode(this,'EX',Blockly.Python.ORDER_ASSIGNMENT);
    var ey=Blockly.Python.valueToCode(this,'EY',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_line(x0='+x+',y0='+y+',x1='+ex+',y1='+ey+',width='+l+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_rect = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var w=Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h=Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_rect(x='+x+',y='+y+',w='+w+',h='+h+',width='+l+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_fill_rect = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var w=Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h=Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.fill_rect(x='+x+',y='+y+',w='+w+',h='+h+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_round_rect = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var w=Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h=Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var r=Blockly.Python.valueToCode(this,'R',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_round_rect(x='+x+',y='+y+',w='+w+',h='+h+',r='+r+',width='+l+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_fill_round_rect = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var w=Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h=Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var r=Blockly.Python.valueToCode(this,'R',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.fill_round_rect(x='+x+',y='+y+',w='+w+',h='+h+',r='+r+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_draw_circle = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var r=Blockly.Python.valueToCode(this,'R',Blockly.Python.ORDER_ASSIGNMENT);
    var l=Blockly.Python.valueToCode(this,'L',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.draw_circle(x='+x+',y='+y+',r='+r+',width='+l+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_fill_circle = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var x=Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y=Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var r=Blockly.Python.valueToCode(this,'R',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='UNIHIKER_gui.fill_circle(x='+x+',y='+y+',r='+r+',color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var num=Blockly.Python.valueToCode(this,'NUM',Blockly.Python.ORDER_ASSIGNMENT);
    var mod=this.getFieldValue('MOD')
    var code='.config('+mod+'='+num+')\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_text = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var text=Blockly.Python.valueToCode(this,'TEXT',Blockly.Python.ORDER_ASSIGNMENT);
    var code='.config(text='+text+')\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_color = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var color=this.getFieldValue('COLOR')
    var code='.config(color="'+color+'")\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_color_RGB = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var R=Blockly.Python.valueToCode(this,'R',Blockly.Python.ORDER_ASSIGNMENT);
    var G=Blockly.Python.valueToCode(this,'G',Blockly.Python.ORDER_ASSIGNMENT);
    var B=Blockly.Python.valueToCode(this,'B',Blockly.Python.ORDER_ASSIGNMENT);
    var code='.config(color=('+R+','+G+','+B+'))\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_clock = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var h=Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var m=Blockly.Python.valueToCode(this,'M',Blockly.Python.ORDER_ASSIGNMENT);
    var s=Blockly.Python.valueToCode(this,'S',Blockly.Python.ORDER_ASSIGNMENT);
    var code='.config(h='+h+',m='+m+',s='+s+')\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_click = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var def=Blockly.Python.valueToCode(this,'DEF',Blockly.Python.ORDER_ASSIGNMENT);
    if(def='unnamed'){
        def=null
    }
    var code='.config(onclick='+def+')\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_image = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var image=Blockly.Python.valueToCode(this,'IMAGE',Blockly.Python.ORDER_ASSIGNMENT);
    var code='.config(image='+image+')\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_emoji = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=this.getFieldValue('NAME')
    var code='.config(emoji="'+name+'")\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_Up_config_button_state = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=this.getFieldValue('NAME')
    var code='.config(state="'+name+'")\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_del = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var code='.remove()\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_del_all = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var code='UNIHIKER_gui.clear()\n'
    if(names!='unnamed'){
        code=names+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_mouse_move = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var name=Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.on_mouse_move('+name+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_AB_click = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var name=Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var ab=this.getFieldValue('AB')
    var code='UNIHIKER_gui.on_'+ab+'_click('+name+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_KEY_click = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var key=Blockly.Python.valueToCode(this,'KEY',Blockly.Python.ORDER_ASSIGNMENT);
    var name=Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.on_key_click('+key+','+name+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_wait_AB = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var ab=this.getFieldValue('AB')
    var code='UNIHIKER_gui.wait_'+ab+'_click()\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_start_thread = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var name=Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.start_thread('+name+')\n'
    if(names!='unnamed'){
        code=names+' = '+code
    }
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_stop_thread = function() {
    Blockly.Python.definitions_['unihiker_GUI'] = 'from unihiker import GUI';
    Blockly.Python.setups_['UNIHIKER_gui'] = 'UNIHIKER_gui=GUI()';
    var names=Blockly.Python.valueToCode(this,'NAMES',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_gui.stop_thread('+names+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_button_is_pressed = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var ab=this.getFieldValue('AB')
    var code='(button_'+ab+'.is_pressed()==True)'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_light_read = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var code='light.read()'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_audio_read = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var code='UNIHIKER_audio.sound_level()'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_accelerometer = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var ab=this.getFieldValue('AB')
    var code='accelerometer.get_'+ab+'()'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_gyroscope = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var ab=this.getFieldValue('AB')
    var code='gyroscope.get_'+ab+'()'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_buzzer_play = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var mod=this.getFieldValue('MOD')
    var code='buzzer.play(buzzer.'+name+',buzzer.'+mod+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_buzzer_set_tempo = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var o=Blockly.Python.valueToCode(this,'O',Blockly.Python.ORDER_ASSIGNMENT);
    var p=Blockly.Python.valueToCode(this,'P',Blockly.Python.ORDER_ASSIGNMENT);
    var code='buzzer.set_tempo('+o+','+p+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_buzzer_pitch = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var pai=this.getFieldValue('PAI')
    var code='buzzer.pitch('+name+','+pai+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_buzzer_pitch_d = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var code='buzzer.pitch('+name+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_buzzer_pitch_stop = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var code='buzzer.stop()\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_buzzer_redirect = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var code='buzzer.redirect(Pin.'+name+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_pin_pin = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var code='Pin((Pin.'+name+'))\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_pin_read = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    Blockly.Python.setups_['pin_read'] = 'p_'+name+'_in=Pin(Pin.'+name+', Pin.IN)';
    var code='(p_'+name+'_in.read_digital()==True)'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_pin_readADC = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    Blockly.Python.setups_['pin_readADC'] = 'p_'+name+'_analog=Pin(Pin.'+name+', Pin.ANALOG)';
    var code='p_'+name+'_analog.read_analog()'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_pin_set = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var mod=this.getFieldValue('MOD')
    var code='p_'+name+'_out=Pin(Pin.'+name+', Pin.OUT)\np_'+name+'_out.write_digital('+mod+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_pin_setPWM = function() {
    Blockly.Python.definitions_['pinpong_unihiker'] = 'from pinpong.extension.unihiker import *'
    Blockly.Python.definitions_['pinpong_board'] = 'from pinpong.board import Board,Pin';
    Blockly.Python.setups_['pinpong_board'] = 'Board().begin()';
    var name=this.getFieldValue('NAME')
    var num=Blockly.Python.valueToCode(this,'NUM',Blockly.Python.ORDER_ASSIGNMENT);
    var code='p_'+name+'_pwm=Pin(Pin.'+name+', Pin.PWM)\np_'+name+'_pwm.write_analog('+num+')\n'
    return code;
  };
  
  Blockly.Python.Dfrobot_UNIHIKER_audio_record = function() {
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio'
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var time=Blockly.Python.valueToCode(this,'TIME',Blockly.Python.ORDER_ASSIGNMENT);
    var url=Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_audio.record('+url+','+time+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_audio_play = function() {
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio'
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var url=Blockly.Python.valueToCode(this,'URL',Blockly.Python.ORDER_ASSIGNMENT);
    var code='UNIHIKER_audio.start_play('+url+')\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_audio_play_time_remain = function() {
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio'
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var code='UNIHIKER_audio.play_time_remain()'
    return [code, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python.Dfrobot_UNIHIKER_audio_pause = function() {
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio'
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var code='UNIHIKER_audio.pause_play()\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_audio_resume = function() {
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio'
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var code='UNIHIKER_audio.resume_play()\n'
    return code;
  };

  Blockly.Python.Dfrobot_UNIHIKER_audio_stop = function() {
    Blockly.Python.definitions_['unihiker_Audio'] = 'from unihiker import Audio'
    Blockly.Python.setups_['unihiker_Audio'] = 'UNIHIKER_audio = Audio()';
    var code='UNIHIKER_audio.stop_play()\n'
    return code;
  };




  

 

  
