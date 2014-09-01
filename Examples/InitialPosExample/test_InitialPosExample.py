import os


def test(anytest):
    
    mg = anytest.macro_gen
    path_kw = { 'AMMR_PATH':anytest.ammr,
                'ANYMOCAP':anytest.anymocap,
                'TEMP_PATH': "."}
    mainfile = os.path.join(anytest.model_path, 'Main.any')
    mg.add_load(mainfile, path_kw = path_kw)
    macro = mg.generate_macros()
    
    outputlist = anytest.app.start_macro( macro )
    
    anytest.check_output_log(outputlist)  

    
    
    
    