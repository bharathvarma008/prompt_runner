from typing import Dict, Any
from openai_client import OpenAIClient
from logger import logger

class PromptManager:
    def __init__(self):
        self.client = OpenAIClient()
        logger.info("PromptManager initialized")
        
    def summarize_text(self, text: str) -> str:
        logger.info("Generating text summary", prompt=text)
        prompt = f"Please summarize the following text:\n\n{text}"
        response = self.client.generate_response(prompt)
        logger.info("Generated summary", prompt=text, response=response)
        return response
    
    def analyze_sentiment(self, text: str) -> str:
        logger.info("Analyzing sentiment", prompt=text)
        prompt = f"Analyze the sentiment of the following text:\n\n{text}"
        response = self.client.generate_response(prompt)
        logger.info("Sentiment analysis complete", prompt=text, response=response)
        return response
    
    def generate_ideas(self, topic: str, num_ideas: int = 5) -> str:
        logger.info(f"Generating {num_ideas} ideas", prompt=topic)
        prompt = f"Generate {num_ideas} creative ideas about: {topic}"
        response = self.client.generate_response(prompt)
        logger.info("Ideas generated", prompt=topic, response=response)
        return response
    
    def answer_question(self, question: str) -> str:
        logger.info("Processing question", prompt=question)
        response = self.client.generate_response(question)
        logger.info("Answer generated", prompt=question, response=response)
        return response
    
    def analyze_resume_point(self, resume_text: str) -> str:
        logger.info(
            "Analyzing resume text for skills extraction",
            prompt=resume_text
        )
        
        prompt = """
        Please analyze the following resume text and extract three categories of skills:
        1. Technical Skills: Hard skills related to specific technologies, tools, or technical knowledge
        2. Functional Skills: Job-specific abilities and domain knowledge
        3. Soft Skills: Interpersonal and behavioral traits

        For each category, provide a comma-separated list of identified skills.
        If a category has no identifiable skills, mark it as "None identified".

        Resume text:
        {text}

        Please format the response as follows:
        Technical Skills: [list of skills]
        Functional Skills: [list of skills]
        Soft Skills: [list of skills]
        """.format(text=resume_text)

        try:
            response = self.client.generate_response(
                prompt=prompt,
                temperature=0.3  # Lower temperature for more focused/consistent output
            )
            logger.info(
                "Successfully extracted skills from resume text",
                prompt=resume_text,
                response=response
            )
            return response
        except Exception as e:
            logger.error(
                "Failed to analyze resume text",
                prompt=resume_text,
                response=str(e)
            )
            raise
    
    def analyze_skill_gap(self, resume_text: str, job_description: str) -> str:
        logger.info(
            "Analyzing skill gap between resume and job description",
            prompt=f"Resume: {resume_text}\nJD: {job_description}"
        )
        
        prompt = """
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
        """.format(resume=resume_text, jd=job_description)

        try:
            response = self.client.generate_response(
                prompt=prompt,
                temperature=0.2  # Lower temperature for more analytical/consistent output
            )
            logger.info(
                "Successfully completed skill gap analysis",
                prompt=f"Resume: {resume_text}\nJD: {job_description}",
                response=response
            )
            return response
        except Exception as e:
            logger.error(
                "Failed to complete skill gap analysis",
                prompt=f"Resume: {resume_text}\nJD: {job_description}",
                response=str(e)
            )
            raise 