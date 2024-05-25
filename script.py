from Blogify import app, db
from Blogify.model import User, Post


with app.app_context():
    db.create_all()
    
    users = User.query.all()
    for user in users:
        print(user)
    print("\n")
    
    posts = Post.query.all()
    for post in posts:
        print(post)
    print("\n")