from flask import Flask, make_response


app = Flask(__name__)

@app.route("/api/v2/test_response")
def users():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Test worked!',
        200,
        headers=headers
    )
@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(
                    name=name,
                    email=email,
                    password=generate_password_hash(
                        password,
                        method='sha256'
                    ),
                    website=website
                )
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template(
        '/signup.html',
        title='Create an Account | Flask-Login Tutorial.',
        form=SignupForm(),
        template='signup-page',
        body="Sign up for a user account."
    )

@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
def users():
    @app.route('/user/<username>')
    def profile(username):

    # ... Logic goes here

    @app.route('/<int:year>/<int:month>/<title>')
    def article(year, month, title):

        @app.errorhandler(404)
        def not_found():
            """Page not found."""
            return make_response(
                render_template("404.html"),
                404
            )

        @app.errorhandler(400)
        def bad_request():
            """Bad request."""
            return make_response(
                render_template("400.html"),
                400
            )

        @app.errorhandler(500)
        def server_error():
            """Internal server error."""
            return make_response(
                render_template("500.html"),
                500
            )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)