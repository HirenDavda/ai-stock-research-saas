# Active Task

Current Work:

Fix runtime errors during vector database migration from MongoDB Atlas to ChromaDB.

Focus:

- ✅ Stabilize `ai-service/scripts/test_search.py` execution (now passes)
- ✅ Resolve import and module path errors in `ai-service/scripts/test_*.py` (added minimal `sys.path` bootstrap where missing)
- ✅ Ensure local ChromaDB search works end-to-end via:
  - `ai-service/scripts/test_vector_store.py` (insert)
  - `ai-service/scripts/test_search.py` (query)
- Next blocker: **API service end-to-end run depends on correct Python environment**
  - Current error when importing `ai-service/main.py`: `ModuleNotFoundError: fastapi`
  - Fix: create/activate venv and `pip install -r ai-service/requirements.txt`
- Maintain compatibility for future MongoDB Atlas migration

Rule:

Fix current error only.
No refactor.
No redesign.
No function changes.