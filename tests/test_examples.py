from __future__ import division, absolute_import, print_function, unicode_literals
import os
import shutil
import pytest

from anypytools.abcutils import AnyPyProcess
from anypytools.generate_macros import MacroGenerator

modelfolder = os.path.join(os.path.dirname(__file__),'..','Model')
examplefolder = os.path.join(os.path.dirname(__file__),'..','Examples')



@pytest.yield_fixture()
def temp_dir(tmpdir, scope="module"):
    """ Copies the AnyMocap model to temp directory to run tests"""
    shutil.copytree(modelfolder, str( tmpdir.join('Model') ) )
    shutil.copytree(examplefolder, str( tmpdir.join('Examples') ) )
    with tmpdir.as_cwd():
        yield tmpdir



def test_example_plugingait(temp_dir):
    app =  AnyPyProcess() 
    mg = MacroGenerator()
    defines = {'JOINT_AND_DRIVERS_OPTIMIZED':0}
    mg.add_load('Examples/Plug-in-gait/Main.any',define_kw = defines)
#    mg.add_run_operation('Main.Studies.ParameterIdentification.ParameterOptimization')
#    mg.add_save_design('Main.Studies.ParameterIdentification',
#                       str(temp_dir.join('paramter.txt'))  )
    result = app.start_macro( mg.generate_macros() )
    assert 'ERROR' not in result[0], result[0]['ERROR']
    
#    defines = {'JOINT_AND_DRIVERS_OPTIMIZED',1}
#    mg.add_load('Examples/Plug-in-gait/Main.any',define_kw = defines)
#    mg.add_run_operation('Main.RunApplication.LoadParameters')
#    mg.add_run_operation('Main.RunApplication.RunInverseDynamics')
#    result = app.start_macro( mg.generate_macros() )
#    assert 'ERROR' not in result[0]
    
    
def test_example_InitialPosExample(temp_dir):
    app =  AnyPyProcess() 
    macro = [['load "Examples/InitialPosExample/Main.any"']]
    result = app.start_macro(macro)
    assert 'ERROR' not in result[0], result[0]['ERROR']


def test_example_MarkerWeightExample(temp_dir):
    app =  AnyPyProcess() 
    macro = [['load "Examples/MarkerWeightExample/Main.any"']]
    result = app.start_macro(macro)
    assert 'ERROR' not in result[0], result[0]['ERROR']

def test_example_LTHT(temp_dir):
    app =  AnyPyProcess() 
    macro = [['load "Examples/LTHT/Subject_1/Static/main.any"'],
             ['load "Examples/LTHT/Subject_1/Walk/main.any"']]
    results = app.start_macro(macro)
    for result in results:
        assert 'ERROR' not in result, result['ERROR']

