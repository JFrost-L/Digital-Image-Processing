# Digital Image Processing Project

This repository contains a collection of digital image processing techniques implemented using Python and OpenCV. The project explores various image enhancement, filtering, transformation, and segmentation methods that are commonly used in computer vision and image analysis tasks.

## Table of Contents
1. [Overview](#overview)
2. [Technologies Used](#technologies-used)
3. [Key Features](#key-features)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [License](#license)

## Overview

Digital Image Processing refers to the use of computer algorithms to perform operations on digital images. It involves a variety of techniques to manipulate, enhance, and analyze image data. This project demonstrates core concepts in image processing such as:

- Image filtering (e.g., Gaussian Blur, Median Filter)
- Image enhancement (e.g., Histogram Equalization, Contrast Stretching)
- Edge detection (e.g., Sobel, Canny)
- Image segmentation (e.g., Thresholding, Watershed)
- Morphological operations (e.g., Erosion, Dilation)
- Frequency domain transformations (e.g., Fourier Transform)

## Technologies Used

- **Python**: The main programming language used for implementing algorithms.
- **OpenCV**: A widely-used computer vision library for image processing tasks.
- **NumPy**: A powerful library for numerical computing with Python, used for handling image data.
- **Matplotlib**: For plotting images and visualizing the results of various processing techniques.

## Key Features

1. **Image Enhancement**:
   - **Histogram Equalization**: Improving the contrast of an image by stretching the pixel intensity distribution.
   - **Gamma Correction**: Adjusting brightness of an image.
   - **Contrast Stretching**: Linear transformation of pixel values to enhance contrast.

2. **Image Filtering**:
   - **Gaussian Blur**: Reducing image noise and detail using Gaussian smoothing.
   - **Median Filter**: A non-linear filter for noise removal, especially effective for salt-and-pepper noise.
   - **Bilateral Filter**: Reduces noise while preserving edges.

3. **Edge Detection**:
   - **Sobel Filter**: Gradient-based method for detecting edges in horizontal and vertical directions.
   - **Canny Edge Detector**: A multi-stage edge detection algorithm.
   - **Laplacian of Gaussian (LoG)**: A method for detecting edges by combining Laplacian and Gaussian filtering.

4. **Image Segmentation**:
   - **Thresholding**: Simple binary and adaptive thresholding for separating objects from the background.
   - **Watershed Algorithm**: A powerful method for separating overlapping objects in an image.

5. **Morphological Operations**:
   - **Erosion**: Removes pixels on object boundaries.
   - **Dilation**: Adds pixels to the boundaries of objects.
   - **Opening/Closing**: Combination of erosion and dilation to remove small objects or fill small holes.

6. **Frequency Domain Processing**:
   - **Fourier Transform**: Transforming the image to the frequency domain for filtering and analysis.
   - **High-Pass and Low-Pass Filtering**: Emphasizing or reducing certain frequencies in an image.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/digital-image-processing.git
   cd digital-image-processing
