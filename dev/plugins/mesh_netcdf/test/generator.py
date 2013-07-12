#!/usr/bin/env python

import os


os.system("TST=$PWD/../../tests")
os.system("DATA=$PWD/../../tests/data")

os.system("RTPONEDOMAIN=$DATA/rtopo_shape_DN__2.shp")
os.system("RTPMULTDOMAIN=$DATA/ID0Layer.shp")

os.system("IDFILE=$DATA/a_idLayer.shp")

os.system("NCFILE=$DATA/none")
os.system("REF=$DATA/mesh_terminal_timestamp")
os.system("FILE=$PWD/mesh_terminal")


#if [ "$FILE" -nt "$REF" ]; then



os.system("echo ....................................")

os.system("Generating data: Gaussian bump")
os.system("....................................")
os.system("python $TST/gaussian_bump.py $TST/gaussian_bump.nc")
os.system("grdmath $TST/gaussian_bump.nc 2 MUL = $TST/gaussian_bump_medium.nc")
os.system("grdmath $TST/gaussian_bump.nc 4 MUL = $TST/gaussian_bump_coarse.nc")

os.system("echo ....................................")

os.system("Testing: annulus, Bsplines = True Compounds = False")

os.system(".....................................")

os.system("python mesh_terminal --line BN -g $TST/test_annulus_BN.geo $DATA/annulus.shp --mesh --mval 10")

os.system("echo ....................................")

os.system("Testing: annulus, Bsplines = True Compounds = True")

os.system(".....................................")

os.system("python mesh_terminal --line BY -g $TST/test_annulus_BY.geo $DATA/annulus.shp --mesh --mval 10")
os.system("python mesh_terminal --line BY -g $TST/test_annulus_BY_metric.geo $DATA/annulus.shp --mesh -m $TST/gaussian_bump.nc")
os.system("python mesh_terminal --line BY -g $TST/test_annulus_BY_medium_metric.geo $DATA/annulus.shp --mesh -m $TST/gaussian_bump_medium.nc")
os.system("python mesh_terminal --line BY -g $TST/test_annulus_BY_coarse_metric.geo $DATA/annulus.shp --mesh -m $TST/gaussian_bump_coarse.nc")

os.system("echo ....................................")

os.system("Testing: annulus, Bsplines = False Compounds = True")

os.system(".....................................")

os.system("python mesh_terminal --line LY -g $TST/test_annulus_LY.geo $DATA/annulus.shp --mesh --mval 10")
os.system("python mesh_terminal --line LY -g $TST/test_annulus_LY_metric.geo $DATA/annulus.shp --mesh -m $TST/gaussian_bump.nc")
os.system("python mesh_terminal --line LY -g $TST/test_annulus_LY_medium_metric.geo $DATA/annulus.shp --mesh -m $TST/gaussian_bump_medium.nc")
os.system("python mesh_terminal --line LY -g $TST/test_annulus_LY_coarse_metric.geo $DATA/annulus.shp --mesh -m $TST/gaussian_bump_coarse.nc")



os.system("echo .....................................")

os.system("Testing: BSplines = True Compounds = False")

os.system(".....................................")
os.system("python mesh_terminal --line BN -g $TST/testfileBN_0.geo $RTPONEDOMAIN --mesh")
os.system("python mesh_terminal --line BN -g $TST/testfileBN_1.geo --id $IDFILE $RTPONEDOMAIN --mesh")
os.system("python mesh_terminal --line BN -g $TST/testfileBN_2.geo $RTPMULTDOMAIN --mesh")
os.system("python mesh_terminal --line BN -g $TST/testfileBN_3.geo --id $IDFILE $RTPMULTDOMAIN  --mesh")

os.system("echo .....................................")

os.system("Testing: BSplines = False Compounds = True")

os.system(".......................................")
os.system("python mesh_terminal -l LY -g $TST/testfileLY_0.geo $RTPONEDOMAIN --mesh")
os.system("python mesh_terminal -l LY -g $TST/testfileLY_1.geo --id $IDFILE $RTPONEDOMAIN --mesh")
os.system("python mesh_terminal -l LY -g $TST/testfileLY_2.geo $RTPMULTDOMAIN --mesh")
os.system("python mesh_terminal -l LY -g $TST/testfileLY_3.geo --id $IDFILE $RTPMULTDOMAIN  --mesh")

os.system("echo .....................................")
os.system("Testing: BSplines = True Compounds = True")

os.system("......................................")
os.system("python mesh_terminal -l BY -g $TST/testfileBY_0.geo $RTPONEDOMAIN --mesh")
os.system("python mesh_terminal -l BY -g $TST/testfileBY_1.geo --id $IDFILE $RTPONEDOMAIN --mesh")
os.system("python mesh_terminal -l BY -g $TST/testfileBY_2.geo $RTPMULTDOMAIN --mesh")
os.system("python mesh_terminal -l BY -g $TST/testfileBY_3.geo --id $IDFILE $RTPMULTDOMAIN  --mesh")


os.system("py.test test/test_geo.py")

os.system("echo Done Testing ")


#else
#  echo "mesh_terminal has not been updated since last test"
#fi


