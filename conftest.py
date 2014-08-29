import pytest
from shutil import copytree, ignore_patterns
import os
from anypytools.abcutils import AnyPyProcess,get_anybodycon_path
from anypytools.generate_macros import MacroGenerator
import subprocess 

# These global variables are set by the pytest_report_header funciton 
_anybodycon_path = get_anybodycon_path()
_ammr_path = os.path.join(os.path.dirname(get_anybodycon_path()),'AMMR')

def get_ammr_version(ammr_path):
    import xml.etree.ElementTree as ET
    version_file = os.path.join(ammr_path,'AMMR.version.xml')
    try:
        tree = ET.parse(version_file)
        version = tree.getroot()
        vstring = "{}.{}.{}".format(version.find('v1').text,
                                    version.find('v2').text,
                                    version.find('v3').text )
    except:
        vstring = "Unknown AMMR version"
    return vstring

        
@pytest.yield_fixture(scope='module')
def setup_test_folder(request):
    test_folder = request.fspath.new(basename='')
    if request.config.getoption('--inplace'):
        with test_folder.as_cwd():
            yield
    else:
        dst = request.config._tmpdirhandler.mktemp(test_folder.basename,
                                                   numbered=False)
        dst.remove()
        copytree(str(test_folder), str(dst), ignore=ignore_patterns('test_*.py', '__pycache__'))
        with dst.as_cwd():
            yield


def pytest_addoption(parser):
    parser.addoption("--ammr", action="store", default="built-in",
        help="AMMR used in test: built-in or path-to-ammr")
    parser.addoption("--anybodycon", action="store", default="default",
        help="anybodycon.exe used in test: default or path-to-anybodycon")
    parser.addoption("--inplace", action="store_true",
        help="Run test in place, i.e. do not copy folder")


@pytest.yield_fixture()
def anymocap( scope="session"):  
    folder_path = os.path.dirname(__file__)
    anymocap_path = os.path.join(folder_path, 'Model', 'AnyMocapModel.any')
    yield anymocap_path
        

  
def pytest_report_header(config):
    global _anybodycon_path
    global _ammr_path
    _anybodycon_path = config.getoption("--anybodycon")
    if _anybodycon_path == 'default':
        _anybodycon_path = get_anybodycon_path()

    _ammr_path = config.getoption("--ammr")
    if _ammr_path == 'built-in':
        _ammr_path = os.path.join(os.path.dirname(get_anybodycon_path()),'AMMR')

    if not os.path.exists(_ammr_path):
        raise IOError('Cound not find: {}'.format(_ammr_path))
    if not os.path.isfile(_anybodycon_path):
        raise IOError('Cound not find: {}'.format(_anybodycon_path))
    
    console_output = subprocess.check_output([_anybodycon_path, '/ni'])
    ams_version = console_output.splitlines()[2].decode()[23:]
    ams_build = console_output.splitlines()[4].decode()
    ammr_version = get_ammr_version(_ammr_path)
    header = "\n  AMMR {0}: {1}\n  AnyBody{2} {3}\n  {4}\n".format(ammr_version,
                                                             _ammr_path,
                                                             ams_version,
                                                             ams_build,
                                                             _anybodycon_path)
    return header

class AnyTestFixture():
    def __init__(self, app, ammr):
        self.app = app
        self.ammr = ammr
        
@pytest.yield_fixture()
def AnyFixture(anymocap, setup_test_folder):  
    global _anybodycon_path, _ammr_path
    app = AnyPyProcess(anybodycon_path = _anybodycon_path,
                       keep_logfiles=True, disp=False)
    
    atf = AnyTestFixture(app, _ammr_path)
    atf.anymocap = anymocap
    atf.MacroGenerator = MacroGenerator
    yield atf
