#Extracción de información de pacientes 


import asyncio
import os
from typing import Dict

from shadai.core.agents import ToolAgent
from shadai.core.session import Session

input_dir = os.path.join(os.path.dirname(__file__), "documents")


def get_patient_details(patient_id: str) -> str:
    patients_data = {
    "12345": {
        "age": 30,
        "gender": "Masculino",
        "diagnosis_details": "Hipertensión"
    },
    "67890": {
        "age": 25,
        "gender": "Femenino",
        "diagnosis_details": "Diabetes tipo 1"
    }
    }
    
    # Check if the patient_id exists in the data
    if patient_id not in patients_data:
        return "Paciente no encontrado"
    
    # Extract patient details
    patient = patients_data[patient_id]
    age = patient.get("age", "Edad no disponible")
    gender = patient.get("gender", "Sexo no disponible")
    diagnosis_details = patient.get("diagnosis_details", "Detalles de diagnóstico no disponibles")
    
    # Return formatted patient details
    return f"Edad: {age}\nSexo: {gender}\nDetalles de diagnóstico: {diagnosis_details}"


async def main():
    async with Session(type="standard", delete_session=True) as session:
        await session.ingest(input_dir=input_dir)

        agent = ToolAgent(
            session=session,
            prompt="""
                Analiza la información del paciente y proporciona una descripción detallada de su diagnóstico actual.

                Información del paciente:
                {function_output}
            """,
            use_summary=False,
            function=get_patient_details,
        )

        await agent.call(patient_id="12345")

        await session.query(
            query="¿Tienes información del paciente 12345?", display_in_console=True
        )


if __name__ == "__main__":
    asyncio.run(main())