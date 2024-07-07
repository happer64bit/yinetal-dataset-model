> [!NOTE]  
> We are looking for the volunteer for writing rude words for dataset

# Yinetal Model

This repository contains datasets of rude words in Burmese and a model for censoring these words to provide a safe environment, particularly for children.

## Purpose

The purpose of this project is to automatically detect and censor offensive Burmese words in text data. This helps create safer online environments by filtering out inappropriate content, which is crucial for platforms catering to children and sensitive audiences.

## Features

- **Dataset**: Includes datasets of Burmese words labeled as rude or non-rude.
- **Model**: Utilizes a logistic regression model trained on this dataset to predict whether a word is rude based on its context.
- **Functionality**: Provides methods to load data, train the model, evaluate its performance, and censor text by replacing rude words with asterisks.

## Usage

To use the Yinetal Model:

1. **Clone the repository**:
   ```
   git clone https://github.com/happer64bit/yinetal-dataset-model.git
   cd yinetal-dataset-model
   ```

2. **Set up your environment**:
   - Ensure Python and necessary dependencies are installed (`pandas`, `scikit-learn`, etc.).

3. **Load and preprocess data**:
   - Use the provided datasets (`words.csv`).

4. **Train the model**:
   - Use the `train()` method to train the logistic regression model on your dataset.

5. **Evaluate model performance**:
   - Use the `evaluate()` method to assess the accuracy and other metrics of the trained model.

6. **Censor text**:
   - Use the `predict()` method to censor text by replacing offensive Burmese words with asterisks (`*`).

## Contributing

Contributions to improve the dataset, model performance, or documentation are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
