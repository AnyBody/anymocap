import pytest

@pytest.mark.xfail(reason='Features not implemented in AnyBody yet')
def test(anytest):
    loadcmd = anytest.load_macro('Main.any')
    envelope  = ('Main.Studies.InverseDynamicsStudy.Output'
                 '.BodyModel.SelectedOutput.Right.Leg.Muscles.Envelope')
    macro = [[ loadcmd, 
              'operaiton Main.RunApplication',
              'classoperation {} "Dump"'.format(envelope),
              'exit']]
              
    output = anytest.app.start_macro(macro)
    
    anytest.check_output_log(output)  
    
    assert envelope in output[0]
