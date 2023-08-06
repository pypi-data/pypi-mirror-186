# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import matplotlib.pyplot as pypl
import numpy as nmpy
import mrc as mrci

import cell_tracking_BC.task.registration as rgst


sequence = nmpy.array(mrci.imread("/home/eric/Code/project/abc/cell-death/asma/thesis/_data/sequence/TREAT01_04_R3D.dv"))
print(sequence.shape)

cfp = sequence[:,0,...]
yfp = sequence[:,1,...]
pol = sequence[:,2,...]

n_identical = 0
n_zeros_yfp = 0
n_zeros_pol = 0
for frame_idx in range(cfp.shape[0]):
    translation_yfp = rgst.TranslationFromTo(cfp[frame_idx,...], yfp[frame_idx,...])
    # yfp_registered = rgst.WithTranslationApplied(yfp[frame_idx,...], translation_yfp)

    translation_pol = rgst.TranslationFromTo(cfp[frame_idx,...], pol[frame_idx,...])
    # pol_registered = rgst.WithTranslationApplied(pol[frame_idx,...], translation_pol)

    if nmpy.array_equal(translation_pol, translation_yfp):
        n_identical += 1
    if all(translation_yfp == 0.0):
        n_zeros_yfp += 1
    if all(translation_pol == 0.0):
        n_zeros_pol += 1

print(f"Identical={n_identical}; Different={cfp.shape[0] - n_identical}")
print(f"Zeros: YPF={n_zeros_yfp}; POL={n_zeros_pol}")


# vmin_yfp = nmpy.amin(yfp[frame_idx,...])
# vmax_yfp = nmpy.amax(yfp[frame_idx,...])
#
# vmin_pol = nmpy.amin(pol[frame_idx,...])
# vmax_pol = nmpy.amax(pol[frame_idx,...])
#
# pypl.matshow(cfp[frame_idx,...])
# pypl.gca().set_title("CFP")
#
# pypl.matshow(yfp[frame_idx,...])
# pypl.gca().set_title("YFP Original")
# pypl.matshow(yfp_registered, vmin=vmin_yfp, vmax=vmax_yfp)
# pypl.gca().set_title(f"YFP Registered: {tuple(translation_yfp)}")
#
# pypl.matshow(pol[frame_idx,...])
# pypl.gca().set_title("POL Original")
# pypl.matshow(pol_registered, vmin=vmin_pol, vmax=vmax_pol)
# pypl.gca().set_title(f"POL Registered: {tuple(translation_pol)}")
#
# pypl.show()
