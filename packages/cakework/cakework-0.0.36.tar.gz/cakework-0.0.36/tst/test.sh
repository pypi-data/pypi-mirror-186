#source ../env/bin/activate
#pip3 install ../
python3 main.py &
python3 test.py
pkill -f main.py
