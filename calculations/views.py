from django.shortcuts import render
from calculations.calc import calculate
from calculations.forms import CalculatorForm
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def basic_calculator(request):
    # if this is a POST request we need to process the form data
    result = None
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # used core strategy core  logic
            result = calculate(form.cleaned_data.get("first_value"),
                               form.cleaned_data.get("second_value"),
                               form.cleaned_data.get("operation"))
            # process the data in form.cleaned_data as required
            return render(request, "index.html", {"form": form, "result": result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CalculatorForm()

    return render(request, "index.html", {"form": form, "result": result})
