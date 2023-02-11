echo "Build Start"
apt install sudo
sudo apt install libpq-dev python3-dev
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "Build Complete"