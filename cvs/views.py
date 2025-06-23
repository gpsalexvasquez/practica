from django.shortcuts import render

import os
import fitz  # PyMuPDF
from django.shortcuts import render
from django.conf import settings
from sentence_transformers import SentenceTransformer, util

# Cargar el modelo una sola vez (puedes usar otro más avanzado si quieres)
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def resume_matcher(request):
    context = {}

    if request.method == 'POST':
        profile_text = request.POST.get('profile_text')
        cv_files = request.FILES.getlist('cv_files')

        profile_embedding = model.encode(profile_text, convert_to_tensor=True)

        matches = []
        for f in cv_files:
            file_path = os.path.join(settings.MEDIA_ROOT, f.name)
            with open(file_path, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            cv_text = extract_text_from_pdf(file_path)
            cv_embedding = model.encode(cv_text, convert_to_tensor=True)

            similarity = util.cos_sim(profile_embedding, cv_embedding).item()
            matches.append((f.name, similarity))

        # Ordenar por score y seleccionar top 5
        top_matches = sorted(matches, key=lambda x: x[1], reverse=True)[:5]
        context['matches'] = top_matches

    return render(request, 'cvs/resume_matcher.html', context)