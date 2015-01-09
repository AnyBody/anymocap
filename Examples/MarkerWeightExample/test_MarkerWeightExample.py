

def test(anytest):
    macro = [[anytest.load_macro('Main.any')]]
    
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_model_load_failure(outputlist)
    
    