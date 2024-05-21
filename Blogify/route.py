from flask import Flask, render_template, flash, redirect, url_for
from Blogify import app
from datetime import datetime


posts = [
    {
        'author': 'Brian',
        'title': 'Blog 1',
        'content': 'First post',
        'date_posted': 'April 20,2020'
    },
    {
        'author': 'Brandon',
        'title': 'Blog 2',
        'content': 'Second post',
        'date_posted': 'April 20,2021'
    },
    {
        'author': 'Brian',
        'title': 'Blog 1',
        'content': 'First post',
        'date_posted': 'April 20,2020'
    },
    {
        'author': 'Brandon',
        'title': 'Blog 2',
        'content': 'Second post',
        'date_posted': 'April 20,2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/post")
def blogPost():
    return render_template('posts.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register" ,methods=['GET', 'POST'] )
def register():
        return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'] )
def login():
    return render_template('login.html', title='Login')
