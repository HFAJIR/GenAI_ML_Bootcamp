from flask import Flask, jsonify, request
from blog import Blog


app = Flask(__name__)

@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    blog = Blog(title, content)
    conn = None  # Replace with actual database connection
    blog.save(conn)
    return jsonify(blog.to_dict()), 201
@app.route('/blogs', methods=['GET'])
def get_all_blogs():
    conn = None  # Replace with actual database connection
    blogs = Blog.get_all(conn)
    blogs_list = [blog.to_dict() for blog in blogs]
    return jsonify(blogs_list), 200
@app.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    data = request.json
    title = data.get('title')
    content = data.get('content')
    conn = None  # Replace with actual database connection
    blog = Blog.get_by_id(conn, blog_id)
    if blog:
        blog.title = title
        blog.content = content
        blog.save(conn)
        return jsonify(blog.to_dict()), 200
    else:
        return jsonify({"error": "Blog not found"}), 404
@app.route('/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    conn = None  # Replace with actual database connection
    blog = Blog.get_by_id(conn, blog_id)
    if blog:
        blog.delete(conn)
        return jsonify({"message": "Blog deleted"}), 200
    else:
        return jsonify({"error": "Blog not found"}), 404
    
@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    conn = None  # Replace with actual database connection
    blog = Blog.get_by_id(conn, blog_id)
    if blog:
        return jsonify(blog.to_dict()), 200
    else:
        return jsonify({"error": "Blog not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)
  