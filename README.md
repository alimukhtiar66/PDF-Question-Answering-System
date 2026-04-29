# PDF Question Answering System

This project is a simple PDF Question Answering system built using Python, Streamlit, and Scikit-learn.
It allows users to upload a PDF file and ask questions. The system finds the most relevant sentence using TF-IDF and cosine similarity.

# Features

* Upload any PDF file
* Extract text automatically
* Ask questions from the document
* Uses cosine similarity for finding best answer
* Simple and beginner-friendly code

# Technologies Used

* Python
* Streamlit
* PyPDF2
* Scikit-learn

# Installation

pip install streamlit PyPDF2 scikit-learn

# How It Works

1. PDF is uploaded
2. Text is extracted using PyPDF2
3. Text is split into sentences
4. TF-IDF converts text into vectors
5. Cosine similarity finds the most relevant sentence
6. Best matching sentence is shown as answer
