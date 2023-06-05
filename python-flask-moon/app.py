from flask import Flask, render_template

app = Flask(__name__)

# Create a dictionary of posts
posts = {
    # Key : Value
    0 : {
        'title' : 'Hello World',
        'content' : 'This is my first post on this site'
    }
}

@app.route('/')
def home():
    return 'Hello World!'

# @app.route('/post/<int:post_id>') # /post/0
# def post(post_id): # post_id = 0
#     # return posts.get(post_id) # posts[0]
#     post = posts.get(post_id)
#     # return f"Post : {post['title']} , content :\n\n{post['content']}"
#     return render_template('post.html', post=posts.get(post_id)) # templates/post.html -> post

@app.route('/post/<int:post_id>') 
def post(post_id): 
    post = posts.get(post_id)
    if not post: # post will be None if not found; not None = True
        return render_template('404.html', message=f"A post with id {post_id} was not found")
    return render_template('post.html', post=post) 

    
if __name__ == '__main__':
    app.run(debug=True)