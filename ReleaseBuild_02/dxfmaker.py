from dxfwrite import DXFEngine as dxf
def dxfmaker(Bdata,prof,rim,cup):
    Bmatrix2 = [(float(x[0]), float(x[1]),) for x in Bdata]
    prof2 = [(float(x[0]), float(x[1]),) for x in prof]
    rim2 = [(float(x[0]), float(x[1]),) for x in rim]
    cup2 = [(float(x[0]), float(x[1]),) for x in cup]
    drawing = dxf.drawing('drawing.dxf')
    polyline= dxf.polyline(linetype='LINE')
    polyline.add_vertices(Bmatrix2)
    polyline.add_vertices(prof2)
    polyline.add_vertices(rim2)
    polyline.add_vertices(cup2)
    drawing.add(polyline)
    drawing.save()
    return
