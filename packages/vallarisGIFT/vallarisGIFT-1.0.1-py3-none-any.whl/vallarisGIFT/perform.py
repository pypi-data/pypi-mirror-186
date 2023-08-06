import geopandas as gpd
import json
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import earthpy.plot as ep

def buffer(data, distance, *arge, **kwargs): #ในวงเล็บคือ รับข้อมูลมา 2 ตัว
    crs = kwargs.get('crs',"EPSG:4326")
    
    try:    
        dump_json = json.dumps(data)
        read_data = gpd.read_file(dump_json)

        out1 = read_data.to_crs("EPSG:3857") 
        out1['geometry'] = out1.buffer(distance)
        out2 = out1.to_crs("EPSG:4326")
        return out2
    except Exception as e:
        return 'error:'+str(e)


def union(input_data, overlay_data, *args, **kwargs):
    
    try :
    #     input_data
        in_json = json.dumps(input_data)
        read_in = gpd.read_file(in_json)

    #     overlay_data
        over_json = json.dumps(overlay_data)
        read_over = gpd.read_file(over_json)

        newdf = gpd.overlay(read_in, read_over, how="union")

        return newdf
    
    except Exception as e:
        return 'error :' + str(e)

def intersection(input_data, overlay_data, *args, **kwargs):
    
    try :
    #     input_data
        in_json = json.dumps(input_data)
        read_in = gpd.read_file(in_json)

    #     overlay_data
        over_json = json.dumps(overlay_data)
        read_over = gpd.read_file(over_json)

        newdf = gpd.overlay(read_in, read_over, how="intersection")

        return newdf
    
    except Exception as e:
        return 'error :' + str(e)



def NDVIMap(parameter, *args, **kwargs):

    title = kwargs.get('title', "NDVI")
    ylabel = kwargs.get('ylabel', "Row #")
    xlabel = kwargs.get('xlabel', "Column #")

    try:

        # Open the file:
        raster = rasterio.open(parameter['data'])

        red = raster.read(parameter['red'])
        nir = raster.read(parameter['nir'])
        np.seterr(divide='ignore', invalid='ignore')
        c_map = kwargs.get('cmap', 'viridis')
        minn = kwargs.get('min', -1)
        maxx = kwargs.get('max', 1)

        # Calculate ndvi
        ndvi = (nir.astype(float)-red.astype(float)) / \
            (nir.astype(float)+red.astype(float))

        fig, ax = plt.subplots(figsize=(12, 12))
        im = ax.imshow(ndvi.squeeze(), cmap=c_map, vmin=minn, vmax=maxx)
        ep.colorbar(im)
        ax.set(title=title)
        ax.set(xlabel=xlabel + '\n'+'\n' + '© Vallaris Maps')
        ax.set(ylabel=ylabel)

        return plt.show()

    except Exception as e:
        return 'error display :' + str(e)