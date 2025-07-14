from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/trigger-test", methods=["GET", "POST"])
def github_webhook():
    try:
        print("🔔 Webhook triggered!")

        return jsonify({"status": "received"}), 200
    except Exception as e:
        print(f"[ERROR] Failed to handle webhook: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0")
