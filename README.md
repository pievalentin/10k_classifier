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
  <img src="https://github.com/user-attachments/assets/638a91f4-3bd8-4385-8c32-6ce96e0b010b">
</p>
