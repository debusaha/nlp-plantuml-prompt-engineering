# Assuming plantuml_code_generated contains the output from the model
example_description = plantuml_code_generated

def generate_and_display_plantuml(description, model, tokenizer, device, max_length=512):
    # Tokenize and generate output
    inputs = tokenizer(description, return_tensors="pt", padding=True, truncation=True, max_length=max_length).to(device)
    output_ids = model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_length=max_length)
    plantuml_code = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Ensure '@enduml' is present
    if '@enduml' not in plantuml_code:
        plantuml_code += '\n@enduml'
    
    # Write to file and generate diagram
    with open('diagram.puml', 'w') as file:
        file.write(plantuml_code)
    
    # Generate the diagram using PlantUML server
    !java -jar plantuml.jar diagram.puml
    
    # Display the diagram
    from IPython.display import Image
    display(Image(filename='diagram.png'))

# Now call the function with the output from the model
generate_and_display_plantuml(example_description, model, tokenizer, device)
