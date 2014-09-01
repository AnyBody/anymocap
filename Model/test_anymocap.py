
def test_anymocap(anytest):
    loadcmd = anytest.load_macro('AnyMocapModel.any',define={'JOINT_AND_DRIVERS_OPTIMIZED':0})
    macro = [[loadcmd]]
    
    outputlist = anytest.app.start_macro(macro)
    
    for output in outputlist:
        assert 'ERROR' not in output, output['ERROR']

    
    
    