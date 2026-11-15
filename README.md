# WanderWise — Streamlit app

A responsive travel discovery app built with Streamlit.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Publish on Streamlit Community Cloud (free tier availability subject to Streamlit's current terms)
1. Create/sign in to GitHub and create a new **public** repository named `wanderwise`.
2. Upload `app.py`, `requirements.txt`, and this `README.md` to the repository root.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Select **Create app**, choose your repository, branch (`main`), and main file path (`app.py`).
5. Select **Deploy**. Streamlit will build the app and provide a public `*.streamlit.app` URL you can share.

## Notes
- This is a Streamlit app, not a Canva site. It will publish to a Streamlit URL.
- Destination images are loaded from Unsplash and require internet access.
- Prices are illustrative starting estimates and should be verified before commercial use.
- Recommendation matching is a simple sample ruleset; it is not connected to live inventory or booking services.
