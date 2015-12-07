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
4. Owners of Folders ->  rename, delete, edit existing report NOT SM user
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

#UserList (username - password - privatekey) MUST CREATE NEW SERVER FOR NEW KEYS
1. admin - admin - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQCebbDB23yjZWgw9Ry9eXdaJvQgvDhHx6ioLaIq5IqEL/hMEx+0W09yo8yaJy3GYVkk9N3CbvdBO8ldkjcKegfZb0pF/v/NtzCjNMvSvIwvCtvGzjSqaMBvMUKAtzFdqQP2PcSV+NyCMCpUG2BAb8AQvZNp52NnsLEB8e1+E1USyQIDAQABAoGAb+9QU6egCFI9q1mDVNvdV/Ttx7M0kIKgxzJ2wZd3xq2d4SIh5GwfVgAlL0U/MkrVkSbxB88fIxf6zgHgoaZWpEwr812os0axl8kBw03iGOCVytx1StmHB1jKau8jZlBnT8p6lYM973vegHZfVuAuWIb+XPOT005brz+4xHK5W4ECQQC4WoxIJZFm8qVF8cTdzj7/2y+WYiK6E/sb3UVWt/tQI1tRZB+OnCOt7E4ngNzLcJ3xGs+JND4WLnbcGkckG2X7AkEA2//T2E/K0vUcNz8u3gEhCMxWMDbNTlTf09ZwT5Z0/bB7grMVTJlBWgEvDx55wluE5zxt3MO8QZ1FZ7GTwLVDCwJBAJol5GyjNRxewgFlMlbBEP6BOR5GuoDbGjnnYAYt2q7ckYvR620kc9UG5Sa04modpYMoBubTzyJfAbXzJw8y9acCQQCFECQ65nAfzn8Fb2LShk5LuwO6X7sn0LAcucvuZ2tVceQSdmzAisV7QdILy/wLMT2eeu9cIst/yDcNc9uRKFFnAkA8Kh1OwldatObUvFCfxY/59XW8JqWdT0VFQLCxNc3srKpo/ECW3iAcMUqkiXMvBqQEns2OSziM7QE1zdiE1XUs-----END RSA PRIVATE KEY-----
2. Reid - pass - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQC+9KWZgwqoBenNqZ2XPbaN07OQ+rptbwqg3JeFkTXhqUQjMw3qFQocojw1VgO7MjyWFi1G0a+NqvGayjnyMNoQRy4j6I20YDqrx0258nb/LAa8JJsGg1hoh0r2bFco0ekL0/Kpdd2jcXfc3U8eCMjZ6IdhI4btXeAT/oyPy8ykwQIDAQABAoGBAJVxrfB4Z+ybxCEar6TfvXE9z3iVYTWoA69lNIhp3rte116c5DTghmtmZKxxRrZIWLY1YPXdwQCkWjWEMtlidiWNdqBy20eJkE/vOVIIhJNJW2ubeZdMPDB1AF7dtRvZjadLx1+hknbxaKr5ZY1Qh1z+QyU6UsFj8YKKqJbDEPzhAkEAvz291VHT8WAbtUVhcFpD1ojXK/D/KlrAlqFkwbi2B8VmGu+ePW79NUVrF8Fm+qg6HyMVL6NcM8UVwC8hMtToDQJBAP+eJ1ujUqh0CRcMKalR/TfuId6sgq6DWPkSzgACS4uXeDIQ1SF7ahJQB87BOJEvBXCbbqyf0UxZylL0ABBE7oUCQByb0+Yxk48sXXjEpEr2deeGGQpNxx5C7USbaENCqpiHAztMVVPDYsWxWM/48rrUp704tlamDYkBFrvlUQYVq5ECQQDwhv05+YD6CdXT3hoFvaSsUGOGiIWfePDrzooQ8BfuDmWHltc2Xk79VFlEcASueLSBtYB65xem5IbBb9/vby2RAkBvF/YQnpM6W+Y5tbz6740Ncq9XrksH0y5lCg5cCbWtMiZIqq4CFCM72DaPii/j+KRA6+QUDFVAc0LMpor85ZpE-----END RSA PRIVATE KEY-----
3. User1 - pass - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQDcnacC87oaP5Ad2xO2TrzWAGjeZq/+YFFIDZXukn7QIEyo4zNVSVCRJN8asPdwDrE4k6VV3U8+hWzVWdqDTX/GOvcHUetAU/YlaI/xrNm+BZP4wkRbLxW6DqqQBnVxPIKsNti4kLj5K6GkihIqIKkNwbqRq9hmWw8S0mAholYHZwIDAQABAoGAdQPl1soBtvRp83wE65i9zmBvPy+GP81Er4wNL3piavAG2TmRO7ZkVmgRMi4VQEl6tICTnISDCK1qeYtsPGK51yXJ2NUOu7eJBrv3k4xQSFhmiWhF0fBZP+uqSr7H1FcePQioDBzurn2eADHgDi5HqtGJBMvKKo02AA1japr51gECQQDsdghviHh+72KQAsguURC07VfzyQalQvd6m8zkMHSB8i/C31fGYWXsVqsY3kUCiBe8KNe4FPrErpeXrhQ9LSEBAkEA7thwIzChJsKmy1ZKzhg61cYZMHc75S/TAIG/7CDVaOEvoGWLFdZ+P6Zt1xjd2KywOecye3S4S0a32B/lH23AZwJBAJ+3vkzvxkwfD9ksN+CpGvrKkiz1rQp1qEnl8Mh1Pk0DtGURjO1PnpO7msgqYjyqhjWu9L6/VP8C2xw2Fi+YSwECQBxFF/jCT8Czt2RH4XDFY2lcGi0nX7p/z5y2vs2nETtps+ZrPmwmSCkmfMfB1LhJsE4aNFpydUHLrATzuX3f0q8CQD4rpP5Q7RYwx2nS/cvEq9UTtpyNpsF+ZmXEXrnJ9OND/XZClnf/P4C4QiFZ3vF+TMmxRAeN7/Pr1+Xgq7j/kf8=-----END RSA PRIVATE KEY-----
