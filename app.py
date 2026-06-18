from flask import Flask, render_template
from routes.bloom_routes import bloom_bp

app = Flask(__name__)

# Register Bloom routes
app.register_blueprint(bloom_bp)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )