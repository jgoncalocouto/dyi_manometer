def displayMsg(oled, DisplayMode,Msg):
    
    # Display-specific Parameters:
    if oled.width==128 and oled.height==64:
        NoLineMax=8
        StrLengthMax=16
        
    if "Type" not in DisplayMode:
        raise ValueError("DisplayMode dictionary must contain a 'Type' key")
    
    # Display-mode Settings:
    if DisplayMode["Type"]=="DisplaybyLine":
        
        if len(Msg)>StrLengthMax:
            Msg=Msg[0:StrLengthMax]
            print("Warning: Message too lengthy to be displayed in the desired line. Maximum set of characters displayed, the rest was discarded.")

        if DisplayMode["LineNo"]>NoLineMax-1:
            raise ValueError("Desired line is higher than the Max Line:"+str(NoLineMax)+" | Not displayed")
        
        oled.text(Msg,0,DisplayMode["LineNo"]+1,1)
        oled.show()
        
        