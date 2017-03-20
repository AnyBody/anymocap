
def test(anytest):
    loadcmd = anytest.load_macro('Main.any',
                                 define={'FORCE_MODEL_LOAD_WHEN_DATA_FILES_ARE_MISSING':0})
    macro = [[ loadcmd, 'exit' ]]
   
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_model_load_failure(outputlist)

    
    
    