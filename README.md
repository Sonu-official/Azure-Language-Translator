## Language Translation using Azure Translator resource
  1. **Directly using any Python Editor**
  2. **With Interface (using streamlit)**


# Directly using any Python Editor
This repository contains a Python script that uses the Azure Translator Text API to translate text from one language to another. It demonstrates how to load environment variables, interact with the Azure Translator API, and perform text translations based on user input.

# Prerequisites
Before running the script, you need to set up your environment and install necessary dependencies.

1. **Create an Azure Translator Resource**

   i. **Create an Azure Account:** If you don’t have an Azure account, you can create one for free here.

   ii. **Create a Translator Resource**:
        a. Go to the Azure Portal.
        b. Click on Create a resource.
        c. Search for Translator and select Translator from the search results.
        d. Click Create.
        Fill in the required details such as Subscription, Resource Group, Region, and Name.
        Click Review + create, and then click Create.
        
   iii. **Get Your API Key and Region:**
        a. Once the resource is created, go to the resource in the Azure portal.
        b. Navigate to the Keys and Endpoint section.
        c. Copy the Key1 and Region values. You will need these to authenticate your API requests. 

2. **Install Python**
    Ensure you have Python 3.6 or later installed on your machine. You can download Python from the official Python website.

3. **Install Required Python Libraries**
   You need to install the azure-ai-translation-text library and python-dotenv for managing environment variables. You can install these libraries using pip.
   
   command : **pip install azure-ai-translation-text python-dotenv**

# Getting Started

1. **Clone the Repository** : Clone this repository to your local machine:
   
   **git clone :** https://github.com/Sonu-official/Azure-Language-Translator
                   cd translation-python-script 
                   
2. **Set Up Environment Variables**
    Create a file named .env in the root directory of the repository. Add the following lines to the .env file, replacing YOUR_KEY and  YOUR_REGION with your Azure Translator API key and region respectively:

    TRANSLATOR_KEY=YOUR_KEY
    TRANSLATOR_REGION=YOUR_REGION 
    
3. **Run the Script**
    The script file is named translate.py. Run the script using Python:

    python translate.py

# Script Explanation

1. **Import Dependencies:** The script imports required libraries for handling environment variables and interacting with the Azure  Translator API.
2. **Load Environment Variables:** The script uses dotenv to load API credentials from the .env file.
3. **Create Translator Client:** Initializes the Azure Translator client using the provided API key and region.
4. **Get Supported Languages:** Fetches and displays a list of languages supported for translation.
5. **User Input:** Prompts the user to enter a target language code and text to translate.
6. **Translate Text:** Translates the provided text to the chosen language and displays the result.

**Example**
  a. When you run the script, it will prompt you to enter a target language code and text. 
  
     For example:
                  **Enter a target language code for translation (for example, 'en') :**
               
  b. Enter a valid language code (e.g., es for Spanish), and then enter text to be translated.

           Enter text to translate ('quit' to exit):
  
  Type the text you want to translate and press Enter. To exit the program, type quit.

**________________________________________________________________________________________________________________________________________________________**

# Azure Translator with Streamlit

This project demonstrates how to build a language translation application using Azure Translator API and Streamlit. You can input text in one language and translate it into another.

## Prerequisites

1. **Azure Subscription**: You need an Azure subscription to access the Azure Translator service. If you don't have one, you can [sign up for a free account here](https://azure.microsoft.com/free/).

2. **Create an Azure Translator Resource**:
   - Go to the [Azure Portal](https://portal.azure.com/).
   - Click on `Create a resource`.
   - Search for `Translator` and select it.
   - Click `Create` and follow the instructions to set up the resource.
   - After creating the resource, note down your `Subscription Key`, `Endpoint`, and `Resource Region`.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository


2. **Install Required Packages**: Ensure you have Python installed. Then, install the required Python packages using pip:
   ```bash
   pip install streamlit requests python-dotenv


3. **Create a .env File:** Create a file named .env in the root directory of the project with the following content:
   ```bash
   AZURE_TRANSLATOR_KEY=your_subscription_key
   AZURE_TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com
   AZURE_TRANSLATOR_REGION=your_resource_region

  Replace your_subscription_key with the key you obtained from Azure, your_resource_region with the region of your Azure resource (e.g., westus), and ensure the endpoint is correct.

**Running the Application**
  1. **Run the Streamlit App:** Execute the following command in your terminal:

     ```bash
     streamlit run translator_app.py

  2.**Access the App:** Once the application is running, it will open in your default web browser. If it does not open automatically, go to http://localhost:8501 in your browser to view the application.


## How It Works

1. **Input Text:** Enter the text you want to translate.
2. **Source Language:** Enter the language code of the text (e.g., `en` for English).
3. **Target Language:** Enter the language code you want to translate the text into (e.g., `es` for Spanish).
4. **Translate:** Click the "Translate" button to see the translated text.

