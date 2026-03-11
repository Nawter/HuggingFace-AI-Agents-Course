# HuggingFace AI Agents Course

My personal notes, notebooks, and writeups as I work through the [HuggingFace AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction).

---

## What this repo is

This is a learning repo — not a polished library. Every notebook here is me working through the course material hands-on, understanding how LLMs and AI Agents actually work under the hood.

Each unit has a companion post on my Substack where I write a 2,000-word breakdown of what I learned. Links below.

---

## Structure

| File | Description |
|------|-------------|
| `dummy_agent_library.ipynb` | Building a simple agent loop from scratch — no frameworks, just raw LLM calls |
| `smolagents_intro.ipynb` | First steps with HuggingFace's `smolagents` library |

---

## Course Progress

| Unit | Topic | Status | Substack |
|------|-------|--------|----------|
| Unit 1 | What are LLMs? | ✅ Done | [Read →](#) |
| Unit 2 | Coming soon... | 🔄 In progress | — |

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

---

## Course Link

👉 [huggingface.co/learn/agents-course](https://huggingface.co/learn/agents-course/en/unit0/introduction)# HuggingFace-AI-Agents-Course
