from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import BookForm, BorrowerForm, EmployerForm, IssueForm, ReturnForm
from .models import User, Books, Student, Employer, Issue, Return, Semester, SBorrower, Librarian
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q
from .decorators import unauthenticated_user, librarian_only, student_only
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Create your views here.

@unauthenticated_user
def student_signup(request):
    if request.method == "POST":
        student_id = request.POST['student_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        try:
            group = Group.objects.get(name='Student')
        except Group.DoesNotExist:
            group = None

        user.groups.add(group)
        student = Student(student_id=student_id, user=user)
        student.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/student_signup.html')

@unauthenticated_user
def librarian_signup(request):
    if request.method == "POST":
        librarian_id = request.POST['librarian_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        try:
            group = Group.objects.get(name='Librarian')
        except Group.DoesNotExist:
            group = None

        user.groups.add(group)
        student = Student(student_id=student_id, user=user)
        student.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/librarian_signup.html')


@unauthenticated_user
def student_login(request):
    if request.method == "POST":
        userid = request.POST['userid']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                student = get_object_or_404(Student, pk=userid)
                if student:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'student_login.html',
                                  {'error_message': 'Invalid security credentials'})
            else:
                return render(request, 'student_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'student_login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/student_login.html')


@unauthenticated_user
def librarian_login(request):
    if request.method == "POST":
        userid = request.POST['userid']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                librarian = get_object_or_404(Librarian, pk=userid)
                if Librarian:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'librarian_login.html',
                                  {'error_message': 'Invalid security credentials'})
            else:
                return render(request, 'librarian_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'librarian_login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/librarian_login.html')


def index(request):
    return render(request, 'libman/home.html')


@login_required
@librarian_only
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('view_books')

    else:
        form = BookForm()

    return render(request, 'libman/add_book.html', {'form': form})


def view_books(request):
    books = Books.objects.order_by('department')
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(Q(book_name__icontains=query) | Q(author_name__icontains=query) | Q(book_detail__icontains=query) | Q(department__icontains=query))
    else:
        books = Books.objects.order_by('department')
    return render(request, 'libman/view_book.html', {'books': books})



def view_borrower(request):
    borrower = SBorrower.objects.order_by('batch')
    query = request.GET.get('q')
    if query:
        borrower = SBorrower.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(phone__icontains=query) | Q(depart__icontains=query) | Q(borrower_id__icontains=query))
    else:
        borrower = Student.objects.order_by('batch')
    return render(request, 'libman/view_borrower.html', {'borrower': borrower})


@login_required
@librarian_only
def add_borrower(request):
    if request.method == 'POST':
        s_form = BorrowerForm(request.POST)
        if s_form.is_valid():
            s_form.save(commit=True)
            return redirect('add_borrower')
    else:
        s_form = BorrowerForm()
    return render(request, 'libman/add_borrower.html', {'s_form': s_form})


def view_employer(request):
    employer = Employer.objects.order_by('timer')
    query = request.GET.get('q')
    if query:
        employer = Employer.objects.filter(Q(Fname__icontains=query) | Q(Lname__icontains=query) | Q(phone__icontains=query) | Q(timer__icontains=query) | Q(emp_id__icontains=query))
    else:
        employer = Employer.objects.order_by('timer')
    return render(request, 'libman/view_employer.html', {'employer': employer})


@login_required
@librarian_only
def add_employer(request):
    if request.method == 'POST':
        e_form = EmployerForm(request.POST)
        if e_form.is_valid():
            e_form.save(commit=True)
            return redirect('add_employer')
    else:
        e_form = EmployerForm()
    return render(request, 'libman/add_employer.html', {'e_form': e_form})



def view_issue(request):
    issue = Issue.objects.order_by('borrower_name', 'issue_date')
    return render(request, 'libman/view_issue.html', {'issue': issue})


@login_required
@student_only
def new_issue(request):
    if request.method == 'POST':
        i_form = IssueForm(request.POST)
        if i_form.is_valid():
            name = i_form.cleaned_data['borrower_id']
            book = i_form.cleaned_data['isbn']
            i_form.save(commit=True)
            books = Books.objects.get(isbn_no=book)
            semest = Student.objects.get(student_id=name).semester
            departm = Student.objects.get(student_id=name).depart
            Books.Claimbook(books)
            return redirect('new_issue')
    else:
        i_form = IssueForm()
    semest = None
    departm = None
    sem_book = Semester.objects.filter(sem=semest, depart=departm)
    return render(request, 'libman/new_issue.html', {'i_form': i_form, 'sem_book': sem_book})


@login_required(login_url='/login/')
@student_only
def return_book(request):
    if request.method == 'POST':
        r_form = ReturnForm(request.POST)
        if r_form.is_valid():
            r_form.save(commit=True)
            book = r_form.cleaned_data['isbn_no']
            books = Books.objects.get(isbn_no=book)
            b_id = r_form.cleaned_data['borrower_id']
            Books.Addbook(books)
            Issue.objects.filter(borrower_id=b_id, isbn=book).delete()
            return redirect('return_book')
    else:
        r_form = ReturnForm()
    return render(request, 'libman/return_book.html', {'r_form': r_form})

def redir(request):
    return redirect('home')

'''
@login_required(login_url='/login/')
class ViewUpdatePost(UpdateView):
    model = Books
    template_name = 'libman/update_book.html'
    fields = ['book_name', 'author_name', 'book_detail', 'no_of_books']

    def get_object(self, queryset=None):
        isbn_no = self.args['isbn_no']
        return self.model.objects.get(isbn_no=isbn_no)

    def form_valid(self, form):
        form.save()
        return redirect('view_book')
'''

