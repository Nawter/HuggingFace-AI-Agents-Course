# Alfred's Gala Agent — Agentic RAG with smolagents

From [HuggingFace Agents Course, Unit 3](https://huggingface.co/learn/agents-course/unit3/agentic-rag/introduction).

## Project Structure

| File | Purpose |
|---|---|
| `retriever.py` | RAG tool — loads guest dataset, BM25 retrieval |
| `tools.py` | DuckDuckGo search, Weather info, HF Hub stats tools |
| `app.py` | Assembles all tools into Alfred (stateless version) |
| `app_with_memory.py` | Multi-turn conversation with memory across runs |
| `guest_data.json` | Local fallback guest dataset (10 guests) |
| `requirements.txt` | Python dependencies |

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py                # single-turn examples
python app_with_memory.py    # multi-turn conversation with memory
```

---

## Design Decision 1 — Why we added a local `guest_data.json` file

The original course tutorial loads the guest list from the HuggingFace Hub:

```python
guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
```

This works only when:
1. The machine has internet access to `huggingface.co`
2. The `datasets` library is configured with credentials
3. HuggingFace Hub is up and the dataset is accessible

**Why the JSON fallback matters:**

| Concern | Without JSON fallback | With JSON fallback |
|---|---|---|
| **Offline development** | Blocked — tutorial won't run | Works fine |
| **Restricted networks** (corporate / sandbox) | Blocked | Works fine |
| **Reproducibility** | Breaks if dataset changes upstream | Pinned, version-controlled |
| **Testing / CI** | Requires HF auth + network | Self-contained |
| **Learning** | Hidden schema — you can't see the data | Open file you can read and edit |

The `retriever.py` tries HuggingFace Hub first, then falls back to the local JSON:

```python
try:
    guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
except Exception:
    with open("guest_data.json") as f:
        guests = json.load(f)
```

**Schema matches exactly** (`name`, `relation`, `description`, `email`) — so the rest of the pipeline is identical whichever source loads. This is a production pattern: always have a local fallback for your source-of-truth data, and ensure both paths produce the same shape.

---

## Design Decision 2 — Why memory is NOT coupled to the agent by default

The course deliberately leaves memory out of the default agent definition. From the tutorial:

> *"None of these three agent approaches directly couple memory with the agent. Is there a specific reason for this design choice?"*

**Yes. Four reasons:**

### 1. Predictability and reproducibility
An agent is a *reasoning engine*. Calling `agent.run("Tell me about X")` should produce the same behavior every time. If memory were implicit, two identical calls could return different answers depending on past interactions — a debugging nightmare. Making memory opt-in via `reset=False` forces the developer to be explicit about state.

### 2. Multi-user safety
One agent instance often serves many users in production (a web API, a Slack bot, a gala chatbot). If memory were baked in globally, **user A's context would leak into user B's session** — a privacy bug waiting to happen. Decoupling forces you to scope memory per user/session.

### 3. Cost control
Every turn of a conversation grows the prompt. On turn 10, you're paying to send turns 1–9 as context. Making memory explicit forces the developer to think: *Do I really need all prior turns? Should I summarize? Should I reset?* Hidden memory = runaway token bills.

### 4. Flexibility — memory has many flavors
"Memory" isn't one thing:
- Short-term (last few turns in a prompt)
- Long-term (summarized user profile)
- Episodic (per-session)
- Semantic (RAG over past conversations)

Frameworks decouple memory from agent logic so you can plug in whichever flavor fits. Coupling them would force one pattern on everyone.

**How each framework handles it:**

| Framework | Memory mechanism |
|---|---|
| **smolagents** | `agent.run(query, reset=False)` — reuses the previous run's memory steps |
| **LlamaIndex** | Pass a `Context` object into `.run(query, ctx=ctx)` |
| **LangGraph** | Accumulate messages in state, or use a `MemorySaver` component |

**Key takeaway:** in smolagents, `reset=False` is the memory switch. See `app_with_memory.py` for a working multi-turn example.

---

## Tools Available to Alfred

| Tool | Description |
|---|---|
| `guest_info_retriever` | BM25 search over guest dataset |
| `weather_info` | Dummy weather for any location |
| `hub_stats` | Most downloaded HF model by author |
| `web_search` | DuckDuckGo web search |
| `visit_webpage` | Fetch webpage content (base tool) |
| `final_answer` | Return final answer (base tool) |