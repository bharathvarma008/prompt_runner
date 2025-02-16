from prompt_manager import PromptManager

def main():
    manager = PromptManager()
    
    # Example usage
    try:
        # Example of resume point analysis
        resume_point = """
        Led a team of 5 developers to successfully migrate a legacy Java application 
        to Python, implementing CI/CD pipelines using Jenkins and Docker. 
        Improved system performance by 40% through optimization and reduced deployment 
        time by 60%. Conducted weekly team meetings and mentored 2 junior developers.
        """
        
        skills_analysis = manager.analyze_resume_point(resume_point)
        print("\nSkills Analysis:")
        print(skills_analysis)
        
        resume = """John Doe
        Software Engineer with 5+ years of experience in big data technologies. 
        Proficient in Hadoop, Spark, and Kafka. 
        Led a team to develop a data processing pipeline that improved data retrieval times by 30%. 
        Experience in designing and implementing scalable data architectures and data models. 
        Strong background in Python and Java, with a focus on data analysis and machine learning applications.
        """
        job_description = """As a Data Engineer, you will be responsible for designing, building, and maintaining scalable data pipelines and architectures. 
        You will work with large datasets to ensure data quality and accessibility for analytics and business intelligence. 
        Key responsibilities include developing ETL processes, optimizing data storage solutions, and collaborating with data scientists and analysts to support data-driven decision-making. 
        Required skills include proficiency in SQL, Python, and big data technologies such as Apache Spark and Hadoop. Experience with cloud platforms like AWS or Azure is a plus. 
        Strong problem-solving skills and the ability to work in a fast-paced environment are essential."""
        result = manager.analyze_skill_gap(resume, job_description)
        print("\nSkill Gap Analysis:")
        print(result)

        # Example 1: Summarize text
        # text_to_summarize = """
        # Artificial intelligence (AI) is intelligence demonstrated by machines, 
        # as opposed to natural intelligence displayed by animals including humans. 
        # AI research has been defined as the field of study of intelligent agents, 
        # which refers to any system that perceives its environment and takes actions 
        # that maximize its chance of achieving its goals.
        # """
        # summary = manager.summarize_text(text_to_summarize)
        # print("Summary:", summary)
        
        # # Example 2: Generate ideas
        # ideas = manager.generate_ideas("sustainable energy solutions")
        # print("\nIdeas:", ideas)
        
        # # Example 3: Answer a question
        # answer = manager.answer_question("What are the main principles of machine learning?")
        # print("\nAnswer:", answer)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 