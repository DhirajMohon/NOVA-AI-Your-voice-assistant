import google.generativeai as genai
from PIL import Image
from io import BytesIO
import base64

# Configure the Gemini API key
genai.configure(api_key="************")  # Replace with your actual key

# Set up the model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",  # Use the correct model that supports image generation
)

# Create a prompt
prompt = (
    "Create a 3D rendered image of a pig with wings and a top hat "
    "flying over a happy futuristic sci-fi city with lots of greenery."
)

# Generate the content
response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(response_mime_type="image/png"),
)

# Handle the image response
image_data = response.binary  # This is a byte string of the PNG image

# Convert to PIL image and display/save it
image = Image.open(BytesIO(image_data))
image.save("gemini_generated_image.png")
image.show()
