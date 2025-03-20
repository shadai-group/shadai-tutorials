#Multi turn chat with the agent

import asyncio
import os
from shadai.core.session import Session

input_dir = os.path.join(os.path.dirname(__file__), "documents")

agent_copy_prompt = """
You are a helpful assistant that can hep to refine marketing copy.
"""

async def main():
    async with Session(type="standard", delete_session=True) as session:
        await session.ingest(input_dir=input_dir)
        
        # Initial greeting
        await session.chat(
            message="I need to write a marketing copy for a new product. Can you help me?",
            system_prompt=agent_copy_prompt,
            display_in_console=True,
        )
        
        # Interactive chat loop
        print("\n--- Type 'exit' or 'quit' to end the conversation ---")
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation.")
                break  
            response = await session.chat(
                message=user_input,
                system_prompt=agent_copy_prompt,
                display_in_console=False,
            )
            print(f"\nAssistant: {response}")
if __name__ == "__main__":
    asyncio.run(main())