from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import render
from .forms import NumberForm
from django.views.generic import TemplateView

def home(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
        	start_time = timezone.now()
        	start_time = '{:%S}.{:03d}'.format(start_time, start_time.microsecond // 1000)
	        nth_term = form.cleaned_data['nth_term']
	        nth_term = get_fibonacci( nth_term )
	        end_time = timezone.now()
	        end_time = '{:%S}.{:03d}'.format(end_time, end_time.microsecond // 1000)
	        time = time_total( start_time, end_time )
	        return render( request, 'fib/index.html', {'form': form, 'nth_term': nth_term, 'time': time } )
    else:
        form = NumberForm()
    return render(request, 'fib/index.html', {'form': form})

# returns the nth term from fibonacci series
def get_fibonacci( term ):
	first_num = 1
	second_num = 1
	if term == 1:
		return first_num
	if term == 2:
		return second_num
	count = 3 
	third_num = 0;
	while ( count <= term ):
		third_num = first_num + second_num
		first_num = second_num
		second_num = third_num
		count += 1
	return third_num

# gets the total time taken
def time_total( start_time, end_time ):
	st_time_milli = start_time.split( "." )
	end_time_milli = end_time.split( "." )
	st_total_milli = int( st_time_milli[0] ) * 1000  + int( st_time_milli[1] )
	end_total_milli =int( end_time_milli[0] )  * 1000 + int( end_time_milli[1] )
	time_differ = end_total_milli - st_total_milli
	return str( time_differ ) + ' milli sec'