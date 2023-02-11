echo "Build Start"
python3.9 -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo "Build Complete"