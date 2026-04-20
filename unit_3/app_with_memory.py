"""
app_with_memory.py - Alfred with conversation memory across turns.

Key difference from app.py:
    alfred.run(query, reset=False)   # <-- reuses previous run's memory

This demonstrates the opt-in memory pattern described in the README:
memory is a separate concern from agent logic — you enable it explicitly.
"""

from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool
from tools import WeatherInfoTool, HubStatsTool
from retriever import load_guest_dataset


def build_agent():
    """Build Alfred with all tools (same as app.py)."""
    model = InferenceClientModel()
    alfred = CodeAgent(
        tools=[
            load_guest_dataset(),
            WeatherInfoTool(),
            HubStatsTool(),
            DuckDuckGoSearchTool(),
        ],
        model=model,
        add_base_tools=True,
        planning_interval=3,
    )
    return alfred


def chat_loop(alfred):
    """Interactive REPL where every turn remembers the previous ones."""
    print("\n🎩 Alfred at your service. Type 'quit' to exit, 'reset' to clear memory.\n")
    first_turn = True
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("Goodbye!")
            break
        if user_input.lower() == "reset":
            first_turn = True
            print("🎩 Memory cleared. Starting fresh.\n")
            continue

        # On the first turn, reset=True (default). On every subsequent turn,
        # reset=False to KEEP the prior conversation in memory.
        response = alfred.run(user_input, reset=first_turn)
        first_turn = False
        print(f"\n🎩 Alfred: {response}\n")


def scripted_demo(alfred):
    """Non-interactive demo showing memory across 3 turns."""
    print("=" * 60)
    print("Scripted Memory Demo")
    print("=" * 60)

    # Turn 1 — fresh start, reset defaults to True
    print("\n--- Turn 1 ---")
    r1 = alfred.run("Tell me about Lady Ada Lovelace.")
    print(f"🎩 Alfred: {r1}\n")

    # Turn 2 — reset=False keeps Turn 1's context
    # "she" refers to Ada Lovelace — only resolvable with memory
    print("--- Turn 2 (memory on) ---")
    r2 = alfred.run("What is her email address?", reset=False)
    print(f"🎩 Alfred: {r2}\n")

    # Turn 3 — still remembers both prior turns
    print("--- Turn 3 (memory on) ---")
    r3 = alfred.run(
        "Suggest one conversation starter based on what you know about her.",
        reset=False,
    )
    print(f"🎩 Alfred: {r3}\n")


def main():
    alfred = build_agent()
    # Run the scripted demo first, then open the interactive chat
    scripted_demo(alfred)
    # Note: the REPL below starts a NEW conversation (reset=True on first turn)
    chat_loop(alfred)


if __name__ == "__main__":
    main()