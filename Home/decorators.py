from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == None:
            return view_func(request, *args, **kwargs)
        if group == 'manager':
            return redirect('ManagerHome')
            
        
    return wrapper_function