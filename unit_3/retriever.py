"""
retriever.py - Guest Information Retriever Tool for Alfred's Gala
Implements the RAG component using BM25 retrieval over the guest dataset.
"""

import json
import os
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from smolagents import Tool


class GuestInfoRetrieverTool(Tool):
    """Retrieves detailed information about gala guests based on their name or relation."""

    name = "guest_info_retriever"
    description = "Retrieves detailed information about gala guests based on their name or relation."
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest you want information about."
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(docs, k=3)
        self.is_initialized = True

    def forward(self, query: str) -> str:
        results = self.retriever.invoke(query)
        if results:
            return "\n\n".join([doc.page_content for doc in results[:3]])
        else:
            return "No matching guest information found."


def load_guest_dataset():
    """Load guest data and return an initialized GuestInfoRetrieverTool.

    Tries to load from HuggingFace Hub first, falls back to local JSON.
    """
    docs = []

    try:
        import datasets
        guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
        docs = [
            Document(
                page_content="\n".join([
                    f"Name: {guest['name']}",
                    f"Relation: {guest['relation']}",
                    f"Description: {guest['description']}",
                    f"Email: {guest['email']}"
                ]),
                metadata={"name": guest["name"]}
            )
            for guest in guest_dataset
        ]
        print(f"Loaded {len(docs)} guests from HuggingFace Hub")
    except Exception as e:
        print(f"HuggingFace Hub unavailable ({e}), loading from local JSON...")
        local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guest_data.json")
        with open(local_path, "r") as f:
            guests = json.load(f)
        docs = [
            Document(
                page_content="\n".join([
                    f"Name: {guest['name']}",
                    f"Relation: {guest['relation']}",
                    f"Description: {guest['description']}",
                    f"Email: {guest['email']}"
                ]),
                metadata={"name": guest["name"]}
            )
            for guest in guests
        ]
        print(f"Loaded {len(docs)} guests from local JSON")

    return GuestInfoRetrieverTool(docs)


if __name__ == "__main__":
    # Quick test
    tool = load_guest_dataset()
    print("\n--- Test: 'Lady Ada Lovelace' ---")
    result = tool.forward("Lady Ada Lovelace")
    print(result)
    print("\n--- Test: 'scientist' ---")
    result = tool.forward("scientist")
    print(result)
