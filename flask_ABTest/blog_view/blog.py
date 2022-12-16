from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from blog_control.user_mgmt import User


blog_abtest = Blueprint("blog", __name__)

@blog_abtest.route("/test")
def test():
    return make_response(jsonify(success = True), 200)

@blog_abtest.route("/test_blog")
def test_blog():
    return render_template("blog_A.html")    

@blog_abtest.route("/set_email", methods = ["GET", "POST"])
def set_email():
    
    if request.method == "GET":
        print(request.args.get("user_email"), request.args.get("blog_id"))
        print("set_email", request.headers)
        user_email = request.args.get("user_email")
        blog_id = request.args.get("blog_id")
        return redirect("/blog/test_blog")
    elif request.method == "POST":
        # request.get_json()을 쓰려면 content type이 application/json인 경우만 가능
        # print(request.get_json())
        print(request.form)
        return redirect("/blog/test_blog")



    # User.create(user_email, blog_id)
    
      # /blog/test_blog로 다른경로로 가게 리다이렉트 할수있음
    # return make_response(jsonify(success = True), 200)



