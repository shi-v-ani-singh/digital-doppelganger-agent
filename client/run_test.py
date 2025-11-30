# import asyncio
# from google.genai import types
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.adk.memory import InMemoryMemoryService
# from config import APP_NAME, USER_ID
# from client.executor_agent import executor_agent

# session_service = InMemorySessionService()
# memory_service = InMemoryMemoryService()

# PERSISTENT_SESSION_ID = "demo_session_persistent"

# runner = Runner(
#     agent=executor_agent,
#     app_name=APP_NAME,
#     session_service=session_service,
#     memory_service=memory_service,
# )

# async def init_session():
#     await session_service.create_session(
#         app_name=APP_NAME,
#         user_id=USER_ID,
#         session_id=PERSISTENT_SESSION_ID
#     )

# async def send_message(user_query: str):
#     test_content = types.Content(parts=[types.Part(text=user_query)])
#     print(f"\n👤 User: {user_query}")
#     print("🤖 Doppelganger Response:\n" + "-"*60)

#     async for event in runner.run_async(
#         user_id=USER_ID,
#         session_id=PERSISTENT_SESSION_ID,
#         new_message=test_content
#     ):
#         if event.is_final_response():
#             if event.content and event.content.parts:
#                 for p in event.content.parts:
#                     if hasattr(p, "text"):
#                         print(p.text)

#     print("-"*60)

# async def main():
#     await init_session()
#     await send_message("Bro coding at 2AM hits different ngl. Remember to drink water.")
#     await send_message("Summarize my previous message in my tone.")
#     await send_message("Write an email about this coding session in my playful style.")

# asyncio.run(main())
import asyncio
import aiohttp

API_URL = "http://127.0.0.1:8001/a2a/execute"


async def send_message(user_query: str):
    print(f"\n👤 User: {user_query}")
    print("🤖 Doppelganger Response:\n" + "-"*60)

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json={"input": user_query}) as res:
            data = await res.json()

            # ADK wraps final output inside "response" or "output"
            text = data.get("response") or data.get("output") or data
            print(text)

    print("-"*60)

async def main():
    await send_message("Bro coding at 2AM hits different ngl. Remember to drink water.")
    await send_message("Summarize my previous message in my tone.")
    await send_message("Write an email about this coding session in my playful style.")

asyncio.run(main())
