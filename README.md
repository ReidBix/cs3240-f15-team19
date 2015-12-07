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
1. Public/Private Key Encryption Checks
4. Owners of Folders ->  rename, delete NOT SM user
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
1. admin - admin - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQCpqSVdPgWRJiMZwLAPLR+uGKpbBw8bZSo/yRU4DlIEHHD+Rs0WUALUG3ql10+1kMbtrNgu77rJnZjol5sg/AuzXaUiYwc4luGE/CIS3MGaGUUGUhUNsLoZ2vbgNxk5B7qr6Das4SEcRuqfO0HaOJvqAl/7NlM9QMmGTs/gQasFBQIDAQABAoGAOINVJNfx9sVjT8K1Yni/YrholmWljJSIHDMY1FFA1Im8wZZH3jTMnGaC1hcAQBR3jtfSMuA7scjDFEbbr4MFSjDyL5DawSb1QhNO2S03rc4mbnkivDrTli+wSbCbLQXbR8Cv1x/jCkLpOS3Dy3s7ccaVWWIyIpxu0B1cHXQkhAkCQQDKPW6rao/wA/GFC3G3i9or3lO3qCoWIYLF6NOevfZ8VM0BNRmkpOadq4no7YusS4vkDv3OUhFOmRAcGZ9j852jAkEA1sKshzL/pVwTGFLUgj3mUtA1sUdexAqWhyEf4yQZvvg6X4p0ZcMh9dpk9ay8swaL1HJXf47Y+5Pga0e6kM+tNwJBAJvaVdQiDgSwdUrLc/o3+4z9C9Un8i8V6hqsf5EA4dgU3duFWVqpfdOaI3Bux8mieo7pAq0iT5YbnO+ay1uSnTMCQBIXilNFb5XtoMouyCpErq+RTMSnf4tCXRX7K2WGOAkHfltoHZApFSZSBKlRqP/n8EWwcECVtx/SgFhpTYU/iZcCQALAwDdoVmwE71u+GJBGYW97QH3ZJZJ80L0xuy8p4illYcGLy+HlwR5Jvj5dPt4JzFqVUz0woIfrIsXqOuAdtR8=-----END RSA PRIVATE KEY-----
2. Reid - pass - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQCh2HlUNaJtCOEhGzGwxX+NO0x0bYSLVkXxOFJCOgagJMiIfcuU/K9X1YV9/Rs/Km3Uuq2iQNiEvW+77h2Xm3YatvhoHhOjclXFTa+2CYkf6hk9rPKjLQY3QB9KU1YDPBuptqwIXGY7OnrAXdrbf9//u9QqThlGLa52/dvWfQ+apwIDAQABAoGBAItL27FEsFWT7OAnna79bPjLbtROZmPejzg8N2BUvNscjZQcYRoMGYZJeimjrM3C4ODVAxjBIxmsSfy/xqxz20NnGRtcGyW3LE/PP3+9v6MFMQx6DkpKJ76HHUlkw3mYzesx2M5dOc9OihFmASt6KC7Vd2o8KWwNLRu3jeau9WJxAkEAucAPnEC32ofP6UJfdunbyZHa38UGF96+Pcea96ck8ATC4mcnm1CI4PIPx1Z6EyAV62ClfmFG/pVDfPUywUdFpQJBAN8OBHK5+jSg6e4TGUdioxQML0ZvW2rQa7LDzvkoJ3v0dp6o9eUAeNz7RQifQpMxR/stACSnfBTZ92bAbua1JVsCQH+FGzJqO84K7vF0X5WDdyAqwdhdqpE4meJP5lOeq/0bR6+moco+v7mudKak96mpnWK6NuNMZTDhyDNBIlcOVwECQDYLSGqfww7TWjqz5/ES5h5qYV34hzbXLvEOXmyiHQb8kW0Z1RJaTe6E9xICvHe7fgxOt/Upm3fV5ArCX1yI0XcCQDAsNxlCGIEWyEvy+mWO6G/79ZcseydA7UCzAqzmbJbow0JLPuALqDjyk6AePAC9XeLOJpf3QanTNzTHTTYbgu0=-----END RSA PRIVATE KEY-----
3. User1 - pass - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQCt2QB/1T1QEAcN6t8DbfGe0HKuxBPgrQlSozRl8LzQnolRxNhkBJONPRVKmT8kPSH59ctCJddVBdM9SsCK083Re3vI+WSD6oA685UeOtNUDJZm14CBYPs4pWAnfOimEL9+ScnfdX2b0qAOUhiBnsYqU6TWnsBG1+CRKlId2uxM6wIDAQABAoGAHZs8K4kMNQtVuDgMnM/ney1yqnK4E+ZEFS+4J7g0365wIl3MoFPrMP17F8Y7a5eBpskGQZCiOFeSnviRC9OAVGmMibHp85+aEeAx8aTz1shFS49FxmkMXEmt2+5EeG1Xzsj1kakeLElTPLzrkJ8+/puYj/e+5QPvcZR1MrmXeyECQQDDlLJflORUASXWB538bY7pFdi47NaWZVA7X0o/BQKfEVTKHGoUEp4AJ+pxYNci7Z8RUGVG+Lpl1LRbWo92hW1RAkEA442PPTjwFYdUL6d4JjvY6GomSyLBaUrCLVrDaWoaK5o0NzYgPtsNbkqV9oArO8qlwsASvltiFbD/SPldMnaXewJBAL69hxSWlfOjRu4scZScmJKTXtBDEqiMWCn/Ld62GS9e7K1L9txqp7MJOqimREppKgftu0fzDX6AagDqGh4B1HECQQCIhxGvIO9ja1vGb8t13SiKYc3x/Ltgyjrw7WkbYU6sZIv5qF72d4V6bAPH7ySBblfAHm/giIG0FAtHJF6XfXHrAkAmhCWRwdqNv1FngaKh3zbBVbUzfh4FlTEaaAt1XaTUxqOejOfH7iqnQj/fPCgioOKhCIU5+Xa7QIgneypjXYhF-----END RSA PRIVATE KEY-----
4. KeyGuy - pass - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQDBM6MjeuIheC31KFArFxvPh2MtsivgpaaHp8iBbzofAwNi7PyHjampHbUIRrGtYxxDIny7oNbXrqt6dJ5VwACAnoGwqY82qsLte4r6o/XU++L4K7ablzYfxTt/j+CXWbKqgGYchK0B8FfKGUYvKDVCoGIjkeQ51GTgIIsRMYdgqwIDAQABAoGAUiL32l+lv4DuWOmYm5kpc6MlYQn8aXdDQyzrq0t0NDb9u5LxEVgCpylAC5KyevpFy6zfxozsialysY7euan1C/t3/O9tv1h4q8ChZr1et0C4fsvA1bwllZIV7JyMBUrxoZuGH9E7/HT2kttok6avrNs0Vw4XJ8SnafBKKib6VfECQQDLKsd+L3luDjXIoeWORmIV9NyqgNCz8AFnEoV79GiFdGAbaSp2NU5eZbvHCHbGHHrod7aYW/grPFNxdhpMf0LHAkEA83FxRQCr7La8pgSiWr+YibhhL3BmMfLzPeCo58uaboWotZbC1dogrgPYiLaufDKC2rpQbrKPW4H7QblDQYiO/QJBAKbYDtQ1sIcM7GZDbf0VF9/oIn9zIfFjHAPFVhGheWR/WZ2pE9HXnPAwo7Cj5sZzBQx7o1wjyv3WoMAAuUAxEmkCQEUM72DwINPivT2l4Ns2rzCZIM/Q5NvUGpR5jc85nBMvTDw9iAQae9x/8MJOds15kk4yPLA5a5o8EyWARAhpkI0CQBeJxKmGL0KVozFEiX2XfqoHsRuNmxTMhKzLilRyZgY0bX3qN8omI0y3pFPYrkIpS9l0yfUVT5tzFU9hPtIiISY=-----END RSA PRIVATE KEY-----
