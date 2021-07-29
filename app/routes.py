from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import ContactForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)