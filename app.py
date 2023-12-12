from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the db object from the pickle file
with open('model/db.pickle', 'rb') as db_pickle:
    db = pickle.load(db_pickle)

# Load the llm model from the pickle file
with open('model/llm.pickle', 'rb') as llm_pickle:
    llm = pickle.load(llm_pickle)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_explanation', methods=['POST'])
def get_explanation():
    query = request.form['query']
    
    # Perform similarity search
    docs = db.similarity_search(query)

    # Display the Explanation from the first result
    explanation = docs[0].page_content
    
    return render_template('result.html', query=query, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)
