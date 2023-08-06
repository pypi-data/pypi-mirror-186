import os
import json

from nipy import load_image
from nipy.core.api import xyz_affine
from nipy.labs.viz import plot_map, coord_transform
import numpy as np
import matplotlib
from pylab import savefig, subplot, subplots_adjust, figure, rc, text

from datetime import datetime

# colormap processing
cdict = {
    "red": (
        (0.0, 0.0, 0.0),
        (0.25, 0.2, 0.2),
        (0.45, 0.0, 0.0),
        (0.5, 0.5, 0.5),
        (0.55, 0.0, 0.0),
        (0.75, 0.8, 0.8),
        (1.0, 1.0, 1.0),
    ),
    "green": (
        (0.0, 0.0, 1.0),
        (0.25, 0.0, 0.0),
        (0.45, 0.0, 0.0),
        (0.5, 0.5, 0.5),
        (0.55, 0.0, 0.0),
        (0.75, 0.0, 0.0),
        (1.0, 1.0, 1.0),
    ),
    "blue": (
        (0.0, 0.0, 1.0),
        (0.25, 0.8, 0.8),
        (0.45, 0.0, 0.0),
        (0.5, 0.5, 0.5),
        (0.55, 0.0, 0.0),
        (0.75, 0.0, 0.0),
        (1.0, 0.0, 0.0),
    ),
}
ndict = {
    "red": ((0.0, 0.0, 0.0), (0.5, 0.2, 0.2), (0.9, 0.0, 0.0), (1.0, 0.5, 0.5)),
    "green": ((0.0, 0.0, 1.0), (0.5, 0.0, 0.0), (0.9, 0.0, 0.0), (1.0, 0.5, 0.5)),
    "blue": ((0.0, 0.0, 1.0), (0.5, 0.8, 0.8), (0.9, 0.0, 0.0), (1.0, 0.5, 0.5)),
}
pdict = {
    "red": ((0.0, 0.5, 0.5), (0.1, 0.0, 0.0), (0.5, 0.8, 0.8), (1.0, 1.0, 1.0)),
    "green": ((0.0, 0.5, 0.5), (0.1, 0.0, 0.0), (0.5, 0.0, 0.0), (1.0, 1.0, 1.0)),
    "blue": ((0.0, 0.5, 0.5), (0.1, 0.0, 0.0), (0.5, 0.0, 0.0), (1.0, 0.0, 0.0)),
}

both_cmap = matplotlib.colors.LinearSegmentedColormap("brian_combined", cdict, 256)
pos_cmap = matplotlib.colors.LinearSegmentedColormap("brain_above", pdict, 256)
neg_cmap = matplotlib.colors.LinearSegmentedColormap("brain_below", ndict, 256)

cmaps = {
    "both": both_cmap,
    "neg": neg_cmap,
    "pos": pos_cmap,
}

# dict of signs for filtering negative/positive components ("both" is here for compatibility)
# it is intentionally inverted
DSGN = {
    "both": 0.0,
    "neg": 1.0,
    "pos": -1.0,
}

UTCNOW = datetime.utcnow().strftime("%y%m%d.%H%M%S")


def process_image(
    NIFTI, ANAT, DIR, SGN, thr: float = 2.0, dpi: int = 300, iscale: int = 3
):

    nifti = load_image(NIFTI)
    anat = load_image(ANAT)

    imax = nifti.get_data().max()
    imin = nifti.get_data().min()

    imshow_args = {"vmax": imax, "vmin": imin}

    mcmap = cmaps[SGN]

    num_features = nifti.shape[-1]
    # number of rows
    y = max([1, int(round(np.sqrt(num_features / 3)))])
    # number of columns
    x = int(np.ceil(num_features / y) + 1)

    font = {"size": 8}
    rc("font", **font)

    figure(figsize=[iscale * y, iscale * x / 3])
    subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.1, hspace=0)

    for i in range(0, num_features):
        # load the ICA component and filter it according to SGN
        data = nifti.get_data()[:, :, :, i]
        data[np.sign(data) == DSGN[SGN]] = 0

        # plot component
        if max(abs(data.flatten())) > thr + 0.2:
            ax = subplot(x, y, i + 1)
            max_idx = np.unravel_index(np.argmax(data), data.shape)
            plot_map(
                data,
                xyz_affine(nifti),
                anat=anat.get_data(),
                anat_affine=xyz_affine(anat),
                black_bg=True,
                threshold=thr,
                cut_coords=coord_transform(
                    max_idx[0], max_idx[1], max_idx[2], xyz_affine(nifti)
                ),
                annotate=False,
                axes=ax,
                cmap=mcmap,
                draw_cross=False,
                **imshow_args,
            )
            text(
                0.0,
                0.95,
                str(i),
                transform=ax.transAxes,
                horizontalalignment="center",
                color=(1, 1, 1),
            )

    # create output directory and save results
    if DIR is None:
        DIR = UTCNOW
    os.makedirs(f"./brain-paint-results/{DIR}")

    savefig(
        f"./brain-paint-results/{DIR}/output.png",
        facecolor=(0, 0, 0),
        dpi=dpi,
    )
    savefig(
        f"./brain-paint-results/{DIR}/output.svg",
        facecolor=(0, 0, 0),
    )

    setup = {
        "nifti": NIFTI,
        "anat": ANAT,
        "sgn": SGN,
        "thr": thr,
        "dpi": dpi,
    }
    with open(f"./brain-paint-results/{DIR}/setup.json", "w", encoding="utf8") as f:
        json.dump(setup, f)

    print(f"Results can be found at ./brain-paint-results/{DIR}")


def parser():
    import warnings
    import argparse

    warnings.filterwarnings("ignore")

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--nifti",
        type=str,
        required=True,
        help="Path to the 4D nifti to convert to images",
    )
    parser.add_argument(
        "--anat",
        type=str,
        required=True,
        help="Path to the anatomical image to use as underlay",
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=None,
        help="Name for the results directory (can be nested) (default: UTC time)",
    )
    parser.add_argument(
        "--sign",
        type=str,
        choices=["pos", "neg", "both"],
        default="both",
        help="Show only positive components ('pos'), \
            only negative components ('neg'), \
                or both ('both')",
    )
    parser.add_argument(
        "--thr",
        type=float,
        default=2.0,
        help="Threshold value for component significance",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="PNG output dpi",
    )

    args = parser.parse_args()

    process_image(
        NIFTI=args.nifti,
        ANAT=args.anat,
        DIR=args.dir,
        SGN=args.sign,
        thr=args.thr,
        dpi=args.dpi,
    )
