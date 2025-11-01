from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    items = [
        {"name": "Laptop", "price": "$799", "image": "https://cdn-icons-png.flaticon.com/512/1055/1055687.png"},
        {"name": "Smartphone", "price": "$599", "image": "https://cdn-icons-png.flaticon.com/512/2331/2331887.png"},
        {"name": "Headphones", "price": "$129", "image": "https://cdn-icons-png.flaticon.com/512/107/107282.png"},
        {"name": "Smartwatch", "price": "$199", "image": "https://cdn-icons-png.flaticon.com/512/679/679720.png"},
        {"name": "Gaming Console", "price": "$499", "image": "https://cdn-icons-png.flaticon.com/512/3097/3097144.png"},
        {"name": "Camera", "price": "$699", "image": "https://cdn-icons-png.flaticon.com/512/685/685655.png"}
    ]
    return render_template('products.html', items=items)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f"Thank you, {name}. We received your message!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
