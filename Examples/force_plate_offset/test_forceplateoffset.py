
def test(anytest):
    macro = [[anytest.load_macro('Main.any'),
              'exit']]
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_model_load_failure(outputlist)

    
    
    