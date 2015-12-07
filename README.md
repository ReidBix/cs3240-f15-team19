# cs3240-f15-team19
Advanced Software Project Group 19

#how to see file upload thing
1. Pull
2. cd into dev/

(can use python3 or python dependent on system)

3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. python3 manage.py runserver
6. Go to server that they give you (i think it's http://127.0.0.1:8000/), should be there


(Superuser ID: admin, Superuser PW: admin)

#Update tuesday, November 3:
1. When you upload a document, all of the standard fields we need are there and are passed when the document is uploaded
2. timestamp isn't the right timezone, but is still a timestamp, but will be fixed soon (fixed)
3. Need to fix size of input boxes (specifically the one for longer description) but it's being annoying (aesthetics not great, but functionality is good)
4. Files that are uploaded are assigned to the user that is signed in
5. The admin can see every file that has been uploaded
6. User can only see the files they have uploaded themselves
7. 

#TODO
1. Groups -> Integrate Groups into Reports
2. Site Manager Roles -> (access any user's reports)
3. Reports -> Deleteable by SM user
4. Owners of Reports/Folders ->  rename, delete, edit existing report NOT SM user
5. Search -> Fix the shit out of it (Big)
6. FDA -> Fix to new report style
7. Security -> Hash for verifying integrity of report

#How to Use Stand-Alone App

1. Update the Server
2. Run StandAloneApp.py
3. Success
4. Login with Users that have been created/are in the database
5. Look at the documents that you as a user created (AND THAT'S IT)

#Messaging 

Link to already existing repository for messaging: https://bitbucket.org/psam/django-postman/wiki/Quick_Start_Guide

1. messaging works kinda, still needs some tweaks though<br />
2. i can send messages to users that don't have an email associated with it<br />
3. go to the server/SecureWitness/messages to see messaging system<br />
4. have to log in as admin to approve messages being sent before the user actually gets it <br />
5. need to change #4, and figure out why only emails without email associated to it works (fixed)

#Encryption

1. Very very very low level stuff
2. Private and public key pairs assigned to currently existing users, can add new to new ones but not automatically
3. Can encrypt and decrypt files of any type with seperate key that will be encrypted with public key and attached with document
4. Obviously won't be able to decrypt without the private key to decrypt the key for the file
5. Nothing added yet to the stand alone app because I spent far too long ironing out bugs (i.e. F word docs and pdfs)

#File Upload Attempts
1. Works, can now create reports with 1 file and can edit reports to attach additional files to the report. 
2. Can also change other fields of hte report or delete it entirely. 
3. If you want to make some fields of a report unwrittable, just go to forms.py and remove it from the fields of ReportForm 
(ignore the block of comments)
2. Have to work on folders and search functionality

#UserList (username - password - privatekey)
1. admin - admin - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQDHmyx3ygL9vFkEAaVE8p7ksm/nUJGaED+zHo2mzRzxg5c9kUXDNHQLqGRhJdU4i6ouCr48XhSHq5TvovX5TlKvSMVQgfi/GR9pfDCXzQVwbVLSi1kDgEJoK9KKpvmgHQBfRFqR4c5Vwp5xU8/HqTJRspqfCLWXjaOxvNrroOoxCQIDAQABAoGAOW08eu5EtAmHNq7ehJqk+jkYFt3INiHsobTtngqvBBEO5yivgHzL0jrNPmHrGUydVofCuY17rJjBzbv9to9BHCgiJ5s4gi3KiCmpt2qESuNWJdxLUm51bcuV8RSUCPw5t6TK3hFpQpzKPspmxxiufoxITThOijhv+BPTKf8+loECQQDKmGhIH/qruLuaQoAcZbrS3AQ4VYno14YGwpSKvgqkVfeQ8rG2x+xQTfTzDw059xzAuF7+ifv5rxTYl3/pkEi5AkEA/DkMfF+72yMCtftiNmslauAKerKSUZdi5er7OMw+Cye5r+xMBblHaFZGhYaqOwS+werPhDFbetW+olCstIhi0QJBAJwWJ+HJoZtDzGXg7krypalnEWlFnebihcQXjdIG8LQD96SZFwo3pX2JUjshUZNjK6ffZHC/Zn7LwUfOESKloyECQQCcKq6Ca7wi6MCK8QVUcG8Qh3u1kM9r2XIQrbey6TMZMRWVyZcgjCGchp7PmhvYww1hgAPQ88aSfbm1QoJMnY2hAkA7xp6bDxMFfQt/T9fIq4Hbt0ByjRyUL5x8VzdxGrVXzcsk9NqAbKAQAf7NNTDdBXEJGMqUyfONw5J2vQUoHJls-----END RSA PRIVATE KEY-----
2. 
