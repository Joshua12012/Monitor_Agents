from dotenv import load_dotenv
import httpx, os

load_dotenv()

async def get_health_summary(agent_name: str, status_logs: str) -> str:
    headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}"}
    payload = {
        "model": "groq/compound-mini",
        "messages": [{
            "role": "user",
            "content": f"Agent '{agent_name}' has this status history: {status_logs}. Give a one line health summary."
        }],
        "max_tokens":60
    }
    async with httpx.AsyncClient() as client:
        r = await client.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        return r.json()["choices"][0]["message"]["content"]