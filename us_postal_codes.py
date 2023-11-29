def abbr(s):
    for i in [['ad','VI'],['ak','AK'],['zn','AZ'],['st','MN'],['iu','CT'],['ri','GA'],['wi','HI'],['an','ME'],['ln','MD'],['ai','PA'],
['mn','VT'],['ii','VA'],['tn', 'MT'],['vd','NV'],['se','TN'],['ea','TX'],['mi','DC'],['Iw','IA'],['na','KS'],['uk','KY'],
['in','LA'],['ip','MS'],['or','MO'],['ad','MP']]:
        if s[-4]+s[-2] in i[0]:
            return i[1]
    if ' ' in s:
        return s[0]+s[s.index(' ')+1]
    if s:
        return s[:2].upper()