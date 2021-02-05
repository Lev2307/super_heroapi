from flask import Flask, render_template, request
from superhero_api import SuperHeroAPI

app = Flask(__name__)
s = SuperHeroAPI()

@app.route('/', methods=['POST', 'GET'])
def index():
    character_name = request.form.get("name")
    try:
        img_url = s.get_hero_image_url(f'{character_name}')
        return f'''
        <img src="{img_url}" class="image">
        <form action="" method="post">
            <input type="text" name="name" placeholder="Enter your name: ">
            <input type="submit" value="Submit">
        </form>
        <h1> САЛАМАЛЕЙКУМ РУБЛЬ БУДЕТ</h1>'''
    except:
        pass
    return render_template('index.html')
