# ShareGPT + Langchain

This project was built using [Elapse](https://www.elapse.ai).

The concept behind ShareGPT + Langchain was informed by the research from this [video](https://www.youtube.com/watch?v=wVzuvf9D9BU) by 'AI Explain'.

## Relevant Sources

1. [Automatically Discovered Chain of Thought](https://arxiv.org/pdf/2305.02897.pdf)
2. [Karpathy Tweet](https://twitter.com/karpathy/status/1...)
3. [Best prompt: Theory of Mind](https://arxiv.org/ftp/arxiv/papers/23...)
4. [Few Shot Improvements](https://sh-tsang.medium.com/review-gp...)
5. [Dera Dialogue Paper](https://arxiv.org/pdf/2303.17071.pdf)
6. [MMLU](https://arxiv.org/pdf/2009.03300v3.pdf)
7. [GPT-4 Technical Report](https://arxiv.org/pdf/2303.08774.pdf)
8. [Reflexion Paper](https://arxiv.org/abs/2303.11366)

## Quick Start

Follow these steps to get the project up and running on your local machine.

1. **Clone the Repository**

   Use the following command to clone the repository:
   ```
   git clone https://github.com/kdcokenny/smartgpt_langchain.git
   ```

2. **Install Poetry**

   Poetry is a tool for dependency management and packaging in Python. Use the following command to install poetry:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install Dependencies**

   Once you have installed Poetry, use it to update the project's dependencies with the following command:
   ```
   poetry update
   ```

4. **Enter the Poetry Shell**

   Enter the virtual environment created by Poetry using the following command:
   ```
   poetry shell
   ```

5. **Run the Local Server**

   Now that you have all the dependencies installed and are inside the virtual environment, use the following command to start the local server:
   ```
   python run.py
   ```

6. **Visit the Server**

   Open a new browser on your computer, and navigate to http://localhost:8000 to access the local server.
