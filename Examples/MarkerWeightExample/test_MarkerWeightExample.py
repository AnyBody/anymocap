

def test(AnyFixture):
    mg = AnyFixture.MacroGenerator()
    path_kw = {'AMMR_PATH':AnyFixture.ammr,
               'ANYMOCAP':AnyFixture.anymocap,
               'TEMP_PATH': "."}
    mg.add_load('Main.any', path_kw= path_kw)
    macro = mg.generate_macros()
    
    outputlist = AnyFixture.app.start_macro(macro)
    
    for output in outputlist:
        assert 'ERROR' not in output, output['ERROR']
    
    
    