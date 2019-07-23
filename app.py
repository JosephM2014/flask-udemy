from flask import Flask, render_template

app=Flask(__name__)

data = [
    {
        "title":"Python",
        "bio": "Python is a dynamic interpreted language."
    },
    {
        "title":"Java",
        "bio":"Java is an object oriented language"
    },
    {
        "title":"C#",
        "bio":"C# is an object oriented language by Microsoft"
    }

]

@app.route('/')
def hello_world():
    # return "Hello world!"
    # ================================
    title="HipsterCode"
    programming_languages = [
        "Python",
        "Java",
        "JavaScript",
        "Perl"
    ]
    return render_template('index.html', title=title, programming_languages=programming_languages)

# dynamic pages via urls
# http://127.0.0.1:5000/lang/books
# http://127.0.0.1:5000/lang/java
@app.route('/lang/<name>')
def lang(name):
    title=name 
    lang=next(item for item in data if item["title"].lower()==name.lower())
    return render_template('lang.html', title=title, lang=lang)


@app.route('/about')
def about():
    title="About Us"
    return render_template('about.html', title=title)

@app.route('/contact')
def contact():
    title="Contact Us"
    return render_template('contact.html', title=title)

@app.route('/terms')
def terms():
    title="Terms of Use"
    return render_template('terms.html', title=title)


@app.route('/privacy')
def privacy():
    title="Privacy Policy"
    return render_template('privacy.html', title=title)