from django import forms
from .models import Books, Student, Employer, Issue, Return, Sborrower

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Sborrower
        fields = '__all__'

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['issue_date', 'issue_id']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        exclude = ['return_id', 'return_date']
