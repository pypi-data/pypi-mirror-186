import pytest
import subprocess
from cegalprizm.hub import Hub, ConnectorFilter
from pathlib import Path
import psutil
import os
import logging

logging.basicConfig()
logger=logging.getLogger()

petrel_version_override = 2021
try:
    petrel_version = os.environ["PRIZM_PETREL_VERSION"]
except: 
    petrel_version = petrel_version_override

hub_local_path = r".\pytests\cegalhub\hub_local.ps1"
teardown_script_path = r".\pytests\cegalhub\hub_petrel_teardown.ps1"
if os.environ.get("USERNAME").lower() == "vmadministrator":  # if running on azure devops:
    directory = os.environ.get("BUILD_ARTIFACTSTAGINGDIRECTORY")
    pythontoolgridsproject = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolGridsProject", "PythonToolGridsProject" + ".pet") 
    pythontooltestproject = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolTestProject", "PythonToolTestProject" + ".pet")
    pythontooltestproject2 = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolTestProject2", "PythonToolTestProject2" + ".pet")
    hub_local_path = r".\pytests\cegalhub\hub_local_" + str(petrel_version) + r"_azdo.ps1"
else:
    if petrel_version_override is not None:
        petrel_version = petrel_version_override
    home_path = os.environ.get("BBR_UNIT_TEST_FRAMEWORK_FOLDER")
    if home_path is None:
        home_path = str(Path.home())
        pythontoolgridsproject = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolGridsProject\PythonToolGridsProject.pet"
        pythontooltestproject = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolTestProject\PythonToolTestProject.pet"
        pythontooltestproject2 = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolTestProject2\PythonToolTestProject2.pet"

def process_exists(process_name: str) -> bool:
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def initialize_hub_local():
    process = subprocess.Popen(["powershell.exe", hub_local_path], stdout=subprocess.PIPE)
    print('')
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
        if ("Agent configured to allow scripts." in output.decode()):
            logger.info("Hub in Local mode initialized! Ready for test.")
            break
    return process

def initialize_teardown_script():
    process = subprocess.Popen(["powershell.exe", teardown_script_path], stdout=subprocess.PIPE)

def pytest_configure(config):
    if not process_exists('cegalhub'):
        initialize_hub_local()

def pytest_unconfigure(config):
    hub = Hub()
    connectionfilter = ConnectorFilter(labels_dict = {'gui': 'false'})
    headless_petrel = len(hub.query_connectors(connector_filter=connectionfilter)) > 0
    if headless_petrel:
        initialize_teardown_script()

def get_petrel_version(petrellink, hub):
    petrel_version = hub.query_connectors(connector_filter=petrellink._ptp_hub_ctx.connector_filter)[0].labels.get('petrel-major-version')
    return petrel_version

def get_current_petrel_project(petrel_context, hub):
    path_to_current_loaded_project = hub.query_connectors(connector_filter=petrel_context.connector_filter)[0].labels.get('primary-project-path')
    return path_to_current_loaded_project

def petrel_is_running(hub):
    is_running = True
    petrel_connector = hub.query_connectors('cegal.hub.petrel')
    if len(petrel_connector) == 0:
        is_running = False
    return is_running

@pytest.fixture(scope="package")
def petrellink(petrel_context):
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    petrellink = PetrelConnection(allow_experimental=True, petrel_ctx=petrel_context)
    yield petrellink

@pytest.fixture(scope="package")
def hub():
    hub = Hub()
    yield hub

@pytest.fixture(scope="package")
def petrel_context(request, hub):
    if petrel_is_running(hub):
        petrel_ctx = hub.default_petrel_ctx()
    else:
        agent_ctx = hub.default_agent_ctx()
        petrel_ctx = agent_ctx.new_petrel_instance(petrel_version=request.param[0], connect_timeout_secs=720)

    path_to_current_loaded_project = get_current_petrel_project(petrel_ctx, hub)
    if path_to_current_loaded_project.lower() != request.param[1].lower():
        print('Loading project: ' + request.param[1])
        petrel_ctx.load_project(path=request.param[1])
    yield petrel_ctx

@pytest.fixture(scope="package")
def unsupported_version_2019(petrellink, hub):
    unsupported_version_2019 = False
    petrel_version = get_petrel_version(petrellink, hub)
    if int(petrel_version) < 20:
        unsupported_version_2019 = True
    yield unsupported_version_2019


@pytest.fixture(scope="package")
def grid(petrellink):
    grid = petrellink.grids['Models/Segmented model/Segmented grid']
    yield grid

@pytest.fixture(scope="package")
def welltops(petrellink):
    welltops = petrellink.markercollections['Input/WellTops']
    yield welltops

@pytest.fixture(scope="package")
def wellb1(petrellink):
    wellb1 = petrellink.wells['Input/Wells/B Wells/B1']
    yield wellb1

@pytest.fixture(scope="package")
def completions_set(petrellink):
    well = petrellink.wells['Input/Wells/Well_Good']
    completions_set = well.completions_set
    yield completions_set

@pytest.fixture(scope="package")
def completions_set_none(petrellink):
    well = petrellink.wells['Input/Wells/Well_Good lateral']
    completions_set = well.completions_set
    yield completions_set

@pytest.fixture(scope="package")
def pointset_empty(petrellink):
    pointset_empty = petrellink.pointsets['Input/Geometry/Points empty']
    yield pointset_empty

@pytest.fixture(scope="package")
def pointset_custom_property_units(petrellink):
    pointset_empty = petrellink.pointsets['Input/Geometry/Copy of Points 1 many points']
    yield pointset_empty

@pytest.fixture()
def cloned_pointset_custom_property_units(petrellink):
    pointset = petrellink.pointsets['Input/Geometry/Copy of Points 1 many points']
    clone = pointset.clone('Points 1_copy 2', copy_values = True)
    yield clone
    delete_workflow = petrellink.workflows['Workflows/New folder/delete_object']
    object = delete_workflow.input['object']
    delete_workflow.run({object: clone})
