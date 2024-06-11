from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from plantuml import PlantUML
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Define the request body
class Scenario(BaseModel):
    text: str

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("debusaha/t5-base-plantuml")
tokenizer = T5Tokenizer.from_pretrained("t5-base")

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}

@app.post("/generate")
async def generate_diagram(scenario: Scenario):
    # Generate PlantUML code from the scenario
    plantuml_code = generate_plantuml_code(scenario.text)

    # Convert PlantUML code into an image
    image_path = convert_to_image(plantuml_code)

    # Return the image path
    return {"image_path": image_path}

def generate_plantuml_code(scenario):
    # Encode the scenario and generate the PlantUML code
    inputs = tokenizer.encode("generate code: " + scenario.text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)
    plantuml_code = tokenizer.decode(outputs[0])

    return plantuml_code

def convert_to_image(plantuml_code):
    # Write the PlantUML code to a file
    with open("diagram.uml", "w") as f:
        f.write(plantuml_code)

    # Convert the PlantUML code into an image
    puml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
    image_path = puml.processes_file('diagram.uml')

    # Return the image path
    return image_path
