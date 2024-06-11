# AI Engineer / Prompt Engineer

Welcome to the repo! This document outlines the tasks and requirements for candidates applying for a position in our team. Below, you'll find detailed descriptions of the job responsibilities, the dataset to be used, and the tasks to be completed as part of the recruitment process.

### Dataset

The dataset to be used for this project can be found on Hugging Face:
[coai/plantuml_generation](https://huggingface.co/datasets/coai/plantuml_generation)

### Task 1: Training a Large Language Model

- **Objective**: Train a Large Language Model using the provided dataset. The LLM should be capable of generating PlantUML code for a given scenario (which is an input to the LLM).
- **Platform**: The training can be conducted on Google Colab.
- **Deliverable**: A trained LLM that can successfully generate PlantUML code from scenario descriptions. Please upload the weights of the LLM on HuggingFace after training the LLM.

### Task 2: Backend and Frontend Development

- **Backend Development**:
  - **Objective**: Develop a backend service that generates PlantUML code from a given scenario and converts it into an image.
  - **Technology**: The backend could be built using FastAPI .
  - **Deliverable**: A functioning backend that takes scenario descriptions as input and outputs PlantUML diagrams as images.

- **Frontend Development**:
  - **Objective**: Develop a frontend interface where users can input scenarios and view the generated PlantUML diagrams.
  - **Technology**: The frontend can be built using ReactJS or NextJS.
  - **Deliverable**: A user-friendly web interface that displays the PlantUML diagrams based on user input.

## Getting Started

1. **Clone/Fork the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up the environment**:
    - Ensure you have Python and Node.js installed.
    - Install necessary Python packages for LLM training and FastAPI backend.
    - Install necessary JavaScript packages for ReactJS/NextJS frontend.
      
3. **Access the dataset**:
    - Download the dataset from [Hugging Face](https://huggingface.co/datasets/coai/plantuml_generation) and prepare it for model training.

4. **Begin with Task 1**:
    - Train the LLM on Google Colab.
    - Upload the weights to HuggingFace under own profile.
    - Save the trained model for use in the backend service.

5. **Develop the Backend**:
    - Create a FastAPI service that uses the trained LLM to generate PlantUML code.
    - Implement functionality to convert PlantUML code into images.

6. **Develop the Frontend**:
    - Build a ReactJS/NextJS application that interacts with the backend.
    - Ensure the frontend can display the generated PlantUML diagrams based on user input.

## Submission

- Ensure all code is well-documented and follows best practices.
- Create a detailed report explaining your approach, challenges faced, and how you overcame them. Let it be brief.
- Submit your final code and report by providing us the links to your repositories. The links to the weights on the HuggingFace should also be present in your report.

We look forward to seeing your innovative solutions and welcoming you to the DIAS Project team!

**Good luck!**
