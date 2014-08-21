from __future__ import division, absolute_import, print_function, unicode_literals
import os
import shutil
import pytest

from anypytools.abcutils import AnyPyProcess
from anypytools.generate_macros import MacroGenerator

modelfolder = os.path.join(os.path.dirname(__file__),'..','Model')
examplefolder = os.path.join(os.path.dirname(__file__),'..','Examples')

@pytest.yield_fixture()
def init_anymocap(tmpdir, scope="module"):
    """ Copies the AnyMocap model to temp directory to run tests"""
    shutil.copytree(modelfolder, str( tmpdir.join('Model') ) )
    shutil.copytree(examplefolder, str( tmpdir.join('Examples') ) )
    with tmpdir.as_cwd():
        yield tmpdir


def test_example_DynamicOnly(init_anymocap):
    app =  AnyPyProcess() 
    mg = MacroGenerator()
    defines = {'JOINT_AND_DRIVERS_OPTIMIZED',0}
    mg.add_load('Examples/DynamicOnly/Main.any',define_kw = defines)
    mg.add_run_operation('Main.RunApplication.RunParameterIdentificaiton')
    mg.add_run_operation('Main.RunApplication.SaveParameters')
    result = app.start_macro(macro)
    defines = {'JOINT_AND_DRIVERS_OPTIMIZED',1}
    mg.add_load('Examples/DynamicOnly/Main.any',define_kw = defines)
    mg.add_run_operation('Main.RunApplication.LoadParameters')
    mg.add_run_operation('Main.RunApplication.RunInverseDynamics')
    #result = app.start_macro(macro)
    
    assert 'ERROR' not in result[0]
    
def test_example_InitialPosExample(init_anymocap):
    app =  AnyPyProcess() 
    macro = [['load "Examples/InitialPosExample/Main.any"']]
    result = app.start_macro(macro)
    assert 'ERROR' not in result[0]