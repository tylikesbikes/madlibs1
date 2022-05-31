from flask import Flask, render_template, request
app = Flask(__name__)

"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title
        

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

storyList = [
    Story(["number","place", "noun", "verb", "adjective", "plural_noun"],
        """{number} upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
       'Long Ago'),
    Story(['name','verb'],
        """Hi, my name is {name}.  I like to {verb}""",
        'Introduction'),
    Story(['animal','name','food','verb'],
        """I have a {animal} named {name}.  {name} likes to eat {food} and {verb}""",
        'Pets')
]

@app.route('/')
def do_choose_story():
    return render_template('/pick_story.html', storyList = storyList)

@app.route('/fill_story')
def do_main():
    global chosen_story
    for each in storyList:
        if each.title==request.args['story_title']:
            chosen_story = each
    return render_template('/start.html', story = chosen_story)

@app.route('/show_story')
def show_story():
    return render_template('/show_story.html', story = chosen_story, complete_story=chosen_story.generate(request.args))