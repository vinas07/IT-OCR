from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from .cv2_to_str import extract_text

# Create your views here.

def main(request):
    params = {}
    if request.method == 'POST':
        file = request.FILES.get('name_file')

        if file:
            f_type = file.content_type.split('/')
        else:
            f_type = [None]

        if f_type[0] == 'image':
            text = extract_text(file)

            params['results'] = []
            params['txt'] = ''

            for i in range(len(text)):
                params['results'].append({
                    'text': text[i][1],
                    'confidence': text[i][2]
                })
                params['txt'] += (text[i][1] + ' ')

    return render(request, 'main.html', params)
