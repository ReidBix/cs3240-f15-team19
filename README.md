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

