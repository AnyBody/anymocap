import os
import pytest
pytest_plugins = "anypytools"
        

@pytest.fixture()
def anytest(anytest): 
    """This fixture 'overloads' the anytest fixture
    and injects the some extra path and define 
    statements which are specific to the AnyMocapModel.
    """
    anymocap_path = os.path.join(os.path.dirname(__file__) )
                                
    anytest.path_kw.update( {'ANYMOCAP':anymocap_path} )
    anytest.define_kw.update( {'JOINT_AND_DRIVERS_OPTIMIZED':0} )
    return anytest