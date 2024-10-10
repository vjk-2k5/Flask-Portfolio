from flask import Flask, render_template, request

app = Flask(__name__)

# Sample user data
users = [
    {'name': 'vijay', 'email': 'alice@example.com', 'age': 18},
    {'name': 'Bobi', 'email': 'bob@example.com', 'age': 25},
    {'name': 'pradeep', 'email': 'charlie@example.com', 'age': 19},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', users=users)

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            result = "Invalid operation"
        
        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

#commentbysanthosh