# Text Classification with RNN

## Overview
This project performs binary sentiment classification on the IMDB movie reviews dataset using a simple Recurrent Neural Network (RNN).

## Dataset
- Dataset: IMDB Dataset
- Sample used: 3,000 reviews
- Classes:
  - Positive → 1
  - Negative → 0
- Train/Test split: 80% / 20%

## Preprocessing
- Reviews are tokenized using `tiktoken`.
- Encoding used: `cl100k_base`
- Maximum sequence length: 256 tokens
- Reviews longer than 256 tokens are truncated.
- Shorter reviews are padded.

## Model
The model architecture is:

`Token IDs → Embedding → RNN → Linear → Sentiment`

- Embedding dimension: 64
- RNN hidden dimension: 64
- Output: Binary sentiment prediction

## Training
- Loss function: `BCEWithLogitsLoss`
- Optimizer: Adam
- Learning rate: 0.001
- Batch size: 32
- Epochs: 5
- Gradient clipping: 1.0

## Result
- Training Accuracy: **80.00%**
- Test Accuracy: **56.00%**
- Final Training Loss: **0.5241**

## Custom Testing
The model was also tested on new review sentences to observe its sentiment predictions.

## Files
- `Text_Classification_RNN.ipynb` — Jupyter Notebook containing preprocessing, model training, evaluation, and custom predictions.
- `IMDB Dataset.csv` — Dataset used for training and testing.

## Conclusion
The RNN successfully learned sentiment patterns from the IMDB reviews. However, its test accuracy was relatively low compared with its training accuracy, indicating limited generalization on the small lab-scale dataset.
