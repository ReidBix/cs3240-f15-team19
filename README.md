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

#UserList (username - password - privatekey) MUST CREATE NEW SERVER FOR NEW KEYS
1. admin - admin - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQDHjtSYUhTanO3BubhJ6Dm6zgB9I5+tnRDzzdP9sToxLtNKCOzj9seDIFgQBTfyKT4ZhRB8txmS1P8dAalMBaKER57oNlgz0jydsbbALNNR32nRJk0CVRdpVaStO5SuzODPhl+htoEeuBqop8uqawnfqXEq5wFonP7y/VUUqiKMTwIDAQABAoGAQlscFgo1JPxJksFOpkSx7YvSXcoaroArwuYON61WzEPlvhh5rNPCQ7fdkHYrxDoyjAnTEaVQu6JXsi17PewhvYPqvzpWJAuM+dRd/lfvWEo6tKTid5GMVkg6/p5G3e/v8Gtvdpg9XrEG9+IY7IxuFo7Wu0odlnjulpA67DmoPwECQQDTQawXRh2OKgEX9TujMLlVr8YUmrMxzK7Ywkc1MplhAHplhVP/zuO6wUXVwli3DjK9al7m2Asx2PtAHDFnWYGtAkEA8dLcM977LhHL81IGuTdEyKhjaiRA/mf1Q+r21RLPO5iHLgLg+6FrsJhvfsLZuO7b8qMPR6ts8UqgKghvnMPdawJBALj47JyoSOKchr6ae/BkjjKnqHGMDtDQ3ltuqHi86C1WBNV1S1pVpXJ1HhePhqwpo2XUiGnpysuHqF63EM7kQTUCQQCyqfuPR1uE+hkZOK1HApKLPf3VWdu7GsuW1m5vlmoNue+GCxJ2VxjdbIJTwVpiy/ctGVQcu4bN7zjOVVVBGWTpAkB5S6/Xyy9nZuvQ5i+ZBYd+q2iKlu48MCK3BJ5qJ3s84CgibblMcL7GEv3SNZFldPTRkiKNInphpP2WC3RCuyTG-----END RSA PRIVATE KEY-----
2. Reid - pass - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQCqsfE+DSyYfWiSNkddyFqdP48pHsCT6IeoYOSs5A75rbdBVn3N4ekjgEYEV4Fuvb8SSISSCBLydrNxccUaGYaUjL8o/O9mHXjLIlelgp9yL8Nsnwk0Bs1oGlqZ++KBe/ab69VWFczfA+sbeyemTI3BFw1oG71eq2twUy7reuYLdQIDAQABAoGAUjHZXu3tGYjZ//4PI4PEzo+6mixqw05ndJcjxnUTGPujkNzbO3abUzMDhDe25eKMzXsKC1/D7+lkwy3roYPFH51L1Wx3dLXKWCKD2s/nkI7UM+S66eZl3KdSK0WxzO9cmSHV2QvjEgxvXVIhNzsYL9WVuKL3v6+1H519/n8q+gECQQDCyTD+rbCuqG9peg3g2t63V9gfrHgQj88mFoZ3XFP+3QmIQdH+GF2K3OfWkLN0j8Eom/alO2fIwPHFW/1mdO21AkEA4FacHRuWug19xQBVZBCIlLFSU/0aszA4ZR0y0Ke1MZzrCK5PoEMqLM6Wyt/IpG/N4caV4WOOHVeLybGrspk+wQJBAJGaTQqDEWhtteJ1fzxOv17zxjVe+dz/csw42EkO9ia0WbTF5s/2rK3plU+5mLuP3caaVxOKRXk2aUOrEM9upmUCQHueHh5IApF5N7Gjkmo2VhyhbX1Mfjb5PkoxgbvKfiTdlAHPk577A7V3DU6za6t41FkyBYsSQdBXWncEyVj76sECQHmJqW3HyERfztvEvP7OgWwYTYVxJ3xNFrlG4EkcJtOXtFKewEycOHuD3bXvjvQDlyyqRobNiSRGapSZcszJ9hM=-----END RSA PRIVATE KEY-----
3. User1 - pass - -----BEGIN RSA PRIVATE KEY-----MIICWwIBAAKBgQCSBuGFl8fkdsjjUB5eIVD7b44w4u2olu7jecZL/lsCZrQY55qhLN4P+CD2K/Egz2ts3VwvihyKarYp2WchdgIJAdC9kkqLgdSYGC5uMygan5Xsi2Ly/5zUQ+t6PFEGvYJIoBgKo49FjLjPlnfDYEWV5dPYvJRRvLcassXtDJQZoQIDAQABAoGADBMLlMtPGQIFbF5UlH32v0OjI0GwWw9X43FPRztZ9SHe5GxKKeeW2QUwXIqXnpnoDRFkrP2jjIJ0W5OBZo/mbQ5BAsq6mGF+PzSeCFxMoyZU68dptti7gnOhRLDWHDq11VUuwe/DcdM9kkc/htzZ+2oZN6AeNgem/eGWdXramG0CQQC9RiBZTX1kIklNhgYnKFSU/w2JzHKBCMLv25/WAv398H+RXEVPYmQy12Eazko/xGnZKVTUTYaR2xzmabv/3HY/AkEAxYG7C0m475tQyDy+q+kftOP2qIPUU5Jz6gTIlbJ3QQHi/gF+QOIFvd8XnXLbawLiQUNOahphQlZSJMeRT/w4HwJAAyRm5RSkQEVRcjgHYh8JSG/ziZYbUIkUs2ayAJuMG+siMweVHvxDLZTlx8wk72oTV8eX4O5ojYNVt32J4XWHgQJAWR3/SsmaA6teGOun0SPgZZuS2ViafpcPbGF6LGmZe6ChTqFX2Wji1FiMbEO+E5v6gR4gjKmYhvkyGVxfCesxWwJAM8evyKvuELEPL4q/PneHaXgKQM1J4jhZd0lIDFruNHS/JRXLDukASsV5l7SKECBgDeiD6o/KXLQUK8tG0iAUQQ==-----END RSA PRIVATE KEY-----
4. User2 - pass - -----BEGIN RSA PRIVATE KEY-----MIICXgIBAAKBgQCV14/QmtU0XRLL4PR2QMhdjwbX1BerGp7MGcSw49i2GrR4phIiqSsD910K9ZHiScXBOqBnPF6Et714RAG640LAlFqQ6qZWKmKH7qRhkmtu0oV4sTNDpWvCwymWTrywtHpnXmI+dCStxMw+rUZ1VcpZ/C2rkCON5PJi9g0MTiuJ2QIDAQABAoGAfYdb5N+BU1/Rmlk3k0WMVcy3Z+I3fdFMTSIdRC9s4ooWvKgrszvTXHxDRyYY8+DnuYwaysGpUTf4k6Mta9ptlU2TsGGPfcqk1AhAJeVG2fIBcM2Q6owi6XdNyYxn90x/wEdd+uEhALpajxDhPE6iuYiYnSs7CBMRU0mo8bzM4y0CQQC84Zj3de7G8qPVyi10FqsxV1MoH/pm5JUUi9RHbuN9rpAgBoWK8ju4kI59YenX5YLtQBMj9fBq2kfi+6BVatV3AkEAyxaX+ZsLXjihHuYtSRllkqnLeVqR6vzb+IGGij79R8Xt782ssHYGD6GHzQDbOcjhnjR5qbr/igZlGJQPte6vLwJBAJzszbrjB2PRGZ84nzTw1IBk7djLYK31wYpVdiN3FJhJ3MJOyMqc4FNB/rBbFf5iV7mnX3+kCH+uJMWHizkMTpcCQQCSH1WFwKqzRmeXReI7gEx29Dh0vlfTDdBvwzI8cgnnBGCodAHWjXTa9kwxknYp44GCRRtspiGK/ALtZkrPikb9AkEAjeuK4yv02kB51eYlHpLwRrjgonmPXQ+NEK9Oq1IgPNp77LGPoVEn5qb51rK0kzbFE+8mZyeywPcI212UpKmHjw==-----END RSA PRIVATE KEY-----
5. User3 - pass - -----BEGIN RSA PRIVATE KEY-----MIICXAIBAAKBgQCTDfH/icEcf8un3dg+k+ByiPMfIucz4st7HP9v+wdWxFTf+tO8Eirg7I081IryTEurfmMPTaypCXhFhiSnEQ7pDawg2ejiXd/2zSJ99m+V1gdijSjdHq+igYLXn1R3dQrEZsnuyiEhV07x/iNxxD1IdIoCqiMUwMoobdz0IoLEgQIDAQABAoGAOlQeuBhg47gBBM2m93NaZLPTk3cZs+fyhBvFahptF8p6S/lGwOOH5H2PrCA2GNOQdC6Ghkxt/wKFlTYXFblbaxWWWLYIJbdvpgRBnwqw/hkmL/Bh26r7Y/23bJ2QEysMO+vVVTegcmJ3YjRUSO9fnw3kb0yGfJO5wRAPi4hvnC0CQQDAEXLodEPlmfHHegMaCBnupDrCdJjfB/mWaCqb8sXDb9a1vmNaXPY2MiFs05KRqVt5kQnb/MLWttDfid5u+i+PAkEAxADH9T+ZgCsFi4Qv2uq2GDYM7jpi/GlwrNS2R8T+oCF7j9hGdhUKYCb2IYMb0M+Pr0ua3/8YHTQPLznPD7rC7wJAHc7XcYIRw4Fnx5iFALY/KA0u3VzxGLQJJTGXY0qDLLifrucUTkLdJz4Sd+xB8/8/phc/W3fX2TDYK8kez0ReuwJAd+Uma83ovu8SKELG5zn2A59kj4FltZNmGkLP8dz+CMQSim44w9ihDSooG13Q8Q1WjltINMcdYBfNRg0trSiIPwJBAIRdDogj3fTyHYuR9jfQAHmUdfWBfFGbxzGtqtxqwj6AHShSel0Qs/c8sgtFZz+lmJMQR17K3i3ScOzrLacilFk=-----END RSA PRIVATE KEY-----
6. User4 - pass - -----BEGIN RSA PRIVATE KEY-----MIICXQIBAAKBgQC1fnvpdrX08tdDRCMn186pdXbgMMXQC4+n7LK5h937M0D7vEKa5YYG+GfQr3b7bQZn/vwhEacYnHXU+tdVaEoJO6wKSmFuSANeB5DI6RAdxCgl2f+zWQ73+av7kUGkcnmOKC0uRfTbWbB1nzbblBPXBH/4X4B9yg35oRo/NvFRSQIDAQABAoGAR/EdOQvfUHs6LOXDcbWvq6huOKvcnX0Xsp62sahTq5FDfwW++RtmJzksHaKP7VXoJi0C0DDpJW5Pnt7XoHk4bwmDsKOq5C9VQILfP9cfJLWM6IS67fJFYKmgX/Hd4A0YVVua43aLlkTD3fH308GdMyai2RWfBnoDRbXUz1xakOkCQQDQA4KbofVCzh9xEoGM2xBdNDMle3mRmXXPB8O24elQtmx1u8kr2gMu5TB7iwqp20Pz6BziR7PpVcJclXayyPADAkEA31zTh3Pt/a9It5E7VYQla6rJoptCQwp/yqYEEzxz5OCcn2HGXxNyDSuKnXmUoXItIa5PBMJqW5uKw4SsSBDVwwJBALLTYbQUPvpIo6UciL0kEuRdnN7LUM7IBAyQm0Oc4Wye940bfC2zxerJ461B8k/mDXwg/rvVcqjVLjtTzvCSaCsCQEb7ffGO4vP6r1Y+3idIDohPxzJYus8JWCEzbxoZ3Q7AXqW78cmnKViMHMn8qEJCQZtxhIUTr68bGBcYY5OnXfcCQQCItGdUrBs0/a5AB+7unhVZIxZHheZ+9/67PEO6LdjP/xz+Hdam4I1lq53bLA6BGUyHvY0pONENf0LirnR7AHD5-----END RSA PRIVATE KEY-----
