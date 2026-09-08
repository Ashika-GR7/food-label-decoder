import cv2


def preprocess_image(image_path):
    """
    Preprocess a food-label image to improve OCR quality.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Could not read the image.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize image for better OCR
    scale = 2
    resized = cv2.resize(
        gray,
        None,
        fx=scale,
        fy=scale,
        interpolation=cv2.INTER_CUBIC
    )

    # Reduce small image noise
    denoised = cv2.GaussianBlur(resized, (3, 3), 0)

    # Convert to black and white
    processed = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return processed