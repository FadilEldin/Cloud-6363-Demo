#=================================================
# Fadl Eldin
# A quick-and-dirty helper code to draw a polygon in an image. 
# The image and bounding polygon are both hardcoded
# Input: Image and polygon vertices (Hardcoded)
# Output: Polygon drawn on logo detected in input image
#
# Usage Example:
# Go to detecting logos URL  https://cloud.google.com/vision/docs/detecting-logos
# Scroll to "Try this API"
# Copy-paste "Replace image" with a URL of an image that has a logo, e.g.
# https://cdn.motor1.com/images/mgl/jpZ37/s1/mercedes-amg-e-53-coupe-2020.jpg
# or
# https://mk0futurumreseabr7pm.kinstacdn.com/wp-content/uploads/2020/01/aws-logo-1536x1152.png
# Copy the resulting polygon indecis back into the code and run.
# Output image name with yellow polygon on logo is "output-polygon-on-logo.jpg"
#=================================================
import argparse
import io
import json
from PIL import Image, ImageDraw
# pip install pillow
import requests

def draw_polygon(url, bounding_poly):
    im=Image.open(requests.get(url, stream=True).raw)
    #im=Image.open(url)

    #im = Image.open(image_file)
    draw = ImageDraw.Draw(im)
    poly=json.loads(bounding_poly)
    x0=poly['vertices'][0]['x']
    x1=poly['vertices'][1]['x']
    x2=poly['vertices'][2]['x']
    x3=poly['vertices'][3]['x']
    y0=poly['vertices'][0]['y']    
    y1=poly['vertices'][1]['y']  
    y2=poly['vertices'][2]['y']  
    y3=poly['vertices'][3]['y']  
    #draw.polygon([x0,y0,x1,y1,x2,y2,x3,y3], None, 'yellow')
    # Ploygon does not have width https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html
    draw.line([x0,y0,x1,y1], 'yellow', 4)
    draw.line([x1,y1,x2,y2], 'yellow', 4)
    draw.line([x2,y2,x3,y3], 'yellow', 4)
    draw.line([x3,y3,x0,y0], 'yellow', 4)
    
    out_image_file = 'output-polygon-on-logo.jpg'
    
    im.save(out_image_file, 'JPEG')
    print('Saved new image to {}'.format(out_image_file))
#---------------------------------
if __name__ == '__main__':

    #URL of Mercedes:
    # https://cdn.motor1.com/images/mgl/jpZ37/s1/mercedes-amg-e-53-coupe-2020.jpg
    url ="https://cdn.motor1.com/images/mgl/jpZ37/s1/mercedes-amg-e-53-coupe-2020.jpg"
    bounding_poly='{"vertices": [{"x": 624,"y": 618}, {"x": 741,"y": 618 }, {"x": 741,"y": 730 },{"x": 624,"y": 730}]}'
    
    #-----------------------------------
    # NVIDIA:
    # https://media.threatpost.com/wp-content/uploads/sites/103/2020/03/02145658/nvidia.jpg
    #url ="https://media.threatpost.com/wp-content/uploads/sites/103/2020/03/02145658/nvidia.jpg"
    #bounding_poly='{"vertices": [{"x": 207,"y": 46},{"x": 521,"y": 46 },{"x": 521,"y": 385 },{"x": 207,"y": 385 } ]}'
    
    #-----------------------------------
    # Many logos of luxury cars
    # http://1.bp.blogspot.com/-NfZ6vVtQurQ/UoXecgj5clI/AAAAAAAACj4/0605p-MKhbo/s1600/luxury+car+logos+2.gif


    draw_polygon(url,bounding_poly)
