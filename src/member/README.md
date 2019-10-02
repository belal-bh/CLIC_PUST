# Member App

There are six type of member in CLIC and each member type is a model-class in `member` app.
These six member types are:

- Student
- Teacher
- Officer
- Staff
- Othermember
- Librarian

## Student

## Teacher

## Officer

## Staff

## Othermember

## Librarian

## ERRORS:

1. member.Staff.user: (fields.E303) Reverse query name for 'Staff.user' clashes with field name 'User.staff'.
   HINT: Rename field 'User.staff', or add/change a related_name argument to the definition for field 'Staff.user'.

Fixed:

```
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='staff_user',
        on_delete=models.CASCADE,
    )
```
