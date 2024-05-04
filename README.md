
# Trading Bot

This repository contains a Jupyter Notebook for a trading bot developed using the Financial Reinforcement Learning (FinRL) framework, specifically designed to work with the Dow 30 stocks. The bot follows a systematic approach to trading, integrating financial data handling, preprocessing, model training, and potentially executing trades via the Alpaca API.

## Overview

The trading bot notebook recreates the necessary steps to:
- Fetch financial data from the Dow 30 stocks list.
- Preprocess the data by adding technical indicators and risk management metrics.
- Set up the model environment.
- Train the model to execute trades based on learned strategies.

## Prerequisites

Before running this notebook, ensure you have the following:
- Python 3.8 or later.
- Jupyter Notebook or JupyterLab installed.
- Necessary Python libraries which can be installed via requirements file (if provided) or through pip:
  ```bash
  pip install -r requirements.txt
  ```

## Setup

To get started with this trading bot, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook in your Jupyter environment:
   ```bash
   jupyter notebook trading_bot_v2.ipynb
   ```
