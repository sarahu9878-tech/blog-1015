
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 儲存文章（暫時存在記憶體中）
posts = [
    {
        "id": 1,
        "title": "我的第一篇文章",
        "author": "小明",
        "content": "歡迎來到我的部落格！"
    }
]


# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 新增文章頁面
@app.route("/create", methods=["GET", "POST"])
def create_post():

    # 使用者按下發布文章時
    if request.method == "POST":

        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        content = request.form.get("content", "").strip()

        # 確認欄位都有填寫
        if not title or not author or not content:
            return "請填寫標題、作者和文章內容！", 400

        # 建立新文章
        new_post = {
            "id": max((post["id"] for post in posts), default=0) + 1,
            "title": title,
            "author": author,
            "content": content
        }

        posts.append(new_post)

        # 發布完成後回到首頁
        return redirect(url_for("index"))

    # 第一次進入頁面時，顯示表單
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
