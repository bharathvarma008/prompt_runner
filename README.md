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

*Skills Extraction:*

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

*Skill Gap Analysis:*

Prompt:

```
Perform a detailed skill gap analysis between the candidate's resume and the job description. 
        Follow these specific analytical steps:

        1. Skill Extraction and Quantification:
           - From Job Description: List required skills with their relative importance (Scale 1-5)
           - From Resume: List candidate's skills with their apparent proficiency level (Scale 1-5)
           Base these ratings on:
           - Years of experience
           - Project complexity described
           - Leadership/ownership level
           - Specific achievements mentioned

        2. Gap Analysis:
           - Calculate match scores for each skill area
           - Identify missing critical skills (importance ≥4)
           - Note areas where candidate exceeds requirements
           
        3. Recommendations:
           - Prioritize skill gaps by:
             * Importance to role (1-5)
             * Estimated time to acquire
             * Impact on job performance
           - Suggest specific learning paths or certifications

        Format the response as follows:
        
        SKILL REQUIREMENTS ANALYSIS
        [List skills from JD with importance ratings]

        CANDIDATE SKILL ASSESSMENT
        [List candidate's skills with proficiency ratings]

        GAP ANALYSIS
        [Quantified gaps and matches]

        CRITICAL GAPS
        [List of high-priority missing skills]

        RECOMMENDATIONS
        [Prioritized action items]

        Resume text:
        {resume}

        Job Description:
        {jd} 
```

Resume text:

```
John Doe
Software Engineer with 5+ years of experience in big data technologies. 
Proficient in Hadoop, Spark, and Kafka. 
Led a team to develop a data processing pipeline that improved data retrieval times by 30%. 
Experience in designing and implementing scalable data architectures and data models. 
Strong background in Python and Java, with a focus on data analysis and machine learning applications.
```

Job Description: 

```
As a Data Engineer, you will be responsible for designing, building, and maintaining scalable data pipelines and architectures. 
You will work with large datasets to ensure data quality and accessibility for analytics and business intelligence. 
Key responsibilities include developing ETL processes, optimizing data storage solutions, and collaborating with data scientists and analysts to support data-driven decision-making. 
Required skills include proficiency in SQL, Python, and big data technologies such as Apache Spark and Hadoop. Experience with cloud platforms like AWS or Azure is a plus. 
Strong problem-solving skills and the ability to work in a fast-paced environment are essential.
```

Response:

```
Skill Gap Analysis:
SKILL REQUIREMENTS ANALYSIS
- SQL (5)
- Python (4)
- Apache Spark (4)
- Hadoop (4)
- AWS/Azure (3)

CANDIDATE SKILL ASSESSMENT
- SQL: 3
- Python: 5
- Apache Spark: 5
- Hadoop: 5
- AWS/Azure: 0

GAP ANALYSIS
- SQL: Candidate lacks proficiency (Gap: -2)
- Python: Candidate exceeds requirement (Match: +1)
- Apache Spark: Candidate meets requirement (Match: +1)
- Hadoop: Candidate meets requirement (Match: +1)
- AWS/Azure: Candidate lacks proficiency (Gap: -3)

CRITICAL GAPS
- SQL
- AWS/Azure

RECOMMENDATIONS
1. Prioritize learning SQL as it is a critical skill for the role (Importance: 5, Time to acquire: Short, Impact: High)
2. Obtain certification in AWS or Azure to improve proficiency in cloud platforms (Importance: 4, Time to acquire: Medium, Impact: Medium)
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

- Add more prompts for different tasks (e.g. resume summary, cover letter, etc.)
- Add more LLMs to choose from
- Increase informativity of the prompts 

## About Author:

I'm Bharath, a Senior Data Scientist working at [@Starbucks](https://www.starbucks.com/). I'm an AI/ML enthusiast with a passion for building scalable and efficient systems.

You can find me on [LinkedIn](https://www.linkedin.com/in/bharathvarma)