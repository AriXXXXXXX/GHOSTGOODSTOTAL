import time
from resell_sniper_live import run_resell_sniper
from flask import Flask

app = Flask(__name__)

@app.route("/")
def keep_alive():
    return "GHOST GOODS: GLITCH ALERT >40%"

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_resell_sniper).start()
    app.run(host="0.0.0.0", port=8080)
