# This is the dependencies file for PellioRPI. It is meant to help us manage dependencies involved with the project. 

## Installation 
In order to run and test Pellio, the user will need to have some dependencies installed. 

..* Python 3
..* Django
..* MySQL 

## Known Issues 
### Making the python3 manage.py runserver work on MacOS
Since the project is using python 3 and MacOS usually defaults python to be 2.7, there can be issues when trying to setup the files. If you find that you have all the files installed but can't run the server using runserver, try running the following commands: 
`sudo ln -s /usr/local/Cellar/openssl/1.x.x/lib/libssl.1.x.x.dylib /usr/local/lib`
`sudo ln -s /usr/local/Cellar/openssl/1.x.x/lib/libssl.1.x.x.a /usr/local/lib`
`sudo ln -s /usr/local/Cellar/openssl/1.x.x/lib/libcrypto.1.x.x.dylib /usr/local/lib`
`sudo ln -s /usr/local/Cellar/openssl/1.x.x/lib/libcrypto.1.x.x.a /usr/local/lib`

This will allow your python to look in the right places for dependencies. 
