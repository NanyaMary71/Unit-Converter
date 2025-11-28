from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------- LENGTH CONVERSION --------------------
def convert_length(value, from_unit, to_unit):
    length_units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344
    }

    meters = value * length_units[from_unit]
    result = meters / length_units[to_unit]
    return result


# -------------------- WEIGHT CONVERSION --------------------
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "oz": 28.3495,
        "lb": 453.592
    }

    grams = value * weight_units[from_unit]
    result = grams / weight_units[to_unit]
    return result


# -------------------- TEMPERATURE CONVERSION --------------------
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from_unit → Celsius
    if from_unit == "C":
        c = value
    elif from_unit == "F":
        c = (value - 32) * 5/9
    elif from_unit == "K":
        c = value - 273.15

    # Convert Celsius → to_unit
    if to_unit == "C":
        return c
    elif to_unit == "F":
        return (c * 9/5) + 32
    elif to_unit == "K":
        return c + 273.15


# -------------------- FLASK ROUTES --------------------
@app.route("/")
def home():
    return render_template("length.html")


@app.route("/length", methods=["GET", "POST"])
def length():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_length(value, from_unit, to_unit)

    return render_template("length.html", result=result)


@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_weight(value, from_unit, to_unit)

    return render_template("weight.html", result=result)


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_temperature(value, from_unit, to_unit)

    return render_template("temperature.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
