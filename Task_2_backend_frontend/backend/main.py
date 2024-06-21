from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import T5Tokenizer, AutoModelForSeq2SeqLM
import subprocess
import os

# Define the request body

class Senario(BaseModel):
    text: str
    

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credential=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load the trained model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("debusaha/T5-large_plantumlcode_v3 ")
tokenizer= T5Tokenizer.from_pretrained("debusaha/T5-large_plantumlcode_v3 ")

@app.post("/generate")
async def generate_diagram(scenario: Scenario):
    # Generate PlantUML code from the scenario
    plantuml_code = generate_plantuml_code(scenario.text)

    # Write the PlantUML code to a file
    with open('diagram.puml', 'w') as file:
        file.write(plantuml_code)

    # Generate the diagram using PlantUML server
    subprocess.run(['java', '-jar', 'plantuml.jar', 'diagram.puml'])

    # Convert the generated .png file to a base64 string
    with open('diagram.png', 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Return the base64 string
    return {"diagram": encoded_string}

def generate_plantuml_code(description, max_length=512):
    # Tokenize and generate output
    inputs = tokenizer(description, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
    output_ids = model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_length=max_length)
    plantuml_code = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Ensure '@enduml' is present
    if '@enduml' not in plantuml_code:
        plantuml_code += '\n@enduml'
    
    return plantuml_code