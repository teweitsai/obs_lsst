# This file is part of obs_lsst.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.

import os.path

from lsst.utils import getPackageDir
# The following will have to be uncommented and adapted when the
# X-talk correction will be active
#from lsst.obs.lsst.isr import SubaruIsrTask
#config.isr.retarget(SubaruIsrTask)
#config.isr.load(os.path.join(getPackageDir("obs_lsst"), "config", "isr.py"))

config.load(os.path.join(getPackageDir("obs_lsst"), "config", "lsstCam.py"))

configDir = os.path.join(getPackageDir("obs_lsst"), "config")
bgFile = os.path.join(configDir, "background.py")
fpBgFile = os.path.join(configDir, "focalPlaneBackground.py")

config.largeScaleBackground.load(fpBgFile)
config.detection.background.load(bgFile)
config.subtractBackground.load(bgFile)

config.isr.doBrighterFatter = False
