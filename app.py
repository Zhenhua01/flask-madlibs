from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def show_page():
    """send prompts to questions.html"""
    return render_template("questions.html", prompt_list = silly_story.prompts)

@app.get("/results")
def show_results():
    """get inputs and show story with inputs"""

    story_text = silly_story.generate(request.args)

    return render_template("results.html", story = story_text)

    #use above since request.args return 'dictionary' object of all args in query
    """answer_list = {}
    for prompt in silly_story.prompts:
        prompt_input = request.args.get(prompt)
        answer_list[prompt] = answer_list.get(prompt,prompt_input) """
