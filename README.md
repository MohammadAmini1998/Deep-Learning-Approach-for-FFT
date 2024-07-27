# A Machine Learning Approach to FFT in OFDM Receiver

## Overview

Orthogonal Frequency Division Multiplexing (OFDM) systems are widely used in high-speed communication networks due to their efficient use of the frequency spectrum. A critical component of OFDM systems is the Fast Fourier Transform (FFT) and its inverse (IFFT), which are essential for signal modulation and demodulation. However, while the FFT is effective in transforming signals between time-domain and frequency-domain representations, it can pose significant computational challenges, especially in high-speed communication systems.

## Project Objective

This project aims to address the computational limitations associated with the traditional FFT process in OFDM receivers. We propose an innovative approach that replaces the conventional FFT operation with a machine learning model. Specifically, we are exploring the use of feed-forward neural networks to perform the FFT operation. Our goal is to achieve similar or improved performance compared to traditional FFT methods while enhancing the speed of the processing.

## Key Goals

- **Enhance Speed**: Accelerate the FFT process by leveraging machine learning techniques.
- **Maintain Accuracy**: Ensure that the machine learning-based FFT performs with accuracy comparable to or better than traditional methods.
- **Reduce Computational Load**: Decrease the computational burden on high-speed communication systems.

## Approach

1. **Model Design**: Develop and train feed-forward neural networks to approximate the FFT operation.
2. **Performance Evaluation**: Compare the performance of the machine learning model against conventional FFT methods in terms of speed and accuracy.
3. **Integration**: Implement the trained model in an OFDM receiver to assess real-world applicability and benefits.

## Data Generation

To facilitate training and testing machine learning models for OFDM systems, we generate synthetic data that includes both time-domain and frequency-domain symbols. The dataset is created using the following approach:

1. **Parameters**:
   - **Number of Samples**: 100,000
   - **Number of Subcarriers**: 1 (for simplicity)

2. **Data Generation**:
   - Random time-domain symbols are generated.
   - The Fast Fourier Transform (FFT) is applied to these symbols to obtain the corresponding frequency-domain symbols.

3. **Data Preparation**:
   - The data is reshaped into a format suitable for modeling.
   - Input data (`X`) consists of frequency-domain symbols.
   - Output data (`y`) consists of time-domain symbols.

4. **Saving the Data**:
   - The generated dataset is saved as a CSV file (`ofdm_dataset.csv`), which includes columns for both time-domain and frequency-domain symbols.

This dataset serves as a basis for exploring machine learning approaches to perform FFT operations in OFDM systems, aiming to enhance processing speed and accuracy.
## Getting Started

To get started with the project, you will need to:

1. **Clone the Repository**:
   ```bash
   https://github.com/MohammadAmini1998/deep-learning-approach-for-FFT.git
   گگگکک
