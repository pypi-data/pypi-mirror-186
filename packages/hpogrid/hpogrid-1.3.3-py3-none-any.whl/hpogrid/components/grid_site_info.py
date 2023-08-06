import os
import sys
import json
import fnmatch
from typing import List, Optional

from hpogrid.core.defaults import kDefultGridSiteType, kDefaultGridSiteInfo
from hpogrid.utils.stylus import create_table

class GridSiteInfo():
    
    @staticmethod
    def show(name:str=None, gpu:bool=True, active:bool=True, site_type:Optional[List]=kDefultGridSiteType,
             info:List=kDefaultGridSiteInfo):

        grid_site_info = GridSiteInfo.extract(name, gpu, active, site_type, info)
        print(create_table(grid_site_info, transpose=True))

    @staticmethod
    def list_sites(name:str=None, gpu:bool=True, active:bool=True, site_type:Optional[List]=kDefultGridSiteType):
        grid_site_info = GridSiteInfo.extract(name, gpu, active, site_type)
        return list(grid_site_info.keys())

    @staticmethod
    def extract(name:str=None, gpu:bool=True, active:bool=True, site_type:Optional[List]=kDefultGridSiteType,
        info:List=kDefaultGridSiteInfo):
        '''
        retrieve some basic information of PanDA grid sites
        '''
        try:
            jsonfileLocation = os.environ['ALRB_cvmfs_repo'] + '/sw/local/etc/agis_schedconf.json'
        except:
            jsonfileLocation = '/cvmfs/atlas.cern.ch/repo/sw/local/etc/agis_schedconf.json'
        
        if not os.path.exists(jsonfileLocation):
            raise ValueError('cannot locate file containing grid site information: agis_schedconf.json')
            
        with open(jsonfileLocation,'r') as jsonfile:
            jsondata = json.load(jsonfile)

        if name is None:
            name = '*'

        grid_site_info = {}

        for site in jsondata:
            # filter site names (could also match jsondata[site]['panda_resource'] instead)
            if not fnmatch.fnmatch(site, name):
                continue
            # filter non-active grid sites
            if active and (not jsondata[site]['state'] == 'ACTIVE'):
                continue
            # no good indicator of a GPU site yet will just judge on site name
            if gpu and (not 'GPU' in jsondata[site]['panda_resource']):
                continue
            if site_type and (jsondata[site]['type'] not in site_type):
                continue
            grid_site_info[site] = {key: jsondata[site][key] for key in info}
        from pdb import set_trace
        set_trace()
        return grid_site_info