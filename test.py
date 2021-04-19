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


from_day=1
to_day=17

k=[]

m=np.zeros((1500, 3600,1))

for lo in range(0,len(lon)-1):
      for la in range(0,len(lat)-1):
         if np.isnan(ta[0,la,lo])==False:
            maxval=ta[from_day-1:to_day-1,la,lo].max()
            m[la,lo,0]=maxval
            k.append((maxval,lon[lo].item(),lat[la].item()))
         else:
            m[la,lo,0]=np.nan
            k.append((np.nan,lon[lo].item(),lat[la].item()))
         
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