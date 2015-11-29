wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz
tar xvfJ Python-2.7.10.tar.xz
cd Python-2.7.10
./configure --prefix=~/python --enable-unicode=ucs4
make
make install
