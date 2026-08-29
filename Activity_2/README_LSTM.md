# Text Classification with LSTM

## Overview
This project performs binary sentiment classification on the IMDB movie reviews dataset using a Long Short-Term Memory (LSTM) neural network.

## Dataset
- Dataset: IMDB Dataset
- Sample used: 3,000 reviews
- Classes:
  - Positive → 1
  - Negative → 0
- Train/Test split: 80% / 20%

## Preprocessing
The same preprocessing setup as the RNN activity is used:
- Reviews are tokenized using `tiktoken`.
- Encoding used: `cl100k_base`
- Maximum sequence length: 256 tokens
- Reviews longer than 256 tokens are truncated.
- Shorter reviews are padded.

## Model
The model architecture is:

`Token IDs → Embedding → LSTM → Linear → Sentiment`

- Embedding dimension: 64
- LSTM hidden dimension: 64
- Output: Binary sentiment prediction

## Training
- Loss function: `BCEWithLogitsLoss`
- Optimizer: Adam
- Learning rate: 0.001
- Batch size: 32
- Epochs: 5
- Gradient clipping: 1.0

## Result
- Training Accuracy: **80.25%**
- Test Accuracy: **59.83%**
- Final Training Loss: **0.4450**

## Comparison with RNN
The LSTM achieved:
- **59.83%** test accuracy compared with **56.00%** for the RNN.
- An improvement of **3.83 percentage points**.
- Lower final training loss: **0.4450** compared with **0.5241** for the RNN.

## Custom Testing
The LSTM was tested using the same custom review sentences used for the RNN. It correctly classified the strongly positive and negative examples used in the experiment.

## Files
- `Text_Classification_LSTM.ipynb` — Jupyter Notebook containing preprocessing, model training, evaluation, and custom predictions.
- `IMDB Dataset.csv` — Dataset used for training and testing.

## Conclusion
The LSTM performed better than the simple RNN in this experiment. Its gated memory mechanism helps it retain and selectively update information across a sequence, which can improve learning of sentiment-related patterns.
