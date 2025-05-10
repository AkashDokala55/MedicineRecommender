from django.shortcuts import render
from .utils import fetch_medicine_data, process_input

def index(request):
    return render(request, 'index.html')

def recommend_medicine(request):
    if request.method == 'POST':
        user_input = request.POST.get('symptoms', '')
        processed_input = process_input(user_input)

        medicines = []
        if processed_input:
            medicines = fetch_medicine_data(processed_input[0])  # First symptom only

        return render(request, 'results.html', {'medicines': medicines})

    return render(request, 'index.html')
