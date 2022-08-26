import logging
import os
import pyglider.seaexplorer as seaexplorer
import pyglider.ncprocess as ncprocess
import pyglider.utils as pgutils

logging.basicConfig(level='INFO')

rawdir  = '/home/callum/Downloads/glider dataa/zwei/'
rawncdir     = '/home/callum/Downloads/glider_data/SEA61_M48_sub_10/M48_sub_10/rawnc/'
deploymentyaml = '/home/callum/Documents/data-flow/raw-to-nc/deployment-yaml/mission_yaml/SEA61_M48.yml'
l0tsdir    = './L0-timeseries/'
profiledir = './L0-profiles/'
griddir    = './L0-gridfiles/'

# clean last processing...

if True:
    # turn *.EBD and *.DBD into *.ebd.nc and *.dbd.nc netcdf files.
    #os.system('rm ' + rawncdir + '* ' + l0tsdir + '* ' + profiledir + '* ' +
     #         griddir + '* ')
    #seaexplorer.raw_to_rawnc(rawdir, rawncdir, deploymentyaml)
        # merge individual neetcdf files into single netcdf files *.ebd.nc and *.dbd.nc
    #seaexplorer.merge_rawnc(rawncdir, rawncdir, deploymentyaml, kind='raw')

        # Make level-1 timeseries netcdf file from th raw files...
    outname = seaexplorer.raw_to_timeseries(rawncdir, l0tsdir, deploymentyaml, kind='raw', profile_min_time=30)
    #ncprocess.extract_timeseries_profiles(outname, profiledir, deploymentyaml)
    #outname2 = ncprocess.make_gridfiles(outname, griddir, deploymentyaml)