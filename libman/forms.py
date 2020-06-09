from django import forms
from .models import Books, Student, Employer, Issue, Return, SBorrower

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ['book_id']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = SBorrower
        fields = '__all__'

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'

class IssueForm(forms.ModelForm):
    borrower_name = forms.CharField(
         required=False,
     )
    book_name = forms.CharField(
         required=False,
     )
    class Meta:
        model = Issue
        exclude = ['issue_date', 'issue_id', 'book_id']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        exclude = ['return_id', 'return_date', 'book_id', 'borrower_name', 'book_name']
