# Script for installing timeloop-python interface.
# Tested on Python 3.8.17
import os
pytimeloop_dir = "src/timeloop-python"
timeloop_dir = "src/timeloop"
timeloop_include_dir = "src/timeloop/include"
timeloop_lib_dir = "src/timeloop/lib"
working_path = os.getcwd()
dst_path = os.path.join(working_path, pytimeloop_dir)
timeloop_path = os.path.join(working_path, timeloop_dir)
include_path = os.path.join(working_path, timeloop_include_dir)
lib_path = os.path.join(working_path, timeloop_lib_dir)
try:
    os.system("git clone https://github.com/Accelergy-Project/timeloop-python.git {}".format(dst_path))
    os.chdir(f'{dst_path}')
    os.system("git pull origin main")
    os.system('git submodule update --init')
    os.environ['LIBTIMELOOP_PATH'] = timeloop_path
    os.environ['TIMELOOP_INCLUDE_PATH'] = include_path
    os.environ['TIMELOOP_LIB_PATH'] = lib_path
    os.system('git submodule update --init')
    os.system('rm -rf build')
    os.system('pip3 install -e .')
except:
    "Something wrong when installing Timeloop for Python, please check timeloop-python repository for detailed installation. Also note that the build works on older versions of Python (i.e. 3.8)."