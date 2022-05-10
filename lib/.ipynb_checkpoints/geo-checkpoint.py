import math


def geo_shift(p, dist):
    
    cos_d = math.cos( p[1]  * math.pi/180 )

    lat_delt = dist / 110.574 / 1000
    lng_delt = dist / 111.320 / 1000 /cos_d


    return [lng_delt, 
            lat_delt, 
            p[0] + lng_delt, 
            p[1] + lat_delt,
            p[0] - lng_delt, 
            p[1] - lat_delt
           ]



def ll_distance(lat1, lon1, lat2, lon2, unit='K') :
    if ((lat1 == lat2) & (lon1 == lon2)):
        return 0

    else:
        radlat1 = math.pi * lat1/180;
        radlat2 = math.pi * lat2/180;
        theta = lon1-lon2;
        radtheta = math.pi * theta/180;
        dist = math.sin(radlat1) * math.sin(radlat2) + math.cos(radlat1) * math.cos(radlat2) * math.cos(radtheta);
        if (dist > 1) :
            dist = 1;
        
        dist = math.acos(dist);
        dist = dist * 180/math.pi;
        dist = dist * 60 * 1.1515;
        if unit=="K": dist = dist * 1.609344 
        if unit=="N": dist = dist * 0.8684 
        return dist;
