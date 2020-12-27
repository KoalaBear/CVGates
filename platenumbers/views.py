from django.contrib import messages
from django.shortcuts import redirect, render

from platenumbers.forms import PlateNumberForm
from platenumbers.models import PlateNumber


def has_available_permits(request):
    if request.user.is_superuser:
        return True

    used_permits = len(PlateNumber.objects.filter(user=request.user))
    if request.user.permits > used_permits:
        return True
    messages.error(request, "Permits limit had been reached")
    return False


def plate(request):
    if request.user.is_superuser:
        plates = PlateNumber.objects.all()
    else:
        plates = PlateNumber.objects.filter(user=request.user)

    if request.method == "POST" and has_available_permits(request):
        form = PlateNumberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Successfully added")
            except Exception:
                pass
    else:
        form = PlateNumberForm()
    return render(request, 'plates/index.html', {'form': form, 'plates': plates})


def edit_plate(request, id):
    plate = PlateNumber.objects.get(id=id)
    if not (request.user.is_superuser or plate.user.id == request.user.id):
        plate = None
        messages.error(request, "User not permitted to edit given Plate Number")
    else:
        messages.success(request, "Successfully edited")
    return render(request, 'plates/edit.html', {'plate': plate})


def update_plate(request, id):
    plate = PlateNumber.objects.get(id=id)
    if not (request.user.is_superuser or plate.user.id == request.user.id):
        messages.error(request, "User not permitted to edit given Plate Number")
    else:
        form = PlateNumberForm(request.POST, instance=plate)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited")
            return redirect("/plates")
    return render(request, 'plates/edit.html', {'plate': plate})


def destroy_plate(request, id):
    plate = PlateNumber.objects.get(id=id)
    if not (request.user.is_superuser or plate.user.id == request.user.id):
        messages.error(request, "User not permitted to destroy given Plate Number")
    else:
        plate.delete()
        messages.success(request, "Successfully edited")
    return redirect("/plates")
