# Library
This project aims to create a secure computerized system to maintain all the daily work of the library. This website manages all actions that occur in a library by keeping a record of all students, books, and employers that interact with the system. Unlike other Library Systems, our website provides detailed reports and history charts to track the actions and events taking place in the library.

## Implemetation of RBAC
The Library Management System has different types of users including students, librarians and admins. Hence, it is important to implement role-based access control to restrict control based on the authority of the user. Here is the list of roles along with access rights of the Library Management System:
* Unauthenticated_user: This user cannot be identified as they have not logged into the system. Hence they are given very limited access.
* Student: Students may use the website to borrow or return books. Apart from this they may view other information regarding employees and borrowers.
* Librarian: The librarian is in charge of maintaining the library facilities and employees. They must have access to all related pages and functions.
* Admin: The admin may log in by navigating to the /admin URL to reach a Login page. The admin is allowed to access all functions and pages in the website. There are no restrictions as the admin is the highest authority in the system.


### User Type: Role Permissions
#### Unauthorised_user
* View home page
* View login page
* View signup page
* View book
* View borrowers
* View employers

### Student
* New issue book
* Return book
* View book
* View employees
* View borrowers
* View Issued books
* View returned books

### Librarian
* Add book
* Add borrower
* Add employer
* View book
* View employees
* View borrowers
* View issued books
* View returned books

### Administration
* Add book		
* Add borrower		
* Add employer		
* View book		
* View employees	
* View borrowers		
* View issued books
* View returned books
* Return book
* Issue book
* Add user
* Edit user details

If any user is unauthorized to view a page or perform an action, they will be shown as a message stating that they are unauthorized as shown in the screenshots of the result section.
And if the data which the user is requesting doesn’t exist, it will show a 404 error with a message stating the reason.


## Installing
- `git clone https://github.com/Niwedita17/Library.git`
- `./run.sh`

