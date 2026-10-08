from flask import Flask, render_template, request
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

# Language codes
LANGUAGES = {
    "English": "en-GB",
    "Telugu": "te-IN",
    "Hindi": "hi-IN"
}


@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    source_text = ""
    source_language = "English"
    target_language = "Telugu"
    error = ""

    if request.method == "POST":
        source_text = request.form.get("source_text", "").strip()
        source_language = request.form.get("source_language", "English")
        target_language = request.form.get("target_language", "Telugu")

        if not source_text:
            error = "Please enter some text to translate."

        elif source_language == target_language:
            translated_text = source_text

        else:
            try:
                source_code = LANGUAGES[source_language]
                target_code = LANGUAGES[target_language]

                translator = MyMemoryTranslator(
                    source=source_code,
                    target=target_code
                )

                translated_text = translator.translate(source_text)

            except Exception as e:
                error = f"Translation failed: {e}"

    return render_template(
        "index.html",
        translated_text=translated_text,
        source_text=source_text,
        source_language=source_language,
        target_language=target_language,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)