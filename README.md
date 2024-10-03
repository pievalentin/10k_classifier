# Udem Hackathon

This repository contains the code to evaluate models submitted through Pull Requests (PRs) for the Udem Hackathon. The evaluation process uses a dataset from the Kaggle competition: [Financial Computing Workshop 2021](https://www.kaggle.com/competitions/en553803-financial-computing-workshop-2021/overview).

## Evaluation Process

1. **Dataset**: The dataset is sourced from the Kaggle competition mentioned above.
2. **Model Submission**: Participants submit their models via PR.
3. **Evaluation Script**: The script in CI/CD automatically evaluates the submitted models against the dataset.

## How to Submit Your Model

1. Fork this repository.
2. Modify the predictor.py with your own model
3. Create a Pull Request with your changes.

## Evaluation Criteria

- **F1 score**
- **Style and ingeniosity**

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/pievalentin/udem-hackathon.git
    ```
2. Install [Poetry](https://python-poetry.org/docs/#installation):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
3. Install the required dependencies:
    ```bash
    poetry install
    ```
4. Run the evaluation script:
    ```bash
    poetry run python evaluate.py
    ```
