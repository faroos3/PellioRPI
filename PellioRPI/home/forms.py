from django import forms

class GAD7Form(forms.Form):
  first = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  second = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  third = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  fourth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  fifth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  sixth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  seventh = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])

class PHQ9Form(forms.Form):
  first = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  second = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  third = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  fourth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  fifth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  sixth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  seventh = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  eighth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
  ninth = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'Radio'}), choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')])
