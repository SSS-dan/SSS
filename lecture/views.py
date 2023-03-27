from django.shortcuts import render, redirect, get_object_or_404
from .models import Lecture
from .forms import LectureForm

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'timetable.html', {'lectures': lectures})

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture})

def lecture_new(request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture_detail', lecture_id=lecture.pk)
    else:
        form = LectureForm()
    return render(request, 'lecture_edit.html', {'form': form})

def lecture_edit(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance=lecture)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('lecture_detail', lecture_id=lecture.pk)
    else:
        form = LectureForm(instance=lecture)
    return render(request, 'lecture_edit.html', {'form': form})

def lecture_delete(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    lecture.delete()
    return redirect('lecture_list')
