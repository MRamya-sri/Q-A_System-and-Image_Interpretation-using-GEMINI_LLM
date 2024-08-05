# Q/A System and Image Interpretation using GEMINI LLM

This project includes two applications that utilize Google's GEMINI LLM API:

1. **Q/A System**: A text-based question answering application.
2. **Image Interpretation**: An application for identifying and interpreting images.

## Project Structure

- `Text.py`: Implements the Q/A system for text-based interactions.
- `Image.py`: Implements the image interpretation functionality.

## Q/A System Overview

![Screenshot (566)](https://github.com/user-attachments/assets/e5ac0f16-dd8c-4b93-81b2-ed35105eb889)

## Image Interpretation
![Screenshot (567)](https://github.com/user-attachments/assets/fcff8778-257c-487a-9753-26660ebf5a6c)

![Screenshot (568)](https://github.com/user-attachments/assets/c9de4c04-38b5-4dc7-8bd8-34912a6588d1)

![Screenshot (569)](https://github.com/user-attachments/assets/785dd238-e79d-453b-a85a-d37ba4443600)



## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   
   cd your-repo-name

   pip install -r requirements.txt



## Usage
### Text Q/A System
Run the Streamlit app for the Q/A system:
"streamlit run Text.py" 
Open your web browser and navigate to http://localhost:8501 to access the Q/A system.
Interact with the application by entering questions into the provided input field and clicking the "Click here for Response to Your Question." button to receive responses from the GEMINI LLM.

### Image Interpretation
Run the Streamlit app for image interpretation:
"streamlit run Image.py"
Open your web browser and navigate to http://localhost:8501 to access the image interpretation application.
Upload an image by clicking on the "Choose an Image..." button. Once the image is uploaded, click the "Interpret about Image." button to get the interpretation from the GEMINI LLM.

## Contributing
Contributions are welcome! Please create a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Setup
   Create a .env file in the root directory of the project with the following content:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here


