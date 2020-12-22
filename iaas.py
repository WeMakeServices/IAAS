
from flask import Flask, request
from flask_limiter import Limiter
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers.get("X-Real-Ip"),
)


@app.route("/do-i-the-invoker-of-iaas-have-internet-availability-right-now-at-this-current-point-in-time-assuming-iaas-is-currently-properly-functional-and-live-for-any-get-request", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("1 per day")
def iaas_affirmation():
    return "YES", 200

@app.route("/do-i-the-invoker-of-iaas-not-have-internet-availability-right-now-at-this-current-point-in-time-assuming-iaas-is-currently-properly-functional-and-live-for-any-get-request", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("1 per day")
def iaas_negation():
    return "NO", 200


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")