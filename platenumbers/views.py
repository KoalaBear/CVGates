from django.shortcuts import redirect, render

from platenumbers.forms import PlateNumberForm
from platenumbers.models import PlateNumber


def plate(request):
    if request.method == "POST":
        form = PlateNumberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/plates/show')
            except Exception:
                pass
    else:
        form = PlateNumberForm()
    return render(request, 'plates/index.html', {'form': form})


def show_plate(request):
    if request.user.is_superuser:
        plates = PlateNumber.objects.all()
    else:
        plates = PlateNumber.objects.filter(user=request.user)
    return render(request, "plates/show.html", {'plates': plates})


def edit_plate(request, id):
    plate = PlateNumber.objects.get(id=id)
    if not (request.user.is_superuser or plate.user.id == request.user.id):
        plate = None

    return render(request, 'plates/edit.html', {'plate': plate})


def update_plate(request, id):
    plate = PlateNumber.objects.get(id=id)
    if not (request.user.is_superuser or plate.user.id == request.user.id):
        plate = None

    form = PlateNumberForm(request.POST, instance=plate)
    if form.is_valid():
        form.save()
        return redirect("/plates/show")
    return render(request, 'plates/edit.html', {'plate': plate})


def destroy_plate(request, id):
    plate = PlateNumber.objects.get(id=id)
    if not (request.user.is_superuser or plate.user.id == request.user.id):
        plate = None

    plate.delete()
    return redirect("/plates/show")
