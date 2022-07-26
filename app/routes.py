from app import app
from flask import render_template

@app.route('/')
def index():
    home = [{'img': 'https://openai.com/content/images/2020/04/2x-no-mark-1.jpg'}]
    return render_template('index.html', items=home)

@app.route('/things')
def things():
    staff = [
        {'name': 'Childish Gambino' ,'img':'https://i.scdn.co/image/ab6761610000e5eb3ef779aa0d271adb2b6a3ded', 'genre': 'hip hop, funk, R&B'},
        {'name': 'Yellowcard','img':'https://i.scdn.co/image/014d29b70a865b02144687255cfeb7dbe65d08f8', 'genre': 'pop punk, alt rock'},
        {'name': 'Jonas Brothers','img':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/mh-jb-042919-05-1162-v2-1558460995.png?crop=0.6665xw:1xh;center,top&resize=480:*', 'genre': 'pop rock, rock, pop punk'},
        {'name': 'Adele','img':'https://i.dailymail.co.uk/1s/2022/07/17/00/60350603-11021149-image-a-127_1658012810801.jpg', 'genre': 'pop, soul'}, 
        {'name': 'Billie Eilish','img':'https://yt3.ggpht.com/ytc/AKedOLQFmN0dv74DvLrRAT6g5KEKfsm4I-fuPnz0eT9Ksw=s900-c-k-c0x00ffffff-no-rj', 'genre': 'pop, electropop'}]
    return render_template('things.html', names=staff)