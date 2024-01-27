from flask import Flask, request, jsonify
from threading import Thread
import openai
import os
import django

# Assuming Django models are used to store business idea metadata
from CashFlow.models import BusinessIdeas

app = Flask(__name__)

# Initialize OpenAI API key
openai.api_key = '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'

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# Import Django models
from CashFlow.models import BusinessIdeas


@app.route('/generate_business_idea', methods=['POST'])
def generate_business_idea():
    data = request.json

    # Assuming the request includes metadata for the business idea
    metadata = data.get('metadata')  # To fix once data is implemented

    # Assuming metadata includes information needed to generate a business idea
    prompt = "Generate a unique business idea based on the following metadata:\n" + metadata

    # Function to generate business idea in a thread
    def generate_idea(prompt):
        try:
            # Generate business idea using OpenAI GPT-3
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7
            )
            business_idea = response.choices[0].text.strip()
        except Exception as e:
            business_idea = f"Error generating business idea: {str(e)}"
        return business_idea

    # Start a new thread to generate business idea
    thread = Thread(target=generate_idea, args=(prompt,))
    thread.start()

    return jsonify({'message': 'Generating business idea...'})


if __name__ == '__main__':
    app.run(debug=True)
