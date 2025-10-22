from django import forms

class QuizForm(forms.Form):
    question = forms.CharField(label='Question', max_length=200)
    option_a = forms.CharField(label='Option A', max_length=100)
    option_b = forms.CharField(label='Option B', max_length=100)
    option_c = forms.CharField(label='Option C', max_length=100)
    option_d = forms.CharField(label='Option D', max_length=100)
    answer = forms.CharField(label='Correct Answer', max_length=1)