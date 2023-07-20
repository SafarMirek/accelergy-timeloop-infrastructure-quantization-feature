# Script for applying an older commit patch to pytimeloop in order to successfully build it.
# The original script is taken from the GAMMA for Timeloop repository (https://github.com/maestro-project/gamma-timeloop/blob/master/build_pytimeloop.py).
# Original author: Felix Kao
# Tested on Python 3.8.17
import os
commit_id = 'b5885615eeddfc249758d003a99c6854884a94b9'
pytimeloop_dir = "src/timeloop-python"
timeloop_dir = "src/timeloop"
timeloop_include_dir = "src/timeloop/include"
timeloop_lib_dir = "src/timeloop/lib"
working_path = os.getcwd()
dst_path = os.path.join(working_path, pytimeloop_dir)
timeloop_path = os.path.join(working_path, timeloop_dir)
try:
    os.system("git clone https://github.com/Accelergy-Project/timeloop-python.git {}".format(dst_path))
    os.chdir(f'{dst_path}')
    os.system(f"git checkout {commit_id}")
    os.system(f'git am {working_path}/patches/update_interface.patch')
    os.system('git submodule update --init')
    os.environ['LIBTIMELOOP_PATH'] = timeloop_path
    os.system('git submodule update --init')
    os.system('rm -rf build')
    os.system('pip3 install -e .')
except:
    "Something wrong when installing Timeloop for Python, please check timeloop-python repository for detailed installation. Also note that the build works on older versions of Python (i.e. 3.8)."