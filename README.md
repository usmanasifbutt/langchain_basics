# LangChain Basics

A collection of LangChain examples covering chat models, streaming responses,
retrieval-augmented generation (RAG), agents, tools, schemas, and MCP
integration.

## Company policy assistant

The main application is a Streamlit RAG assistant in
[`chat/rag.py`](chat/rag.py). It answers employee questions using uploaded
company onboarding and policy documents:

1. PDF files are loaded with `PyPDFLoader`.
2. Documents are split into smaller chunks.
3. Chunks are stored in a local Chroma database under `knowledgebase/`.
4. Relevant chunks are retrieved for each question.
5. `gpt-4.1-mini` generates an answer based only on the retrieved content.

If the uploaded documents do not contain an answer, the assistant is instructed
to say that there is not enough information rather than make assumptions.

## Requirements

- Python 3.14 or newer
- An OpenAI API key
- `uv` recommended for environment and dependency management

## Setup

From the project root:

```powershell
uv sync
```

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not commit `.env` or expose the API key in source control.

## Run the policy assistant

```powershell
uv run streamlit run chat/rag.py
```

Use the sidebar to upload PDF policy documents, then ask questions in the main
form. The local Chroma database is created and updated in `knowledgebase/`.

## Repository layout

| Path | Purpose |
| --- | --- |
| `chat/rag.py` | Company policy RAG assistant |
| `chat/stream.py` | Streaming chat example |
| `chat/multimodel_input.py` | Multi-modal model input example |
| `agents/` | Agent examples, including memory and MCP usage |
| `tools/` | Reusable tool definitions |
| `schemas/` | Structured data schemas |
| `mcp/` | MCP server example |
| `responses/` | Example response files |
| `knowledgebase/` | Local Chroma persistence directory |
| `pyproject.toml` | Project metadata and dependencies |

## Notes

- Add only trusted internal documents to the policy knowledge base.
- The assistant does not provide authoritative legal, HR, or compliance advice.
- Uploaded PDFs are temporarily written to `temp/` while they are processed.
