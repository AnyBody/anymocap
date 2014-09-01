
def test_static(anytest):
    mg = anytest.macro_gen
    loadcmd = anytest.load_macro('Subject_1/Static/Main.any')
    mg.add_macro( loadcmd )
    macro = mg.generate_macros()
    
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)  

def test_walk(anytest):
    mg = anytest.macro_gen
    loadcmd = anytest.load_macro('Subject_1/Walk/Main.any')
    mg.add_macro( loadcmd )
    macro = mg.generate_macros()
    
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)  
