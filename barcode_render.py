
//*********** requirments.txt ****////
reportlab==3.4.0
Django==1.10.2
pyBarcode==0.7

//************** urls.py *******//



urlpatterns += [ url(r"^barcode/(?P<data>\w+)/$",BarcodeGenerator.as_view(),name="barcode_generator")
]

//************** view.py *******//

from barcode.writer import ImageWriter
from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String


class BarcodeRender(Drawing):
    def __init__(self, data, barHeight=10, barWidth=10,*args, **kw):
        barcode = createBarcodeDrawing('Code128', value=data,  barHeight=barHeight*mm, barWidth = barWidth*mm,humanReadable=True)
        Drawing.__init__(self,barcode.width,barcode.height,*args,**kw)
        self.add(barcode, name='barcode')

    def asBinary(self,format="gif"): #format png, gif, jpeg etc..
        return self.asString(format=format)

## using Report LAB
class BarcodeGenerator(APIView):
    
    def get(self,request,data=None,format=None):

        mybarcode = BarcodeRender(data,barHeight=20,barWidth=1)

        return HttpResponse(mybarcode.asBinary("png"), content_type="image/png")
    def post(self,request,format=None):
        pass

## using pybarcode
class BarcodeGenerator(APIView):

    def get(self,request,data=None,format=None):
            ean = barcode.get_barcode('ean13', data, writer=ImageWriter())
            print "data is %s" % (ean.get_fullcode())
            ean.save("mybarcode")
            image_data = open("mybarcode.png", "rb").read()
            return HttpResponse(image_data, content_type="image/png")