from ..models import Measurement

def get_measurments():
    Measurments = Measurement.objects.all()
    return Measurments

def get_measurment(var_pk):
    variable = Measurement.objects.get(pk=var_pk)
    return variable

def create_measurment(var):
    variable = Measurement(name=var["name"])
    variable.save()
    return variable

def update_measurment(var_pk, new_var):
    variable = get_measurment(var_pk)
    variable.name = new_var["name"]
    variable.save()
    return variable