import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2


def add_text_to_image(image, text, position, font, color):
    # Load the font using PIL
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    # Add text to the image with the loaded custom font using PIL
    draw.text(position, text, font=font, fill=color)

    # Convert back to OpenCV format
    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    return cv_image_with_text


def write_front_text(NAME, ID, EMAIL, PHONE, TEMPLATE_PATH):
    # Read the image using OpenCV
    image = cv2.imread(TEMPLATE_PATH)

    # Font settings
    font_color = (0, 0, 0)
    font_path = r"C:\wbl\vishal\myapp\Card\MartianMono_SemiCondensed-Regular.ttf"
    font_size = 20

    # Load the font using PIL and initialize it once for reuse
    font = ImageFont.truetype(font_path, size=font_size)

    # Define text positions dynamically
    positions = [
        (250, 656),  # NAME
        (250, 708),  # ID
        (250, 760),  # EMAIL
        (250, 812),  # PHONE
    ]

    # Add each text to the image
    for text, position in zip([NAME, ID, EMAIL, PHONE], positions):
        image = add_text_to_image(image, text, position, font, font_color)

    # Save the image with the added text
    output_image_path = f"{ID}_front.jpg"
    cv2.imwrite(output_image_path, image)


def write_text_back(DEPT, JOINING, ENDING, TEMPLATE_PATH, ID):
    # Read the image using OpenCV
    image = cv2.imread(TEMPLATE_PATH)

    # Font settings
    font_color = (0, 0, 0)
    font_path = r"C:\wbl\vishal\myapp\Card\MartianMono_SemiCondensed-Regular.ttf"
    font_size = 20

    # Load the font using PIL and initialize it once for reuse
    font = ImageFont.truetype(font_path, size=font_size)

    # Define text positions dynamically
    positions = [
        (360, 665),  # DEPT
        (360, 715),  # JOINING
        (360, 765),  # ENDING
    ]

    # Convert JOINING and ENDING to strings if they are not already
    if not isinstance(JOINING, str):
        JOINING = JOINING.strftime("%d-%m-%Y")
    if not isinstance(ENDING, str):
        ENDING = ENDING.strftime("%d-%m-%Y")

    # Add each text to the image
    for text, position in zip([DEPT, JOINING, ENDING], positions):
        image = add_text_to_image(image, text, position, font, font_color)

    # Save the image with the added text
    output_image_path = f"{ID}_back.jpg"
    cv2.imwrite(output_image_path, image)


def write_front_image(IMG, ID):
    # Read the new image to be added
    nparr = np.frombuffer(IMG, np.uint8)
    profile_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Construct the path for the existing image
    existing_image_path = f"{ID}_front.jpg"

    # Check if the existing image file exists
    if os.path.exists(existing_image_path):
        # Read the existing image using OpenCV
        existing_image = cv2.imread(existing_image_path)

        # Check if the existing image is loaded successfully
        if existing_image is not None:
            # Convert the OpenCV image to a PIL image
            pil_existing_image = Image.fromarray(cv2.cvtColor(existing_image, cv2.COLOR_BGR2RGB))

            # Calculate positions for centering the new image horizontally
            existing_image_width, existing_image_height = pil_existing_image.size

            # Custom resize the profile image to fit within the bounds of the existing image
            custom_width = 215
            custom_height = 274

            profile_image_resized = cv2.resize(profile_image, (custom_width, custom_height))

            # Calculate the x-coordinate to center the image horizontally
            new_image_x = (existing_image_width - custom_width) // 2

            # Overlay the new image onto the existing image using NumPy operations
            x_start = new_image_x
            x_end = new_image_x + custom_width
            y_start = 345
            y_end = 345 + custom_height
            existing_image[y_start:y_end, x_start:x_end] = profile_image_resized

            # Convert back to PIL format
            cv_image_with_text = cv2.cvtColor(existing_image, cv2.COLOR_BGR2RGB)
            pil_image_with_text = Image.fromarray(cv_image_with_text)

            # Save the image with the added text
            output_image_path = f"static/download/{ID}_front.jpg"
            pil_image_with_text.save(output_image_path)

        else:
            print(f"Error: Existing image at {existing_image_path} could not be loaded.")
    else:
        print(f"Error: Existing image file {existing_image_path} not found.")


def write_qr(QR_PATH, ID):
    # Read the existing image using OpenCV
    existing_image_path = f"{ID}_back.jpg"
    existing_image = cv2.imread(existing_image_path)

    # Read the new image to be added
    profile_image = cv2.imread(QR_PATH)

    # Convert the OpenCV image to a PIL image
    pil_existing_image = Image.fromarray(cv2.cvtColor(existing_image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_existing_image)

    # Calculate positions for centering the new image horizontally
    existing_image_width, existing_image_height = pil_existing_image.size

    # Custom resize the profile image to fit within the bounds of the existing image
    custom_width = 350
    custom_height = 350

    profile_image_resized = cv2.resize(profile_image, (custom_width, custom_height))

    # Calculate the x-coordinate to center the image horizontally
    new_image_x = (existing_image_width - custom_width) // 2

    # Overlay the new image onto the existing image using NumPy operations
    x_start = new_image_x
    x_end = new_image_x + custom_width
    y_start = 280
    y_end = 280 + custom_height
    existing_image[y_start:y_end, x_start:x_end] = profile_image_resized

    # Convert back to PIL format
    cv_image_with_text = cv2.cvtColor(existing_image, cv2.COLOR_BGR2RGB)
    pil_image_with_text = Image.fromarray(cv_image_with_text)

    # Save the image with the added text
    output_image_path = f"static/download/{ID}_back.jpg"
    pil_image_with_text.save(output_image_path)
    os.remove(QR_PATH)
    os.remove(existing_image_path)

# --------------------------------------------------------------------------------------------------------------


def write_front_text_student(NAME, ID, COURSE, BRANCH, PHONE, TEMPLATE_PATH):
    output_image_path = f"{ID}_front.jpg"
    # Read the image using OpenCV
    image = cv2.imread(TEMPLATE_PATH)

    # Font settings
    font_color = (0, 0, 0)
    font_path = r"C:\wbl\vishal\myapp\Card\MartianMono_SemiCondensed-Regular.ttf"
    font_size = 20

    # Load the font using PIL and initialize it once for reuse
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.truetype(font_path, size=font_size)

    # Define text positions dynamically
    positions = [
        (280, 648),  # NAME
        (280, 690),  # ID
        (280, 732),  # COURSE
        (280, 774),  # BRANCH
        (280, 816),  # PHONE
    ]

    # Add each text to the image
    for text, position in zip([str(NAME), str(ID), str(COURSE), str(BRANCH), str(PHONE)], positions):
        draw.text(position, text, font=font, fill=font_color)

    # Convert back to OpenCV format
    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # Save the image with the added text
    cv2.imwrite(output_image_path, cv_image_with_text)


def write_text_back_student(BATCH, VALID_FROM, VALID_UPTO, ADDRESS1, ADDRESS2, TEMPLATE_PATH, ID):
    output_image_path = f"{ID}_back.jpg"
    # Read the image using OpenCV
    image = cv2.imread(TEMPLATE_PATH)

    # Font settings
    font_color = (0, 0, 0)
    font_path = r"C:\wbl\vishal\myapp\Card\MartianMono_SemiCondensed-Regular.ttf"
    font_size = 20

    # Load the font using PIL and initialize it once for reuse
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.truetype(font_path, size=font_size)

    # Define text positions dynamically
    positions = [
        (300, 637),  # BATCH
        (300, 677),  # VALID_FROM
        (300, 717),  # VALID_UPTO
        (300, 760),  # ADDRESS1
        (300, 800),  # ADDRESS2
    ]

    # Convert VALID_FROM and VALID_UPTO to strings if they are not already
    if not isinstance(VALID_FROM, str):
        VALID_FROM = VALID_FROM.strftime("%d-%m-%Y")
    if not isinstance(VALID_UPTO, str):
        VALID_UPTO = VALID_UPTO.strftime("%d-%m-%Y")

    # Add each text to the image
    for text, position in zip([str(BATCH), VALID_FROM, VALID_UPTO, ADDRESS1, ADDRESS2], positions):
        draw.text(position, text, font=font, fill=font_color)

    # Convert back to OpenCV format
    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # Save the image with the added text
    cv2.imwrite(output_image_path, cv_image_with_text)


def write_qr_student(QR_PATH, ID):
    # Read the existing image using OpenCV
    existing_image_path = f"{ID}_back.jpg"
    existing_image = cv2.imread(existing_image_path)

    # Read the new image to be added
    profile_image = cv2.imread(QR_PATH)

    # Convert the OpenCV image to a PIL image
    pil_existing_image = Image.fromarray(cv2.cvtColor(existing_image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_existing_image)

    # Calculate positions for centering the new image horizontally
    existing_image_width, existing_image_height = pil_existing_image.size

    # Custom resize the profile image to fit within the bounds of the existing image
    custom_width = 325
    custom_height = 325

    profile_image_resized = cv2.resize(profile_image, (custom_width, custom_height))

    # Calculate the x-coordinate to center the image horizontally
    new_image_x = (existing_image_width - custom_width) // 2

    # Overlay the new image onto the existing image using NumPy operations
    x_start = new_image_x
    x_end = new_image_x + custom_width
    y_start = 280
    y_end = 280 + custom_height
    existing_image[y_start:y_end, x_start:x_end] = profile_image_resized

    # Convert back to PIL format
    cv_image_with_text = cv2.cvtColor(existing_image, cv2.COLOR_BGR2RGB)
    pil_image_with_text = Image.fromarray(cv_image_with_text)

    # Save the image with the added text
    output_image_path = f"static/download/{ID}_back.jpg"
    pil_image_with_text.save(output_image_path)

