# Resumen de un documento de credito


import asyncio
import os

from shadai.core.session import Session

input_dir = os.path.join(os.path.dirname(__file__), "documents")


async def main():
    async with Session(type="light", delete=True) as session:
        await session.aingest(input_dir=input_dir)

        await session.aquery(
            query="¿Cual es el monto del producto de credito?", display_in_console=True
        )

        await session.asummarize(display_in_console=True)


if __name__ == "__main__":
    asyncio.run(main())
