
def test_anymocap(AnyFixture):
    mg = AnyFixture.MacroGenerator()
    def_kw = {'EXCLUDE_OPTIMIZED_DRIVERS':""}
    path_kw = {'AMMR_PATH':AnyFixture.ammr, 'TEMP_PATH': '.'}
    mg.add_load('AnyMocapModel.any', def_kw, path_kw)
    macro = mg.generate_macros()
    
    outputlist = AnyFixture.app.start_macro(macro)
    
    for output in outputlist:
        assert 'ERROR' not in output, output['ERROR']

    
    
    