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
2. timestamp isn't the right timezone, but is still a timestamp, but will be fixed soon
3. Need to fix size of input boxes (specifically the one for longer description) but it's being annoying (aesthetics not great, but functionality is good)
