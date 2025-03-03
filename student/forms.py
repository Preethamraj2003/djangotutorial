from django import forms
class StudentSearchForm(forms.Form):
    usn = forms.CharField(max_length=15, label="Enter USN")
    sem_id = forms.IntegerField(label="Enter Semester Number")
