from flask import Flask, render_template

app = Flask(__name__)

feature_flags = {
    "new_page_flag": True
}

if feature_flags.get("new_page_flag"):
    @app.route('/new_page')
    def newpage():
        # Simulate backend data processing
        items = ["Item 1", "Item 2", "Item 3"]
        return render_template('new_page.html', items=items)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)