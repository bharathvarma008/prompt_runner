# OpenAI Prompt Runner

A simple yet powerful tool to interact with OpenAI's API for various text analysis tasks. I built this to make it easier to analyze resumes, perform skill gap analysis, and handle other text-based tasks consistently.

## What it does

- 📝 Analyzes resumes to extract skills (technical, functional, and soft skills)
- 🎯 Performs detailed skill gap analysis between resumes and job descriptions
- 📊 Generates quantified assessments with actionable recommendations
- 📑 Summarizes text and analyzes sentiment
- 💡 Generates creative ideas on any topic

## Getting Started

1. Clone this repo
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Quick Usage

```bash
python src/main.py
```

This will run the default example of skill gap analysis between a resume and a job description.

## Sample prompt responses

*Skill Gap Analysis:*

Prompt:

```
Please analyze the following resume text and extract three categories of skills:
1. Technical Skills: Hard skills related to specific technologies, tools, or technical knowledge
2. Functional Skills: Job-specific abilities and domain knowledge
3. Soft Skills: Interpersonal and behavioral traits

For each category, provide a comma-separated list of identified skills.
If a category has no identifiable skills, mark it as "None identified".

Resume text:
{resume_text}

Please format the response as follows:
Technical Skills: [list of skills]
Functional Skills: [list of skills]
Soft Skills: [list of skills]
```

Resume text:

```
Led a team of 5 developers to successfully migrate a legacy Java application 
to Python, implementing CI/CD pipelines using Jenkins and Docker. 
Improved system performance by 40% through optimization and reduced deployment 
time by 60%. Conducted weekly team meetings and mentored 2 junior developers.
```

Response:

```
Technical Skills: Java, Python, Jenkins, Docker, CI/CD
Functional Skills: None identified
Soft Skills: Leadership, Mentorship
```


## Customizing the Prompt

The prompt manager is designed to be easily customizable. You can modify the prompts in `src/prompt_manager.py` to suit your specific needs.

## Logging

Logs are stored in the `logs` directory in JSON format with the following information:
- Timestamp
- Log level
- Module
- Message
- Input prompt
- API response

## TODO

- Add more prompts
- Add more LLMs to choose from
- Increase informativity of the prompts 

## About Author:

I'm Senior Data Scientist working at [@Starbucks](https://www.starbucks.com/). I'm an AI/ML enthusiast with a passion for building scalable and efficient systems.

You can find me on [LinkedIn](https://www.linkedin.com/in/bharathvarma)