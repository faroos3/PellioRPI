from django import forms

class MainForm(forms.Form):
  interested = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  distressed = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  alert = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  excited = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  upset = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  strong = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  scared = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  jittery = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
  enthusiastic = forms.ChoiceField(choices=[(1, 'Not at all'), (2, 'A Little'), (3, 'Moderately'), (4, 'Quite a Bit'), (5, 'Strongly')], widget=forms.RadioSelect())
