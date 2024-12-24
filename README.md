
# Image Upscaler Application 🚀

This project is a GUI-based application for upscaling images using the Enhanced Deep Residual Networks (EDSR) model, leveraging **OpenCV** and **PyQt5**. With a sleek interface, it allows users to select an image, upscale it by a factor of 3 using deep learning, and save the output effortlessly.

---

## Features ✨

- **Deep Learning Upscaling**: Upscales images using the EDSR model for better clarity and detail.
- **User-Friendly Interface**: Built with PyQt5, featuring an intuitive multi-page GUI.
- **CUDA Acceleration**: Utilizes NVIDIA CUDA for faster image processing (if available).
- **File Handling**: Easy image selection and saving with QFileDialog.
- **Preview**: Side-by-side comparison of the original and upscaled image in the GUI.

---

## Getting Started 🛠️

### Prerequisites

- Python 3.8 or later
- Required libraries:
  - `opencv-python`
  - `opencv-contrib-python`
  - `PyQt5`

Install the dependencies using pip:

```bash
pip install opencv-python opencv-contrib-python PyQt5
```

### Model File

Download the EDSR model (`EDSR_x3.pb`) and place it in the project directory.  
You can find pre-trained models [here](https://github.com/opencv/opencv_contrib/tree/master/modules/dnn_superres).

---

## How to Run 🖥️

1. Clone the repository:

   ```bash
   git clone https://github.com/hilalTortumluoglu/PixelBoost.git
   ```

2. Launch the application:

   ```bash
   python pixelBoost.py
   ```

3. Use the interface to:
   - **Select an image** for upscaling.
   - **Preview** the upscaled result.
   - **Save** the processed image.

---

## Project Structure 📂

```plaintext
.
├── edsr.py                 # Upscaling logic using OpenCV's DNN Super Resolution module
├── pixelBoost.py           # Main application logic with PyQt5 interface
├── resolutionConverter.ui  # PyQt Designer UI file
├── resolutionConverter.py  # PyQt Designer py file
├── EDSR_x3.pb              # Pre-trained EDSR model for upscaling
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## Screenshots 📸

| Original Image          | Upscaled Image          |
|--------------------------|--------------------------|
| ![Original](example_org.jpg) | ![Upscaled](example_upscaled.jpg) |

---

## Acknowledgements 🙌

- OpenCV for the powerful `dnn_superres` module.
- PyQt5 for the smooth and user-friendly GUI framework.

---

Enjoy seamless image upscaling with our app! 🌟
