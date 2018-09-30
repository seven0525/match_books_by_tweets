# !//usr/bin/env/python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, redirect, request
from os.path import join, dirname, abspath, exists

import analyze_books as analyze_books

#Flaskの起動
app = Flask(__name__)

@app.route("/")
def show_toppage():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def add_user():
    title = "分析結果"
    my_user_name = request.form['my_user_name']
    if not my_user_name:
        return redirect('/')
    result, result_img = analyze_books.main(my_user_name)
    return render_template('index.html', title=title, result=result, result_img=result_img, my_user_name=my_user_name)

# # if __name__ == "__main__":
# app.run(host="localhost")

if __name__ == "__main__":
    app.run(debug=True)
