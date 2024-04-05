from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
import math 
import random
from django.views import View


# Create your views here.

class PythonView(TemplateView):
    template_name="python.html"

class kg1View(TemplateView):
    template_name="kg1.html"



# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# current_letter = 0

# def learn_alphabet(request):
#   global current_letter
#   current_letter = (current_letter + 1) % len(letters)  # Circular letter update
#   context = {
#       'letter': letters[current_letter],
#   }
#   return render(request, 'kg1.html', context)
    
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def learn_alphabet(request):
    session = request.session  # Access session object

    # Check if 'current_letter' key exists in session
    if 'current_letter' not in session:
        current_letter = 0  # Initialize to 'A' if not in session
        session['current_letter'] = current_letter  # Store in session
    else:
        current_letter = session['current_letter']  # Retrieve from session

    current_letter = (current_letter + 1) % len(letters)  # Circular letter update

    context = {
        'letter': letters[current_letter],
    }

    session['current_letter'] = current_letter  # Update session for next request

    return render(request, 'kg1.html', context)


class oneView(TemplateView):
    template_name="1.html"

class twoView(TemplateView):
    template_name="two.html"

class ThreeView(TemplateView):
    template_name="three.html"

class FourView(TemplateView):
    template_name="four.html"
    
class FiveView(TemplateView):
    template_name="five.html"

class SixView(TemplateView):
    template_name="six.html"

class SevenView(TemplateView):
    template_name="seven.html"

class EightView(TemplateView):
    template_name="eight.html"

class NineView(TemplateView):
    template_name="nine.html"

class TenView(TemplateView):
    template_name="ten.html"

class firstdetailView(TemplateView):
    template_name="firstdetails.html"

class Traceandweite(TemplateView):
    template_name="traceandwrite.html"



class CountingGameView(View):
  def get(self, request):
    correct_answer = self.generate_random_number()
    context = {'correct_answer': correct_answer, 'result': ''}
    return render(request, 'countinggame.html', context)

  def generate_random_number(self):
    return random.randint(0, 10)   # Generate random number between 1 and 3


