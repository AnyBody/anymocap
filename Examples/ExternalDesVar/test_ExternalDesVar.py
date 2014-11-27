
def test(anytest):
    loadcmd = anytest.load_macro('Main.any')
    macro = [[ loadcmd, 'exit' ]]
   
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)  
    
    
    
    