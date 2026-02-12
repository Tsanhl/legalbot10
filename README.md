<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# legalbot10

AI-powered legal research chatbot with RAG (Retrieval-Augmented Generation) using ChromaDB and Gemini.

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/Tsanhl/legalbot10.git
cd legalbot10
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
pip install huggingface_hub   # needed for downloading the index
```

### 3. Download the ChromaDB index

The pre-built vector index (~6 GB) is hosted on Hugging Face at [Agnes999/legalbot10](https://huggingface.co/datasets/Agnes999/legalbot10).

**Option A — Run the download script (recommended):**

```bash
python download_index.py
```

**Option B — Manual download via CLI:**

```bash
huggingface-cli download Agnes999/legalbot10 --repo-type=dataset --include "chroma_db/*" --local-dir .
```

### 4. Set your Gemini API key

Edit `.env.local` and replace the placeholder:

```
GEMINI_API_KEY=your_actual_key_here
```

### 5. Run the app

```bash
streamlit run streamlit_app.py
```

## Project Structure

| File / Folder | Description |
|---|---|
| `streamlit_app.py` | Main Streamlit UI |
| `gemini_service.py` | Gemini API integration and prompt engineering |
| `rag_service.py` | ChromaDB RAG service with hybrid search |
| `knowledge_base.py` | Knowledge base utilities |
| `chroma_db/` | Vector index (downloaded from Hugging Face, git-ignored) |
| `download_index.py` | Script to download the index from Hugging Face |
| `requirements.txt` | Python dependencies |
