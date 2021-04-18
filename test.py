# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:23:16 2021

@author: Stefano
"""

import numpy as np
import xarray as xr
import netCDF4 as nc
import pandas as pd


fn="ta.nc"
ds=nc.Dataset(fn)
ta=ds.variables['ta']
lon=ds.variables['lon']  
lat=ds.variables['lat'] 
time=ds.variables['time']

start=0
end=16

m=np.zeros((1500, 3600,1))
for lo in range(0,len(lon)-1):
      for la in range(0,len(lat)-1):
         if np.isnan(ta[0,la,lo])==False:
            maxval=ta[start:end,la,lo].max()
            m[la,lo,0]=maxval
         else:
            m[la,lo,0]=np.nan
        
newds = xr.Dataset(

    {

        "temperature": (["yc", "xc","time"], m),
    },

    coords={
        "lon": (["xc"], lon),
        "lat": (["yc"], lat),
        "reference_time": pd.Timestamp("1999-01-01"),
    },

)

air = newds.temperature
air2d = air.isel()
air2d.plot(yincrease=False)