
def test(anytest):
    mg = anytest.macro_gen
    loadcmd = anytest.load_macro('Main.any')
    mg.add_macro( loadcmd )
    macro = mg.generate_macros()
    
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)  

    
    
    