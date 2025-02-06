#Articulo sobre la eficiencia de la cadena de suministro, recomendaciones para mejorar la eficiencia y reducir costos operacionales.


import asyncio
import os
from shadai.core.session import Session

input_dir = os.path.join(os.path.dirname(__file__), "documents")


async def main():
    async with Session(type="standard", delete_session=True) as session:
        await session.ingest(input_dir=input_dir)
        
        await session.create_article(
            topic="la eficiencia de la cadena de suministro, recomendaciones para mejorar la eficiencia y reducir costos operacionales",
            display_in_console=True,
        )

if __name__ == "__main__":
    asyncio.run(main())