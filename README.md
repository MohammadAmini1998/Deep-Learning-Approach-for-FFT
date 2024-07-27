# 🚀 A Machine Learning Approach to FFT in OFDM Receiver

## 🌟 Overview

Orthogonal Frequency Division Multiplexing (OFDM) systems are a cornerstone of high-speed communication networks due to their efficient utilization of the frequency spectrum. Central to OFDM systems are the Fast Fourier Transform (FFT) and its inverse (IFFT), which are crucial for converting signals between time-domain and frequency-domain representations. While FFT is effective, it can present significant computational challenges, especially in high-speed scenarios.

## 🎯 Project Objective

This project seeks to tackle the computational constraints of traditional FFT processes in OFDM receivers. We propose a groundbreaking approach that substitutes the conventional FFT operation with a machine learning model. Specifically, we aim to utilize feed-forward neural networks to replicate the FFT operation, striving for performance that matches or surpasses traditional methods, all while boosting processing speed.

## 🔑 Key Goals

- **⚡ Enhance Speed**: Accelerate the FFT process using advanced machine learning techniques.
- **🔍 Maintain Accuracy**: Ensure that the machine learning-based FFT performs with accuracy comparable to or exceeding traditional methods.
- **💪 Reduce Computational Load**: Lower the computational burden on high-speed communication systems.

## 🔍 Approach

1. **🧩 Model Design**: Develop and train feed-forward neural networks to approximate the FFT operation.
2. **🔬 Performance Evaluation**: Assess the machine learning model's performance against conventional FFT methods regarding speed and accuracy.
3. **🔧 Integration**: Deploy the trained model in an OFDM receiver to evaluate its practical benefits and applicability.

## 📊 Data Generation

To support the training and evaluation of machine learning models for OFDM systems, we generate synthetic data featuring both time-domain and frequency-domain symbols. Here’s how the dataset is created:

1. **📏 Parameters**:
   - **Number of Samples**: 100,000
   - **Number of Subcarriers**: 1 (for simplicity)

2. **🔢 Data Generation**:
   - Generate random time-domain symbols.
   - Apply the Fast Fourier Transform (FFT) to obtain corresponding frequency-domain symbols.

3. **🔄 Data Preparation**:
   - Reshape the data for modeling purposes.
   - **Input Data (`X`)**: Frequency-domain symbols.
   - **Output Data (`y`)**: Time-domain symbols.

4. **💾 Saving the Data**:
   - Save the dataset as a CSV file (`ofdm_dataset.csv`), including columns for both time-domain and frequency-domain symbols.

This dataset is fundamental for exploring machine learning methods to perform FFT operations in OFDM systems, aiming to improve both speed and accuracy.

## 📈 Results

Here are some visual results from the project:

![Results 1](https://github.com/user-attachments/assets/9a6c0e96-2351-4503-a322-c35e1062af1b)
![Results 2](https://github.com/user-attachments/assets/6f5efe02-2b5a-475a-94e7-2ac75f3706c5)

## 🚀 Getting Started

To get started with the project, follow these steps:

1. **🔄 Clone the Repository**:
   ```bash
   git clone https://github.com/MohammadAmini1998/deep-learning-approach-for-FFT.git
2. 📊 Generate the Dataset:
Run the dataset_generator script to create the dataset.

3. 📝 Train and Evaluate:
Execute project.ipynb to train the model and review the results.
##
Feel free to explore and contribute to this innovative approach to enhancing FFT processes in OFDM systems!
