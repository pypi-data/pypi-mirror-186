import geopandas as gpd
import json

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