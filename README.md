# HuggingFace AI Agents Course

My personal notes, notebooks, and writeups as I work through the [HuggingFace AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction).

---

## What this repo is

This is a learning repo — not a polished library. Every notebook here is me working through the course material hands-on, understanding how LLMs and AI Agents actually work under the hood.

---

## Structure

```
HuggingFace-AI-Agents-Course/
├── unit_1/                         # What are LLMs?
│   ├── dummy_agent_library.ipynb   # Building a simple agent loop from scratch — no frameworks
│   └── smolagents_intro.ipynb      # First steps with HuggingFace's smolagents library
│
├── unit_2.1/                       # Smolagents — Tools, Code Agents, Multi-Agent Systems
│   ├── tools.ipynb                 # Defining and using tools in smolagents
│   ├── tool_calling_agents.ipynb   # Tool-calling agents — how agents select and invoke tools
│   ├── code_agents.ipynb           # Code agents — agents that write and execute Python code
│   ├── retrieval_agents.ipynb      # Retrieval-augmented agents with vector search
│   ├── multi_agent_systems.ipynb   # Multi-agent systems — orchestrator and sub-agent patterns
│   ├── vision_agents.ipynb         # Vision agents — agents that process images
│   ├── vision_web_browser.py       # Vision-based web browser agent script
│   ├── batman_supercar_locations.csv
│   └── batman_supercar_report.csv
│
├── unit_2.2/                       # LlamaIndex — Agents, Workflows, and MCP
│   ├── llamaindex_hello_world.ipynb # Getting started with LlamaIndex
│   ├── components.ipynb            # LlamaIndex core components
│   ├── tools.ipynb                 # Tools in LlamaIndex
│   ├── agents.ipynb                # Building agents with LlamaIndex
│   ├── workflows.ipynb             # Agentic workflows in LlamaIndex
│   ├── simple_mcp_server.py        # Simple MCP server implementation
│   ├── workflow_all_flows.html     # Workflow visualization output
│   ├── data/                       # Sample data for exercises
│   └── lib/                        # Supporting library code
│
└── unit_2.3/                       # LangGraph — Building Stateful Agents
    ├── building_blocks.ipynb       # LangGraph core building blocks
    ├── first_graph.ipynb           # Building a first graph with LangGraph
    ├── agent.ipynb                 # Full ReAct agent — vision + tool use with LangGraph
    └── Batman_training_and_meals.png  # Sample document used in agent.ipynb
```

---

## Course Progress

| Unit | Topic | Status |
|------|-------|--------|
| Unit 1 | What are LLMs? | Done |
| Unit 2.1 | Smolagents — Tools, Code Agents, Multi-Agent Systems | Done |
| Unit 2.2 | LlamaIndex — Agents, Workflows, and MCP | Done |
| Unit 2.3 | LangGraph — Building Stateful Agents | Done |

---

## Key Concepts Covered (Unit 2.3)

- LangGraph core primitives: nodes, edges, and state graphs
- Building stateful, cycle-capable agent graphs
- Conditional routing and branching in graphs
- `AgentState` with `TypedDict` — carrying messages and file paths across nodes
- `add_messages` operator — appends to message history instead of overwriting
- Binding tools to LLMs with `bind_tools` and `parallel_tool_calls=False`
- `tools_condition` — conditional edge that routes on whether a tool was called
- Full ReAct loop: `assistant → tools → assistant` until no tool call is made
- Vision tool using `claude-sonnet-4-6` — reading images as base64 for text extraction
- Async invocation (`ainvoke`) to avoid event loop conflicts in Jupyter

---

## Key Concepts Covered (Unit 2.2)

- LlamaIndex core components: documents, nodes, indices, and query engines
- Defining and using tools within LlamaIndex agents
- Building agentic workflows with event-driven steps
- MCP (Model Context Protocol) — building a simple MCP server

---

## Key Concepts Covered (Unit 2.1)

- Defining custom tools with `@tool` decorator in smolagents
- Tool-calling agents vs. code agents (CodeAgent writes Python, ToolCallingAgent calls JSON)
- Retrieval-augmented agents using vector stores for long-term memory
- Multi-agent orchestration — manager agent delegating to specialist sub-agents
- Vision agents and multimodal inputs
- Building a vision-based web browser agent

---

## Key Concepts Covered (Unit 1)

- What LLMs are and how they work (next-token prediction)
- The 3 types of Transformer architectures: Encoders, Decoders, Seq2Seq
- Tokenization and special tokens
- How prompting steers generation
- How LLMs serve as the "brain" of an AI Agent

---

## Requirements

To run the notebooks you'll need:

- A [HuggingFace token](https://hf.co/settings/tokens)
- Access to Meta Llama models (request via HuggingFace Hub)
- Python 3.9+

```bash
pip install transformers smolagents huggingface_hub
```
