from django.shortcuts import render
import stepic 
from PIL import Image
import io
# Create your views here.

def index(request):
    return render(request,'index.html')

def hide_text_in_image(image,text):
    data=text.encode('utf-8')
    return stepic.encode(image,data)

def encryption_view(request):
    message=" "
    if request.method=="POST":
        text=request.POST['text']
        image_file=request.FILES['image']
        image=Image.open(image_file)

        

        new_image=hide_text_in_image(image,text)
        image_path='encrypted_images/'+ 'new_'+image_file.name
        new_image.save(image_path)
        message=" Massage is been encrypted in the image"

    return render(request,'encryption.html',locals())

def decryption_view(request):
    text=""
    if request.method=='POST':
        image_file=request.FILES['image']
        image=Image.open(image_file)

        
        text=extract_text_from_image(image)

    return render(request,'decryption.html',locals())

def extract_text_from_image(image):
    data=stepic.decode(image)
    if isinstance(data,bytes):
        return data.decode('utf-8')
    return data
