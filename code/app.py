from flask import Flask, render_template, request, jsonify
import characterai

app = Flask(__name__)

# Initialize the characterai client with your character's API credentials
client = characterai.Client()

# Home route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chat messages and interact with Character.AI
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    
    # Set the character to interact with
    character = client.get_character('your_character_id_here')  # Replace with your Character.AI character's ID
    
    try:
        # Send user message and get AI's response
        response = character.chat(user_message)
        ai_response = response['text']
        return jsonify({'response': ai_response})
    except Exception as e:
        return jsonify({'response': 'Error: Could not connect to Character.AI'}), 500

if __name__ == '__main__':
    app.run(debug=True)
