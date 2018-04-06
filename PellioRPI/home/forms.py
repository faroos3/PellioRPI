from django import forms

class GAD7Form(forms.Form):
  feild1 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  feild2 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  feild3 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  feild4 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  feild5 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  feild6 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  feild7 = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
