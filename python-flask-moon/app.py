from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Create a dictionary of posts
posts = {
    # Key : Value
    0 : {
        'post_id' : 0,
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
        return render_template('404.jinja2', message=f"A post with id {post_id} was not found")
    return render_template('post.jinja2', post=post) 

@app.route('/post/form')
def form():
    return render_template('create.jinja2')

# http://127.0.0.1:5000/post/form?title=asd&content=asd
@app.route('/post/create')
def create():
    title = request.args.get('title') # request.args['title']
    content = request.args.get('content')
    post_id = len(posts)
    posts[post_id] = {'id' : post_id, 'title' : title, 'content' : content}
    
    return redirect(url_for('post', post_id=post_id)) # url_for('post') -> call function name 'post'
    
if __name__ == '__main__':
    app.run(debug=True)