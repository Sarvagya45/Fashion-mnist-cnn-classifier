# CNN Fashion MNIST Classifier — PyTorch

A Convolutional Neural Network (CNN) built with PyTorch to classify images from the [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset into 10 clothing categories.

---

## 📌 Project Overview

This project trains a CNN on the Fashion MNIST dataset to recognize grayscale 28×28 images of fashion items. The model is trained end-to-end in a Jupyter Notebook using PyTorch, with GPU acceleration support via CUDA.

---

## 🗂️ Dataset

The dataset used is the **Fashion MNIST** dataset in CSV format, where:
- Each row represents one image.
- The first column is the **label** (class index 0–9).
- The remaining 784 columns are **pixel values** (pixel1 to pixel784), representing a flattened 28×28 grayscale image.

### Class Labels

| Label | Category       |
|-------|----------------|
| 0     | T-shirt/top    |
| 1     | Trouser        |
| 2     | Pullover       |
| 3     | Dress          |
| 4     | Coat           |
| 5     | Sandal         |
| 6     | Shirt          |
| 7     | Sneaker        |
| 8     | Bag            |
| 9     | Ankle boot     |

---

## 🧠 Model Architecture

The CNN consists of:
- **Convolutional layers** for spatial feature extraction
- **Max Pooling layers** for downsampling
- **Fully Connected layers** for classification
- **ReLU activations** throughout
- **Softmax/CrossEntropyLoss** for multi-class output

---

## ⚙️ Tech Stack

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python 3     | Programming language             |
| PyTorch      | Deep learning framework          |
| pandas       | Data loading and manipulation    |
| scikit-learn | Train/test splitting             |
| matplotlib   | Visualization                    |
| CUDA (GPU)   | Accelerated training (if available) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cnn-fashion-mnist-pytorch.git
cd cnn-fashion-mnist-pytorch
```

### 2. Install Dependencies

```bash
pip install torch torchvision pandas scikit-learn matplotlib
```

> For GPU support, install the appropriate CUDA-compatible version of PyTorch from [pytorch.org](https://pytorch.org/get-started/locally/).

### 3. Add the Dataset

Download the Fashion MNIST CSV dataset (e.g., from [Kaggle](https://www.kaggle.com/datasets/zalando-research/fashionmnist)) and place it in the project directory.

### 4. Run the Notebook

Open and run the notebook in Jupyter or Google Colab:

```bash
jupyter notebook cnn-fashion-mnist-pytorch.ipynb
```

---

## 📊 Results

The model is trained with a fixed random seed (`torch.manual_seed(42)`) to ensure reproducibility. Training automatically uses GPU (`cuda`) if available, otherwise falls back to CPU.

> Training accuracy and loss curves are plotted using `matplotlib` within the notebook.

---

## 📁 Project Structure

```
cnn-fashion-mnist-pytorch/
│
├── cnn-fashion-mnist-pytorch.ipynb   # Main notebook
├── README.md                          # Project documentation
└── data/                              # Place Fashion MNIST CSV files here
    ├── fashion-mnist_train.csv
    └── fashion-mnist_test.csv
```

---

## 🙋 Author

**Sarvagya Gupta**  
Feel free to connect or raise issues if you have suggestions or questions!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
