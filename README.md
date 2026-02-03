README
# 🧠 Brain Tumor Detection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview
This project is a **Biomedical Informatics** application designed to detect and localize brain tumors from MRI (Magnetic Resonance Imaging) scans. By leveraging **Computer Vision** techniques and **Image Processing** algorithms, the system automates the identification of pathological anomalies, aiming to assist medical professionals in early diagnosis.

## 🚀 Key Features
* **Preprocessing:** Noise reduction and image enhancement using Gaussian Blur.
* **Segmentation:** Utilizing Thresholding and Morphological Operations to isolate the brain structure.
* **Tumor Detection:** Contour detection algorithms to pinpoint high-intensity tumor regions.
* **Visualization:** Highlights the detected tumor area directly on the original MRI scan.

## 🛠️ Tech Stack
* **Language:** Python
* **Core Library:** OpenCV (cv2)
* **Data Manipulation:** NumPy
* **Visualization:** Matplotlib

## ⚙️ How It Works (Methodology)
1.  **Grayscale Conversion:** Converts raw RGB MRI scans to grayscale for processing.
2.  **Filtering:** Applies filters to remove noise and smooth the image.
3.  **Thresholding:** Uses binary thresholding to separate the tumor (usually brighter) from the background.
4.  **Morphological Operations:** Erodes and dilates the image to remove false positives and refine the tumor shape.
5.  **Contour Analysis:** Finds the contours of the segmented area and draws a bounding box around the tumor.

## 📂 Project Structure
