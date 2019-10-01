# Account

User Account App of CLICPUST Project

## Update Information

#### Username and Library_id

`username` field was selected in `ER-Diagram`. Later we thought that `library_id` is also a _uniqe field_ can be used instead of `usename` field.

Therefore we want to remove `username` field from `ER-Diagram`.

## Regular Expressions

```
    USERNAME_REGEX = '^[a-zA-Z0-9.+-]+$'
    CONTACT_MOBILE_REGEX = '^(?:\+?88|0088)?01[15-9]\d{8}$'
    CONTACT_PHONE_REGEX = '^(?:\+?88|0088)?0\d{10}$'
    LIBRARY_ID_REGEX = '^[a-zA-Z0-9.+-]+$'
```

> [Validate Bangladeshi phone number with optional +88 or 01 preceeding 11 digits](https://stackoverflow.com/questions/30658946/validate-bangladeshi-phone-number-with-optional-88-or-01-preceeding-11-digits)

> [Telephone numbers in Bangladesh](https://en.wikipedia.org/wiki/Telephone_numbers_in_Bangladesh)
