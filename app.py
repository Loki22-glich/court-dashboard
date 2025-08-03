from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']
    
    # For now, just display the input back — replace with scraping logic later
    return f"You entered: {case_type} / {case_number} / {filing_year}"

if __name__ == '__main__':
    app.run(debug=True)
