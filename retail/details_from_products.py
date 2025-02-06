#Integra conocimiento sobre productos, tendencias de consumo, disponibilidad en inventario y promociones actuales 


import asyncio
import os
from typing import Dict

from shadai.core.agents import ToolAgent
from shadai.core.session import Session

input_dir = os.path.join(os.path.dirname(__file__), "documents")


async def get_product_details(session: Session, product_id: str) -> str:
    return await session.query(
        query=f"Dame los detalles del producto {product_id}", display_in_console=False
    )


async def main():
    async with Session(type="standard", delete_session=True) as session:
        await session.ingest(input_dir=input_dir)

        agent = ToolAgent(
            session=session,
            prompt="""
                You are a retail agent that integrates knowledge about products.
                You are given a product id and you need to provide the details of the product.
                Product Details:
                {function_output}

                You need to answer with a JSON object with the following fields:
                - product_id: The id of the product examples: NC030, HELD04, etc.
                - product_name: The name of the product example: Helix Seed Feeder, The Acom Feeder, Geouhaus Peanut and Sunflower, etc.
                - product_details: The details of the product example: Simple and effective clip opening with an integrated hopper for easy filling, Squirrel resistant, etc.
                - product_size: The size of the product example: 9.4 H x 10.5 dia , 13.2 H x 9.1 W, etc.
            """,
            use_summary=False,
            function=get_product_details,
            is_async_function=True
        )

        await agent.call(session=session, product_id="NC030")


if __name__ == "__main__":
    asyncio.run(main())