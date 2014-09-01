
def test(anytest):
    macro = [[anytest.load_macro('gait_ifb/Main.any'),
              'exit']]
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)  

    
    
    