import os
import uuid


def save_image(image):
    file_extension = os.path.splitext(image.filename)[1]
    new_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join("media", new_filename)
    with open(file_path, "wb") as f:
        f.write(image.file.read())
    return f"/media/{new_filename}"
