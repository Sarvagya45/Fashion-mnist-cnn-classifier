# CNN Fashion MNIST Classifier — PyTorch & Streamlit

An end-to-end Machine Learning project featuring a Convolutional Neural Network (CNN) built with PyTorch to classify images from the [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset into 10 clothing categories. The project includes a Jupyter notebook for model training, a Streamlit-powered web application for real-time inference, and Docker configuration for easy deployment. 

**🎉 Live Demo**: [Deployed on Render](https://your-render-url.onrender.com) *(Update with your actual Render URL)*

---

## 📌 Project Overview

This project demonstrates the complete ML lifecycle:
1. **Model Training**: Training a CNN on the Fashion MNIST dataset using PyTorch with GPU acceleration.
2. **Web Interface**: Building an interactive web frontend using Streamlit to allow users to upload images and get predictions.
3. **Deployment**: Containerizing the application using Docker and deploying it seamlessly to Render.

---

## 🗂️ Dataset & Class Labels

The dataset used is the **Fashion MNIST** dataset, which consists of grayscale 28×28 images of fashion items.

| Label | Category       | Label | Category       |
|-------|----------------|-------|----------------|
| 0     | T-shirt/top    | 5     | Sandal         |
| 1     | Trouser        | 6     | Shirt          |
| 2     | Pullover       | 7     | Sneaker        |
| 3     | Dress          | 8     | Bag            |
| 4     | Coat           | 9     | Ankle boot     |

---

## 🧠 Model Architecture

The CNN is built from scratch and consists of:
- **Convolutional layers** for spatial feature extraction.
- **Max Pooling layers** for downsampling.
- **Fully Connected layers** for final classification into 10 distinct classes.
- **ReLU activations** and **CrossEntropyLoss**.

---

## ⚙️ Tech Stack

| Component      | Tools & Frameworks                           |
|----------------|----------------------------------------------|
| **Deep Learning** | PyTorch, Torchvision                       |
| **Frontend/UI** | Streamlit                                    |
| **Data Tools**  | Pandas, NumPy, Scikit-learn, Matplotlib, PIL |
| **Deployment**  | Docker, Render                               |

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.11+ installed. For GPU support during training, install the appropriate CUDA-compatible version of PyTorch.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cnn-fashion-mnist-pytorch.git
cd cnn-fashion-mnist-pytorch
```

### 2. Local Setup (Without Docker)

Navigate to the `app` directory and install the required packages:
```bash
cd app
pip install -r requirements.txt
```

Run the Streamlit application:
```bash
streamlit run main.py
```
The app will be accessible at `http://localhost:8501`.

### 3. Running with Docker

You can also run the application locally using Docker. This ensures a consistent environment matching the deployment on Render.

Build the Docker image:
```bash
cd app
docker build -t fashion-mnist-app .
```

Run the Docker container:
```bash
docker run -p 8501:8501 fashion-mnist-app
```
Access the application at `http://localhost:8501`.

---

## 📁 Project Structure

```
cnn-fashion-mnist-pytorch/
│
├── README.md                          # Project documentation
├── app/                               # Streamlit Web Application
│   ├── Dockerfile                     # Docker configuration
│   ├── main.py                        # Streamlit frontend & inference logic
│   ├── model.py                       # PyTorch model architecture class
│   ├── requirements.txt               # App dependencies
│   ├── config.toml                    # Streamlit configuration
│   └── trained_model/                 # Saved PyTorch model checkpoint (.pth)
│
├── model_training_notebook/           # Training scripts and notebooks
│   └── ...
│
└── test_images/                       # Sample images for testing the UI
    └── ...
```

---

## 🙋 Author

**Sarvagya Gupta**  
Feel free to connect or raise issues if you have suggestions or questions!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
