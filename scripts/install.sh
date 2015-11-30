tmpd=$(mktemp -d)
cd $tmpd
wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz
tar xvfJ Python-2.7.10.tar.xz
cd Python-2.7.10
home=$(readlink -e ~)
./configure --prefix=$home/python2.7.10 --enable-unicode=ucs4
make
make install

mkdir $home/virtualenvs
virtualenv -p $home/python2.7.10/bin/python2.7 $home/virtualenvs/python2.7
wget http://curl.haxx.se/ca/cacert.pem
echo "alias pip=\"$home/virtualenvs/python2.7/bin/pip --cert $home/cacert.pem\"" >> $home/.bashrc
echo "alias python=\"$home/virtualenvs/python2.7/bin/python2.7\"" >> $home/.bashrc
echo "alias ipython=\"$home/virtualenvs/python2.7/bin/ipython\"" >> $home/.bashrc

source $home/.bashrc

$home/update.sh

