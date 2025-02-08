#Resumen de un documento de credito


import asyncio
import os

from shadai.core.session import Session
from shadai.core.agents import ToolAgent

input_dir = os.path.join(os.path.dirname(__file__), "documents")


def generate_test(student_id: str) -> str:
    
    student_data = [{
        "student_id": "12345",
        "age": 10,
        "level": "Beginner",
        "language": "English"
    },
    {
        "student_id": "67890",
        "age": 12,
        "level": "Intermediate",
        "language": "English"
    }]
    # Extract patient details
    for student in student_data:
        if student["student_id"] == student_id:
            age = student.get("age", "Edad no disponible")
            level = student.get("level", "Nivel no disponible")
            language = student.get("language", "Idioma no disponible")
            break
    # Return formatted patient details
    return f"Edad: {age}\nNivel: {level}\nIdioma: {language}"



async def main():
    async with Session(type="standard", delete_session=True) as session:
        await session.ingest(input_dir=input_dir)

        agent = ToolAgent(
            session=session,
            prompt="""
                Genera un test de inglés para el estudiante usando la siguiente información:

                Información del estudiante:
                {function_output}
                
                Información para hacer el test:
                {summary}
            """,
            use_summary=True,
            function=generate_test,
        )
        await agent.call(student_id="12345")



if __name__ == "__main__":
    asyncio.run(main())