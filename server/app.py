from flask import Flask, send_from_directory, request
import geoip2.database


app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/js/scripts.js")
def javascript():
    return send_from_directory(app.static_folder, "js/scripts.js")


@app.route("/css/styles.css")
def css():
    return send_from_directory(app.static_folder, "css/styles.css")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico")


@app.route("/post", methods=["POST"])
def post():
    body = request.get_json()
    print(body)
    print(body["email"])
    print(request.remote_addr)

    with geoip2.database.Reader("geolite/GeoLite2-City.mmdb") as reader:
        # response = reader.city(request.remote_addr)
        response = reader.city("84.162.166.27")
        print(response.city.name)

    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
