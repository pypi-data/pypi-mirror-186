import shutil
import os
import sysconfig

#check if we are on windows
if "win" in sysconfig.get_platform():
    #check if fftw3f.dll is in the current directory
    if not os.path.isfile("fftw3f.dll"):
        #if not, copy it from the libs folder
        shutil.copyfile("libs/fftw3.h","fftw3.h")
        shutil.copyfile("libs/fftw3f.dll","fftw3f.dll")
        shutil.copyfile("libs/fftw3f.lib","fftw3f.lib")

from .fcwt import Morlet, Scales, FCWT, FCWT_LINSCALES, FCWT_LOGSCALES, FCWT_LINFREQS
from .boilerplate import cwt, plot

