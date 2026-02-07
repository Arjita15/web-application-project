from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


@login_required
def home(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("home")
    else:
        form = NoteForm()

    notes = Note.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "home.html", {"form": form, "data": notes})


@login_required
def read_one(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    return render(request, "read_note.html", {"data": note})


@login_required
def update_one(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = NoteForm(instance=note)

    return render(request, "update_note.html", {"form": form})

@login_required
def delete_one(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":
        note.delete()
        return redirect("home")

    return render(request, "delete_note.html", {"data": note})