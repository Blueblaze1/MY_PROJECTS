from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from docx import Document





def text_to_decx(request):
    if request.method == 'POST':
        text = request.POST.get("text")
        if text:
            document = Document()
            document.add_paragraph(text)
            document.save("media/document.docx")
            return render(request,"txt-to-docx/txt-to-docx.html",{'typ':"1"})
        else:
            messages.info(request, 'Invalid information entry!')
            return render(request,"txt-to-docx/txt-to-docx.html")
            
    return render(request,"txt-to-docx/txt-to-docx.html")
