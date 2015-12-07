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
5. Search -> Fix the shit out of it (Can search, but VERY basic)
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
1. admin - admin - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQDBM6MjeuIheC31KFArFxvPh2MtsivgpaaHp8iBbzofAwNi7PyHjampHbUIRrGtYxxDIny7oNbXrqt6dJ5VwACAnoGwqY82qsLte4r6o/XU++L4K7ablzYfxTt/j+CXWbKqgGYchK0B8FfKGUYvKDVCoGIjkeQ51GTgIIsRMYdgqwIDAQABAoGAUiL32l+lv4DuWOmYm5kpc6MlYQn8aXdDQyzrq0t0NDb9u5LxEVgCpylAC5KyevpFy6zfxozsialysY7euan1C/t3/O9tv1h4q8ChZr1et0C4fsvA1bwllZIV7JyMBUrxoZuGH9E7/HT2kttok6avrNs0Vw4XJ8SnafBKKib6VfECQQDLKsd+L3luDjXIoeWORmIV9NyqgNCz8AFnEoV79GiFdGAbaSp2NU5eZbvHCHbGHHrod7aYW/grPFNxdhpMf0LHAkEA83FxRQCr7La8pgSiWr+YibhhL3BmMfLzPeCo58uaboWotZbC1dogrgPYiLaufDKC2rpQbrKPW4H7QblDQYiO/QJBAKbYDtQ1sIcM7GZDbf0VF9/oIn9zIfFjHAPFVhGheWR/WZ2pE9HXnPAwo7Cj5sZzBQx7o1wjyv3WoMAAuUAxEmkCQEUM72DwINPivT2l4Ns2rzCZIM/Q5NvUGpR5jc85nBMvTDw9iAQae9x/8MJOds15kk4yPLA5a5o8EyWARAhpkI0CQBeJxKmGL0KVozFEiX2XfqoHsRuNmxTMhKzLilRyZgY0bX3qN8omI0y3pFPYrkIpS9l0yfUVT5tzFU9hPtIiISY=-----END RSA PRIVATE KEY-----
2. Reid - pass - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQDYnkLVmbL3zmBb1d3muzzCbG342q4+CFjbmFM0ncvQBrGcjEk9lP6VCJZr1Rk32gZIePhAG26GYclRqOKNXwiAbQNFSLbJO25uRp5q15ATHO2Ot3uksY+NjHTP37DE+VNcPlDudGD2dUmIJbYK1VfwqPK4tzvlti+rDa8rnkoCcQIDAQABAoGAL7OqRB90qd1omtCd7RGOb8Iw9XwyorZz2ufQauXU3BqdQjwiZM1KwscBWP20b/gzKgJ5qKRh0nX2P2VRfpBO7pFbDG/uvu+FZM90pABya/oLyC26y6RCVzNugQ8J70jgXyDSyzoulSCSF4O9ISPUc1OkYMqg3pvB6HNLWT+sW4ECQQDprjRdt9SFKhz/MoISV6zSIQtoZdUD1LfCHc7gcNwG8Lm+RupD14imZsphXY0DHbicBb4d77HCqqLtH4UxrKojAkEA7U7cgF4Nt+SYbiLoZXYM9BkaabX/8ZjbpekWnEmW3/GI74s4v7BS3GF2bSHpp0W6dhV8Ub9EeOcoGxntv/TYWwJACAegbQgAGYNU87/8kDzLB31zMucs5rDMj7MOhM/b/7EN8Ofm7OXfIDiwA6B/U/gVe+cGnWi7JwFOD+/hV8+jGQJBANTWZSfws0cajKhDQMI3RdjsZucm5/4tBdthGflkeyAxhoqqCGTMZRTpiQjKYMC45kqgbJb5ABWb5TmhYL5IgH8CQQDf2m2yJXEB2D63LEvBWMRY0mwg5YS//eFcQybact1cDR6M1JA9g7Bt9N/fgEOBhL+Y+AFew09bzSKcaEMgV68o-----END RSA PRIVATE KEY-----
3. User1 - pass - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQCr6OTyD1eEHIq1Xt7w6bq8ZxFUThD7qiJBDW3ExpAUn4ii+zQ81tT47SurX8xCDzjkJJUUzsKNbhci9+B+MPRAXm0mLl7z7f2zfdr4Q0SU/D5ut7B589yymxcw2SvOFu0D9RD25JyGtMxuowSz+zAWYOIil1qUaDoO7eHgfIdvtwIDAQABAoGAfmTQl+yRwu+dSHbFYcnnYwhApIR1ViOj5cJy13/KhW86beJWaPjnQ1JVjj30FwnMIWmINvFB9+xelHY9l2p02f5UjQBGDO02ZUPbtiK8PXJY9fRkAdOTxxkXfVUiDZftaId0kD9kaetDRN3jpcpm2jsSI4ZrnShZASy41dCuvXkCQQDQBGeXCcPp2VwvleVRLi92igvHMt6HlKxEbwMjhD2wcNAia/0+q/zeYK677oXj2ibiKvI1jl7l3ACBl7wXZAvdAkEA05BQGcCjlzXzW+MFG81SlC4Ux7WZIUmDmxFGdXki7zC1qhn+EDxYjqdhZDT9sjJc0sdpSlXbVDrNgbSoIp5KowJADj+O/Oh9U+JAjz3cNEBOnfb8sYtJdM35MsLL2z3un8xKZWEyOn27V1wV++dtolrJ+QnqB0MWOvZjznyfNJb0vQJBAIExroibaAsOCifBsbvxnY0ZutzeG74FG5YVbZaNO/UfJMDUkJ6vi1DKDCJabdZlBOQ+nCCl34NHSXn8rXQ+f8sCQQDBqiAU00SSJ2TaS6UbrNVt9SNBMQRBm+E1139uYsYYhiAt5ThNUgMI4Ke7cgy77pRlfo9SGli2MtwEngCfVzKY-----END RSA PRIVATE KEY-----
4. KeyGuy - pass - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQC5jU/v/FRiY8PEGhGC8S8ur9CS+dhdW2uOU6xkrWfCarrDDs29C2YMZ5PAacUZ85gkYCthuPNBrf87tmO3Kz7jM2MNWES679DzvYGJrgNtHFgTCNrb4ngMHOMrnnBfanJvuFskYV79Tl+STINUzPTub08nPDpHUVf12d6LqNXVdQIDAQABAoGBAJlX+JUbUl2Rl0rsREaTreuGbvfYNQBKOiQAcHsvd42LiNcE1/CAiBB+VPPyNWrSDo0ZUSDMqXRBKKqfe973hVrzlgQmK/ba895YNayH0v49lmHbPj5jjImw0lnuaEdDJ9D9OLvzFLToe0/2Fq3TioM2p2WP2wTwoCcKtN2urbJtAkEAy2Cjjgf5+luWBOQaQ9AmEo/GOzQmUXFxBrBD5Vk7XWfxxgfoSJMmOAUVi6eyA05g/eJwqG/BKAJ8SmUCJ6WXmwJBAOmP8cxkYvXaIdHpc01yFIWTO1l+TFLtbQJ4OP6AD07whekqjAVIE1FvfsPXmFJlScG1aHQ+IlYZeydsOZy9AC8CQGDL5gw7j6aw4H4DctzDvNsowth6waIRtBHS4v3NsouKZXAzY0LnhlEzWkXV0svwCgnMNIJ2biB0zmM6IARus/ECQQDobOiRH+0i/5ncTNcDYN1vN9895eOKOt/aL014ZnPVeKGqMT76Gomu5qdduPTKOiW18RMrapG84MqfpqGGisbdAkBwQEP1KVBIWm3LblCd8MelE6+ueIy2GAPFhCSPw5Mk5PzR7gXdH0n3jHV1VLtf6lT1CBiJ8AvN6NpcOtIZJ27a-----END RSA PRIVATE KEY-----
