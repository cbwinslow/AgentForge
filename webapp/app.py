from flask import Flask, request, render_template_string
from agentforge.orchestrator import Orchestrator, SpecializedAgent

app = Flask(__name__)


def create_app() -> Flask:
    """Factory to create the Flask app with a default orchestrator."""
    app.config["orchestrator"] = Orchestrator({"default": SpecializedAgent("general")})
    return app


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        instructions = request.form.get("instructions", "")
        _files = request.files.getlist("documents")
        orchestrator = app.config.get("orchestrator")
        results = orchestrator.execute(instructions) if orchestrator else {}
        return {"results": results}

    return render_template_string(
        """
        <h1>AgentForge Chatbot</h1>
        <form method='post' enctype='multipart/form-data'>
            <textarea name='instructions'></textarea><br>
            <input type='file' name='documents' multiple><br>
            <input type='submit'>
        </form>
        """
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
