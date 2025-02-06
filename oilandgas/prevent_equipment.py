#Recomendaciones de mantenimiento preventivo para equipos de petroleo y gas

import asyncio
import os
from typing import Dict

from shadai.core.agents import ToolAgent
from shadai.core.session import Session

input_dir = os.path.join(os.path.dirname(__file__), "documents")


def get_oilandgas_details(oilandgas_id: str) -> str:
    oilandgas_data = {
        "1": {
            "equipment_name": "Bomba de petroleo",
            "equipment_type": "Bomba",
            "maintenance_details": "Lubricar las partes moviles"
        },  
        "2": {
            "equipment_name": "Tuberia de petroleo",
            "equipment_type": "Tuberia",
            "maintenance_details": "Prueba de presion"
        }
        }

    # Check if the patient_id exists in the data
    if oilandgas_id not in oilandgas_data:
        return "Equipo de petroleo y gas no encontrado"
    
    # Extract patient details
    equipment = oilandgas_data[oilandgas_id]
    equipment_name = equipment.get("equipment_name", "Nombre del equipo no disponible")
    equipment_type = equipment.get("equipment_type", "Tipo de equipo no disponible")
    maintenance_details = equipment.get("maintenance_details", "Detalles de mantenimiento no disponibles")
    
    # Return formatted patient details
    return f"Nombre del equipo: {equipment_name}\nTipo de equipo: {equipment_type}\nDetalles de mantenimiento: {maintenance_details}"


async def main():
    async with Session(type="standard", delete_session=True) as session:
        await session.ingest(input_dir=input_dir)

        agent = ToolAgent(
            session=session,
            prompt="""
                Analiza la información del equipo de petroleo y gas y proporciona una descripción detallada de su mantenimiento preventivo.

                Información del equipo de petroleo y gas:
                {function_output}
                
                Recomendaciones extras de mantenimiento preventivo:
                {summary}
            """,
            use_summary=True,
            function=get_oilandgas_details,
        )

        await agent.call(oilandgas_id="1")


if __name__ == "__main__":
    asyncio.run(main())