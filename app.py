from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def github_webhook():
    try:
        payload = request.json
        print("🔔 Webhook triggered!")
        print(payload)  # Or use json.dumps(payload, indent=2) for pretty print

        return jsonify({"status": "received"}), 200
    except Exception as e:
        print(f"[ERROR] Failed to handle webhook: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
