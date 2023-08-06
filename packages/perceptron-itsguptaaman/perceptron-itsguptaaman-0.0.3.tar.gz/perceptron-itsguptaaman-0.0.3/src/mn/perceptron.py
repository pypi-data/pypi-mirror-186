import os
import pandas as pd
import numpy as np
import joblib
import logging


# Creating a perceptorn classs from stratch
class Perceptron:

    def __init__(self, learning_rate: float = None, epochs: int = None):

        self.weights = np.random.randn(3) * 1e-4  # Small random weights
        training = (learning_rate is not None) and (epochs is not None)

        if training:
            logging.info(f"Initial weights before training: \n{self.weights}")
        self.learning_rate = learning_rate
        self.epochs = epochs

    # Starting with _ (underscore) means it is an internal method
    def _zee_outcome(self, inputs, weights):
        """
        Description: This is a internal function which takes arguments inputs, weights and multiply them.
        Args:
        inputs (columns) : This is a columns passed by user.
        weights (float) : It is a numerical value
        Returns:
        (float): Dot product of the arguments 
        """
        try:
            return np.dot(inputs, weights)

        except Exception as e:
            logging.info(e)

    # step function
    def activation_function(self, z):
        try:
            return np.where(z > 0, 1, 0)

        except Exception as e:
            logging.info(e)

    # X is inputs y is labels
    def fit(self, X, y):
        try:
            self.X = X
            self.y = y

            # Adding bias with X
            X_with_bias = np.c_[self.X, - np.ones((len(self.X), 1))]
            logging.info(f"X with bias is :\n{X_with_bias}")

            for epoch in range(self.epochs):
                logging.info("--"*10)
                logging.info(f"for epoch --> {epoch}")
                logging.info("--"*10)

                z = self._zee_outcome(X_with_bias, self.weights)
                y_hat = self.activation_function(z)
                logging.info(
                    f"Predicted value after forwar propagation is: \n{y_hat}")

                self.error = self.y - y_hat
                logging.info(f"error: \n{self.error}")

                # Weight update rule
                self.weights = self.weights + self.learning_rate * \
                    np.dot(X_with_bias.T, self.error)
                logging.info(
                    f"Updated weights after epoch: {epoch + 1}/{self.epochs}: \n{self.weights} ")
                logging.info("##"*10)

        except Exception as e:
            logging.info(e)

    def predict(self, test_inputs):
        try:
            X_with_bias = np.c_[test_inputs, - np.ones((len(test_inputs), 1))]
            z = self._zee_outcome(X_with_bias, self.weights)
            return self.activation_function(z)

        except Exception as e:
            logging.info(e)

    def total_loss(self):
        try:
            total_loss = np.sum(self.error)
            logging.info(f"\nTotal loss: {total_loss}\n")
            return total_loss

        except Exception as e:
            logging.info(e)

    # Starting with _ (underscore) means it is an internal method
    def _create_dir_return_path(self, model_dir, file_name):
        try:
            os.makedirs(model_dir, exist_ok=True)
            return os.path.join(model_dir, file_name)

        except Exception as e:
            logging.info(e)

    def model_store(self, file_name, model_dir=None):
        try:
            if model_dir is not None:
                model_file_path = self._create_dir_return_path(
                    model_dir, file_name)
                joblib.dump(self, model_file_path)

            else:
                model_file_path = self._create_dir_return_path(
                    "Model", file_name)
                joblib.dump(self, model_file_path)
            logging.info(
                f">>>> Model is saved at location {model_file_path} <<<<")

        except Exception as e:
            logging.info(e)

    def model_load(self, file_path):
        try:
            return joblib.load(file_path)

        except Exception as e:
            logging.info(e)
