
def test_anymocap(anytest):
    loadcmd = anytest.load_macro('AnyMocapModel.any',
                                 define={'FORCE_MODEL_LOAD_WHEN_DATA_FILES_ARE_MISSING':0})
    macro = [[loadcmd]]
    
    outputlist = anytest.app.start_macro(macro)
    
    anytest.check_output_log(outputlist)
    
    
    