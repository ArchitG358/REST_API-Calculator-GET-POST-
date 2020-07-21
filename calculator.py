from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    try:
        value1 = request.args.get('value1')
        value2 = request.args.get('value2')
        operation = str(request.args.get('operation'))
        value1 = int(value1)
        value2 = int(value2)

        if operation == '-':
            return jsonify({'Output': value1 - value2}), 200
        elif operation == '*':
            return jsonify({'Output': value1 * value2}), 200
        elif operation == ' ':
            return jsonify({'Output': value1 + value2}), 200
        else:
            return "Incorrect Input", 200
    except:
        try:
            value1 = request.json['value1']
            value2 = request.json['value2']
            operation = str(request.json['operation'])
            value1 = int(value1)
            value2 = int(value2)

            if operation == '+':
                return jsonify({'Output': value1 + value2}), 200
            elif operation == '-':
                return jsonify({'Output': value1 - value2}), 200
            elif operation == '*':
                return jsonify({'Output': value1 * value2}), 200
            else:
                return "Incorrect Input", 200

        except:
            abort(400)


if __name__ == '__main__':
    app.run(debug=True)
