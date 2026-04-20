"""
app.py - Alfred's Gala Agent (smolagents)
Combines guest RAG retriever, web search, weather, and Hub stats
into a single CodeAgent for hosting the most extravagant gala.
"""

from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool
from tools import WeatherInfoTool, HubStatsTool
from retriever import load_guest_dataset


def build_agent():
    """Build and return Alfred, the gala agent with all tools."""
    # Initialize the model (uses HF Inference API by default)
    model = InferenceClientModel()

    # Initialize tools
    search_tool = DuckDuckGoSearchTool()
    weather_info_tool = WeatherInfoTool()
    hub_stats_tool = HubStatsTool()
    guest_info_tool = load_guest_dataset()

    # Create Alfred with all tools
    alfred = CodeAgent(
        tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool],
        model=model,
        add_base_tools=True,
        planning_interval=3,
    )
    return alfred


def main():
    import os
    from dotenv import load_dotenv
    from huggingface_hub import login, whoami

    load_dotenv(dotenv_path="../.env", override=True)
    token = os.environ.get("HF_TOKEN")

    # Validate before logging in
    try:
        login(token=token, add_to_git_credential=False)
        user = whoami()
        print(f"✅ Logged in as: {user['name']}")
    except Exception as e:
        print(f"❌ Login failed: {e}")

    alfred = build_agent()

    # --- Example 1: Guest Information ---
    print("=" * 60)
    print("Example 1: Finding Guest Information")
    print("=" * 60)
    response = alfred.run("Tell me about 'Lady Ada Lovelace'")
    print("🎩 Alfred's Response:")
    print(response)

    # --- Example 2: Weather for Fireworks ---
    print("\n" + "=" * 60)
    print("Example 2: Checking the Weather for Fireworks")
    print("=" * 60)
    response = alfred.run(
        "What's the weather like in Paris tonight? Will it be suitable for our fireworks display?"
    )
    print("🎩 Alfred's Response:")
    print(response)

    # --- Example 3: Impressing AI Researchers ---
    print("\n" + "=" * 60)
    print("Example 3: Impressing AI Researchers")
    print("=" * 60)
    response = alfred.run(
        "One of our guests is from Qwen. What can you tell me about their most popular model?"
    )
    print("🎩 Alfred's Response:")
    print(response)

    # --- Example 4: Combining Multiple Tools ---
    print("\n" + "=" * 60)
    print("Example 4: Combining Multiple Tools")
    print("=" * 60)
    response = alfred.run(
        "I need to speak with Dr. Nikola Tesla about recent advancements in wireless energy. "
        "Can you help me prepare for this conversation?"
    )
    print("🎩 Alfred's Response:")
    print(response)

    # --- Example 5: Conversation Memory ---
    print("\n" + "=" * 60)
    print("Example 5: Conversation Memory (reset=False)")
    print("=" * 60)
    response1 = alfred.run("Tell me about Lady Ada Lovelace.")
    print("🎩 Alfred's First Response:")
    print(response1)

    response2 = alfred.run("What projects is she currently working on?", reset=False)
    print("🎩 Alfred's Second Response:")
    print(response2)


if __name__ == "__main__":
    main()
