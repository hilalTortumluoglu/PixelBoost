import cv2
from cv2 import dnn_superres

def upscale_image(file_path: str):
    """
    Upscale an image using the EDSR model with a scale factor of 3.
    :param file_path: Path to the input image.
    :return: Upscaled image.
    """
    try:
        sr = dnn_superres.DnnSuperResImpl_create()
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Could not read the image from {file_path}")

        model_path = "EDSR_x3.pb"
        sr.readModel(model_path)
        sr.setModel("edsr", 3)

        sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        upscaled_image = sr.upsample(image)
        return upscaled_image
    except Exception as e:
        print(f"Error during upscaling: {e}")
        return None
