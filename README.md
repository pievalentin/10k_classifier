# PSP x Udem Hackathon 👩‍💻🧑‍💻

<p align="center">
  <img src="https://p.kindpng.com/picc/s/378-3782668_investissments-ps2p-investments-public-sector-pension-investment-board.png">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlYAhCHpZxXshjxj6gOeN0hqgbSppWeYEkUg&s">
</p>

Welcome to this event organized by PSP and sponsored by Microsoft! In this challenge, we will take time to do something very usual at PSP. A NLP classficitation task. 
For this test we are using the dataset from this the Kaggle competition: [Financial Computing Workshop 2021](https://www.kaggle.com/competitions/en553803-financial-computing-workshop-2021/overview).

There are 8 classes:
| Class Number | Class Name |
|--------------|-------------|
| 1            | Manufacturing |
| 2            | Mining |
| 3            | Finance, Insurance, And Real Estate |
| 4            | Services |
| 5            | Wholesale Trade |
| 6            | Construction |
| 7            | Transportation, Communications, Electric, Gas, And Sanitary Services |
| 8            | Agriculture, Forestry, And Fishing |
| 9            | Retail Trade |

In this repo we duplicated the dataset CSV. Your objective is to write a model that will have the best precision and F1 score on a 80/20 split of the training dataset. 
You can use any technique you want, the only condition is that it can be trained in reasonable time and be evaluated by the CI/CD or a Jury in reasonable time.

To get you started in `predictor.py` we defined a base model you can start from. 
`test_predictor.py` is a pytest that will train your model and output the prediction report. When you submit a pr to this repo, this test will be launched. 
You could over train on the dataset but we will verify each approach individually for final grading 😈

## Evaluation Process

2. **Model Submission**: Participants submit their models via PR.
3. **Evaluation Script**: The script in CI/CD automatically evaluates the submitted models against the dataset.

## How to Submit Your Model

1. Fork this repository.
2. Modify the predictor.py with your own model
3. Create a Pull Request with your changes.

## Evaluation Criteria

- **Recall, Precision and F1 score**
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
4. get the dataset. Either download from the Kaggle competition: [Financial Computing Workshop 2021](https://www.kaggle.com/competitions/en553803-financial-computing-workshop-2021/overview). Or you can git pull the csv from git lfs directly. Make sure you have git lfs installed see: https://git-lfs.com/

5. Run the evaluation script:
    ```bash
    poetry run python evaluate.py
    ```

# Sponsor 
Big thanks to Microsoft for sponsoring the event!
<p align="center">
  <img src="data:image/png;base64,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">
</p>