def displayMsg(oled, DisplayMode,Msg):
    
    # Display-specific Parameters:
    if oled.width==128 and oled.height==64:
        NoLineMax=8
        StrLengthMax=16
    
    # Display-mode Settings:
    if DisplayMode["Type"]=="DisplaybyLine":
        oled.text(Msg,0,mode_parameters["LineNo"]+1,1)
        oled.show()
        
        