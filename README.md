# Shadai Project

## Overview

This project utilizes Shadai to provide solutions across multiple industries by leveraging its powerful tools and libraries.

## Industry Use Cases

- **Healthcare**

We have a solution to analyze a patient's historical data and extract the main information.

Steps:

1. We use our ingest agent to put the patient's historical data inside the session.
2. We create a tool to get the patient's historical data.
3. We create a custom agent that use the tool to get the patient's historical data and answer with the actual diagnosis.
4. We use our query agent to get the specific information of the patient's historical data.

- **Logistics**

We have a solution to create an article using the reports of the year from a logistics company.

Steps:

1. We use our ingest agent to put the reports of the year inside the session.
2. We use our create article agent to create the article.

- **Oil and Gas**

We have a solution to analyze a equipment of oil and gas and made recommendations for the maintenance.

Steps:

1. We use our ingest agent to put the equipment of oil and gas inside the session.
2. We create a tool to get the actual status of the equipment of oil and gas.
3. We create a custom agent that use the tool to get the actual status of the equipment of oil and gas and use our summary agent to made recommendations for the maintenance.

- **Finance**

We create a solution to analyze a credit document and extract the main information.

Steps:

1. We use our ingest agent to put the credit document inside the session.
2. We use our summary agent to get the summary of the credit document.
3. We use our query agent to get the specific information of the credit document.

- **Retail**

We have a solution to analyze a catalog of products and extract the main information.

Steps:

1. We use our ingest agent to put the catalog of products inside the session.
2. We create a tool to get the product details using our query agent.
3. We create a custom agent that use the tool to get the product details and answer.

- **Education**

We have a english tutor that can help with the generation of test questions for the students depending on the level of the student and the topic of the test that comes from a book about the topic.

Steps:

1. We use our ingest agent to put the book pdf inside the session.
2. We create a tool to get student level.
3. We create a custom agent that use the tool to get the student level and our summary agent to get the summary of the book to generate the test questions.
4. We call the agent with the specific student id.

- **Marketing**

We have a solution to create a marketing copy for a new product.

Steps:

1. We use our ingest agent to put the product information inside the session.
2. We create a chat session with the agent.
3. We use the chat session to generate the marketing copy doing adjustments until the user is satisfied.

## Demo Video

[Watch the demo video](https://www.loom.com/share/2d8da268f92443fab56b587e0da6c018?sid=49f00f1c-74a5-4ea1-a6a0-7f0b81127589)

These use cases demonstrate Shadai's versatility in addressing industry-specific challenges and enhancing operational efficiency.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/shadai-group/shadai-tutorials.git
   ```

2. Navigate to the project directory:

   ```bash
   cd shadai-tutorials
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the project root directory and add your Shadai API key:

   ```plaintext
   SHADAI_API_KEY=your_api_key_here
   ```

   Obtain your API key from [dashboard.shadai.ai](https://dashboard.shadai.ai).

## Usage

Provide instructions on how to use the project. For example:

- Run the main script of each Use Case:

  ```bash
  python healthcare/historical_pacient_data.py
  ```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b folder/YourUseCase`).
3. Commit your changes (`git commit -m 'Add some use case'`).
4. Push to the branch (`git push origin folder/YourUseCase`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support to implement your own use case, please contact [Angie] at [angie@shadai.ai].
