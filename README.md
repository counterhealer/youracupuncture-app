# 🪡 TCM Acupuncture Study Suite

A local, mobile-optimized Python Streamlit app engineered to study and review acupuncture, cross-reference competing textbooks (e.g. **Chinese Acupuncture & Moxibustion [CAM]**, **Deadman's Manual of Acupuncture**, and **Maciocia's Foundations of Chinese Medicine**), practice interactive multi-source flashcards, and simulate clinical patient encounters with automated textbook-standard grading.

---

## 📁 Project Directory Structure

```text
acupuncture_app/
├── app.py                  # Main mobile-responsive Streamlit interface (single-column, touch-friendly)
├── requirements.txt        # Dependencies (Streamlit, LlamaIndex, ChromaDB, PDF tools)
├── .env.example            # Sample environment file for optional API keys
├── README.md               # Complete setup, usage, and iPhone instructions
├── materials/              # Drop your PDF textbooks and reference notes here
│   ├── CAM_Chinese_Acupuncture_and_Moxibustion.txt
│   ├── Deadman_A_Manual_of_Acupuncture.txt
│   └── Maciocia_The_Foundations_of_Chinese_Medicine.txt
├── data/                   # Persistent vector embeddings and SQLite databases
│   ├── acupuncture.db      # SQLite database for flashcards, Leitner mastery, and case logs
│   ├── vector_store/       # Persistent LlamaIndex vector store (persists across runs)
│   └── indexed_manifest.json # Tracks hashes of processed materials
└── modules/
    ├── __init__.py
    ├── rag_engine.py       # PDF parsing, instant persistence loading, and cross-referencing
    ├── flashcards.py       # Multi-source flashcard generation, Leitner review, and conflict detection
    └── diagnostics.py      # Clinical case study simulator and textbook-based grading engine
```

---

## ⚡ Key Features

1. **Instant Persistent RAG Indexing:**
   - Textbooks in `materials/` are parsed and embedded into persistent storage in `data/vector_store/` once.
   - On subsequent launches, the index loads in milliseconds without re-parsing large PDFs.
2. **Sidebar Dynamic File Uploader:**
   - Drop new PDFs or notes directly into the `st.file_uploader` in the app sidebar.
   - Files are saved to `materials/` and can be indexed immediately with a single click.
3. **Multi-Textbook Synthesis & Conflict Detection:**
   - When textbooks disagree (e.g., ST36 depth: CAM 1.0–2.0 cun vs. Deadman 1.0–1.5 cun; BL1 needling protocols; LI4 pregnancy cautions), the app explicitly detects and highlights the discrepancies in a dedicated callout card.
4. **Interactive Flashcards with Leitner Spaced Repetition:**
   - Generates and reviews flashcards synthesizing consensus and variations.
   - SQLite tracks review counts and mastery levels (`New`, `Learning`, `Reviewing`, `Mastered`).
5. **Clinical Case Simulator & AI Textbook Grading:**
   - Simulates real TCM patient consultations (Chief Complaint, History, and Four Examinations: 望/闻/问/切).
   - Enter your TCM Pattern Diagnosis, Point Prescription, and Rationale.
   - Receives an automated score (0–100%), letter grade, and breakdown against textbook standards.
6. **Mobile-First Responsive Design:**
   - Single-column layout with min-48px touch targets, comfortable typography, and card-based containers specifically styled for mobile Safari and iPhone browsers.

---

## 🚀 Quickstart: Running Locally

### Step 1: Install Python (if not already installed)
Ensure Python 3.10+ is installed on your computer:
```powershell
winget install Python.Python.3.11
```

### Step 2: Set Up Virtual Environment & Dependencies
Open PowerShell or your terminal and navigate to the project:
```powershell
cd d:\TCM\acupuncture_app
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 3: Run the Streamlit App
```powershell
streamlit run app.py
```
The app will open automatically in your browser at `http://localhost:8501`.

---

## 📱 How to Use on Your iPhone

You can easily review your flashcards and clinical cases on your iPhone while on your home Wi-Fi network:

1. **Start Streamlit bound to your local network:**
   ```powershell
   streamlit run app.py --server.address 0.0.0.0
   ```
2. **Find your computer's local IP address:**
   In PowerShell, run:
   ```powershell
   ipconfig
   ```
   Look for the `IPv4 Address` (for example, `192.168.1.75`).
3. **Open Safari on your iPhone:**
   Type: `http://192.168.1.75:8501` (replace with your computer's actual IP).
4. **Add to Home Screen for Full-Screen App Mode:**
   - In Safari, tap the **Share** button (the square with an arrow pointing up).
   - Scroll down and tap **Add to Home Screen**.
   - Tap **Add**. You now have a full-screen, native-feeling acupuncture study app!

---

## ⚙️ AI Models & Offline Mode

- **Google Gemini (Recommended):** Uses Google's fast, high-context `gemini-1.5-flash` or `gemini-1.5-pro` along with `text-embedding-004`. Set `GEMINI_API_KEY` in `.env` or paste it directly in the app sidebar.
- **Offline Mode:** Works 100% out-of-the-box without requiring any API keys or internet connection. Uses the built-in TCM knowledge synthesis engine and SQLite database.
- **OpenAI:** To use `gpt-4o-mini` or `text-embedding-3-small`, either set `OPENAI_API_KEY` in `.env` or input your key directly into the sidebar in the app.
- **Ollama:** To run fully local LLMs (like `llama3` or `qwen2.5`), install Ollama (`https://ollama.ai`), run `ollama run llama3`, and select **Ollama (Local)** in the sidebar.
