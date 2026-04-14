import gradio as gr
import httpx

# CONFIG
BASE_URL = "http://localhost:8000"
API_TOKEN = "mysupersecrettoken123"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Create Agent
def create_agent(name, type_):
    try:
        r = httpx.post(
            f"{BASE_URL}/agents",
            json={"name": name, "type": type_},
            headers=headers
        )
        return r.json()
    except Exception as e:
        return str(e)

# Update Status
def update_status(agent_id, status):
    try:
        r = httpx.patch(
            f"{BASE_URL}/agents/{agent_id}",
            json={"status": status},
            headers=headers
        )
        return r.json()
    except Exception as e:
        return str(e)

# 📋 Get Agents
def get_agents():
    try:
        r = httpx.get(f"{BASE_URL}/agents", headers=headers)
        return r.json()
    except Exception as e:
        return str(e)

# 🎨 UI Layout
with gr.Blocks() as app:
    gr.Markdown("## 🤖 Agent Manager UI")

    with gr.Tab("Create Agent"):
        name = gr.Textbox(label="Agent Name")
        type_ = gr.Textbox(label="Agent Type")
        create_btn = gr.Button("Create")
        create_output = gr.JSON()

        create_btn.click(create_agent, inputs=[name, type_], outputs=create_output)

    with gr.Tab("Update Status"):
        agent_id = gr.Textbox(label="Agent ID (UUID)")
        status = gr.Textbox(label="New Status")
        update_btn = gr.Button("Update")
        update_output = gr.JSON()

        update_btn.click(update_status, inputs=[agent_id, status], outputs=update_output)

    with gr.Tab("View Agents"):
        fetch_btn = gr.Button("Fetch Agents")
        agents_output = gr.JSON()

        fetch_btn.click(get_agents, inputs=[], outputs=agents_output)

# ▶️ Run app
app.launch()