from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def even_odd():

    numbers = list(range(1, 21))

    even = []
    odd = []

    for n in numbers:

        if n % 2 == 0:
            even.append(n)

        else:
            odd.append(n)

    return render_template(
        "index.html",
        even=even,
        odd=odd
    )


if __name__ == "__main__":
    app.run(debug=True)
