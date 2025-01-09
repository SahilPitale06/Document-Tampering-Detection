# Document Tampering Detection

This repository contains the code and resources for a **Document Tampering Detection** project. The goal of this project is to detect alterations in documents using **Machine Learning (ML) and Image Processing** techniques.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributors](#contributors)
- [License](#license)

## Overview

Document forgery is a critical issue in various sectors, including banking, legal, and government organizations. This project aims to identify tampered documents by analyzing visual and textual inconsistencies using **Python, OpenCV, and Machine Learning models**.

## Features

- **Image Preprocessing**: Extracts and enhances document features.
- **Forgery Detection**: Identifies anomalies and inconsistencies.
- **Machine Learning Model**: Trained to classify tampered vs. genuine documents.
- **Web Interface**: Built using **Flask** for easy user interaction.

## Installation

To run this project locally, ensure you have Python installed. Then, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SahilPitale06/Document-Tampering-Detection.git
   cd Document-Tampering-Detection
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not available, manually install the necessary packages:*

   ```bash
   pip install numpy pandas scikit-learn flask opencv-python matplotlib
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the web interface:**

   Open a web browser and navigate to `http://127.0.0.1:5000/`. You can upload a document image to check for tampering.

## Model Training

The model training process is documented in the Jupyter Notebook `document_tampering.ipynb`. It includes:

- **Data Preprocessing**: Extracting key features from documents.
- **Feature Engineering**: Using **image processing techniques** like edge detection and contour analysis.
- **Model Selection**: Training ML models such as **Random Forest, SVM, and CNN-based classifiers**.
- **Model Serialization**: Saving the trained model (`model.pkl`) for future use.

## Evaluation

The trained model's performance is evaluated using metrics like **accuracy, precision, recall, and F1-score**. Detailed evaluation results and visualizations are available in the Jupyter Notebook.

## Contributors

- [Sahil Pitale](https://github.com/SahilPitale06)

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

*Note: This README provides a general overview. For detailed explanations and code insights, refer to the Jupyter Notebook and Python scripts in the repository.*
