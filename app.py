import streamlit as st

st.set_page_config(
    page_title="WanderWise | Discover your next adventure",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DESTINATIONS = [
    {"name":"Ooty","state":"Tamil Nadu","category":"Hill Stations","price":9000,
     "tags":"ooty tamil nadu hills tea gardens nature",
     "description":"Tea gardens, botanical gardens and mountain railway.",
     "image":"https://images.unsplash.com/photo-1597074866923-dc0589150358?auto=format&fit=crop&w=1000&q=85",
     "guide":"Escape to the Nilgiri hills for cool weather, tea gardens, scenic viewpoints and the heritage mountain railway."},
    {"name":"Munnar","state":"Kerala","category":"Hill Stations","price":11000,
     "tags":"munnar kerala hills tea estates nature",
     "description":"Rolling tea estates and cloud-kissed mountain views.",
     "image":"https://images.unsplash.com/photo-1566837497312-7be4a5e2e3a1?auto=format&fit=crop&w=1000&q=85",
     "guide":"Explore Kerala’s highlands, rolling tea plantations, waterfalls and peaceful mountain roads."},
    {"name":"Hampi","state":"Karnataka","category":"Historical Places","price":9000,
     "tags":"hampi karnataka history ruins culture",
     "description":"Boulder-strewn landscapes and majestic ancient ruins.",
     "image":"https://images.unsplash.com/photo-1600100397608-f010a6b2a3b4?auto=format&fit=crop&w=1000&q=85",
     "guide":"Step into the Vijayanagara era among monumental temples, stone chariots and striking boulder landscapes."},
    {"name":"Goa","state":"Goa","category":"Beaches","price":14000,
     "tags":"goa beaches coast relaxation",
     "description":"Golden beaches, coastal cafes and laid-back days.",
     "image":"https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1000&q=85",
     "guide":"Enjoy sunlit beaches, Portuguese-era lanes, local seafood and relaxed coastal escapes."},
    {"name":"Jaipur","state":"Rajasthan","category":"Historical Places","price":12000,
     "tags":"jaipur rajasthan history culture forts",
     "description":"The Pink City of palaces, forts and colorful bazaars.",
     "image":"https://images.unsplash.com/photo-1603262110263-fb0112e7cc33?auto=format&fit=crop&w=1000&q=85",
     "guide":"Discover Rajasthan’s royal heritage through forts, palaces, colorful markets and traditional crafts."},
    {"name":"Kodaikanal","state":"Tamil Nadu","category":"Hill Stations","price":9500,
     "tags":"kodaikanal tamil nadu hills lakes nature",
     "description":"Misty hills, lakeside walks and peaceful pine forests.",
     "image":"https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1000&q=85",
     "guide":"Slow down among misty viewpoints, forest trails, a peaceful lake and pine-covered hills."},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700;800&display=swap');
:root{--navy:#082a45;--blue:#0788cf;--muted:#7890a2}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
.stApp{background:#f5f9fb;color:#0b2b46}
header[data-testid="stHeader"]{background:rgba(8,42,69,.97)}
.block-container{max-width:1180px;padding-top:1.2rem;padding-bottom:2rem}
.brand{font-size:1.45rem;font-weight:800;color:#fff;letter-spacing:-.5px}
.brand-mark{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:11px;background:linear-gradient(135deg,#28c5f4,#0879cb);margin-right:9px}
.hero{padding:4.2rem 3rem 3rem;border-radius:20px;min-height:390px;color:#fff;background:linear-gradient(90deg,rgba(3,30,52,.94),rgba(6,43,70,.60)),url('https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=2200&q=90') center/cover}
.eyebrow{font-size:.72rem;letter-spacing:2px;font-weight:800;color:#078dcc;margin-bottom:.5rem}
.hero .eyebrow{color:#57d4ff}
.hero h1{font-family:'Playfair Display',serif;font-size:clamp(2.7rem,6vw,4.4rem);line-height:1.05;color:white;margin:.5rem 0 1rem}
.hero p{color:#e0edf4;font-size:1rem}
h2{font-family:'Playfair Display',serif!important;color:#0b2b46!important;font-size:2.15rem!important}
.destination-card{background:white;border-radius:16px;overflow:hidden;box-shadow:0 9px 24px rgba(11,56,80,.08);margin-bottom:1.2rem;height:100%}
.destination-card img{width:100%;height:180px;object-fit:cover;display:block}
.destination-content{padding:15px 16px 17px}
.destination-content h3{font-size:1.12rem;margin:0;color:#102f4b}
.pill{display:inline-block;background:#e8f6ff;color:#1689c7;padding:4px 9px;border-radius:30px;font-size:.68rem;font-weight:800}
.subtle{color:#8197a8;font-size:.8rem}
.desc{color:#71899b;font-size:.84rem;min-height:42px}
.price{font-weight:800;color:#14344f}
div.stButton>button{border-radius:10px;border:0;background:linear-gradient(105deg,#20b9ec,#0879ca);color:white;font-weight:700}
div.stButton>button:hover{border:0;color:white;background:#0879ca}
section[data-testid="stSidebar"]{background:#082a45}
section[data-testid="stSidebar"] *{color:white}
.callout{background:linear-gradient(110deg,#e4f6fd,#f6fbfd);padding:1.5rem 1.8rem;border-radius:16px}
.footer{background:#061f34;color:#d5e4ed;padding:1.5rem;border-radius:14px;margin-top:2rem}
.footer p{margin:.2rem 0;color:#b7cbd8}
hr{border-color:#e2edf3}
@media(max-width:700px){.hero{padding:2.2rem 1.2rem;min-height:360px}.hero h1{font-size:2.8rem}.block-container{padding-left:1rem;padding-right:1rem}h2{font-size:1.8rem!important}}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="brand"><span class="brand-mark">✦</span>WanderWise</div>', unsafe_allow_html=True)
    st.markdown("### Explore")
    page = st.radio("Navigate", ["Home", "Destinations", "Recommendations"], label_visibility="collapsed")
    st.markdown("---")
    st.caption("Discover more. Travel further.")

st.markdown('<div class="brand"><span class="brand-mark">✦</span>WanderWise</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
  <div class="eyebrow">✦ &nbsp; YOUR JOURNEY BEGINS HERE</div>
  <h1>Discover Your<br>Next Adventure.</h1>
  <p>From misty mountains to sun-kissed shores, discover remarkable<br> places across India and find a trip that feels made for you.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
nav1, nav2, nav3 = st.columns([1,1,1])
with nav1:
    if st.button("Explore Destinations", use_container_width=True):
        st.session_state["show_destinations"] = True
with nav2:
    if st.button("Find My Match", use_container_width=True):
        st.session_state["show_recommendations"] = True
with nav3:
    st.markdown("")

st.write("")
st.markdown('<p class="eyebrow">HANDPICKED FOR YOU</p><h2>Featured Destinations</h2><p class="subtle">Extraordinary places worth putting on your map.</p>', unsafe_allow_html=True)
query = st.text_input("Search destinations, states, or experiences", placeholder="Try Ooty, beaches, hills, history…")
filtered = [d for d in DESTINATIONS if not query or query.lower() in (d["name"]+" "+d["state"]+" "+d["category"]+" "+d["tags"]+" "+d["description"]).lower()]
if not filtered:
    st.info("No destinations matched. Try “hills”, “beaches”, or “history”.")
else:
    # Display all matching destinations in responsive Streamlit columns.
    for start in range(0, len(filtered), 3):
        cols = st.columns(3, gap="large")
        for col, d in zip(cols, filtered[start:start+3]):
            with col:
                st.markdown(f"""
                <div class="destination-card">
                  <img src="{d['image']}" alt="{d['name']} destination">
                  <div class="destination-content">
                    <div style="display:flex;justify-content:space-between;gap:8px;align-items:center">
                      <h3>{d['name']}</h3><span class="pill">{d['category']}</span>
                    </div>
                    <p class="subtle">⌖ {d['state']}</p>
                    <p class="desc">{d['description']}</p>
                    <p class="price">From ₹{d['price']:,} <span class="subtle">/ person</span></p>
                  </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"View {d['name']} guide →", key=f"guide_{d['name']}", use_container_width=True):
                    st.session_state["selected_guide"] = d["name"]
if st.session_state.get("selected_guide"):
    selected = next(d for d in DESTINATIONS if d["name"] == st.session_state["selected_guide"])
    with st.expander(f"{selected['name']} — destination guide", expanded=True):
        st.write(selected["guide"])
        st.caption(f"Illustrative starting price: ₹{selected['price']:,} per person. Confirm costs before booking.")

st.write("")
st.markdown('<div class="callout"><p class="eyebrow">SMARTER JOURNEYS</p><h2>Find a destination that fits your story.</h2><p class="subtle">Explore places by your preferred travel style and budget. Choose your preferences below to get a destination idea.</p></div>', unsafe_allow_html=True)
c1,c2 = st.columns(2)
with c1:
    mood = st.selectbox("What sounds best?", ["Mountains & nature","Beaches & relaxation","History & culture","A little bit of everything"])
with c2:
    budget_label = st.selectbox("Budget per person", ["Under ₹10,000","₹10,000 – ₹15,000","₹15,000 – ₹25,000","₹25,000+"])
budget_limit = {"Under ₹10,000":10000,"₹10,000 – ₹15,000":15000,"₹15,000 – ₹25,000":25000,"₹25,000+":100000}[budget_label]
mood_cats = {"Mountains & nature":["Hill Stations"],"Beaches & relaxation":["Beaches"],"History & culture":["Historical Places"],"A little bit of everything":["Hill Stations","Beaches","Historical Places"]}
matches = [d for d in DESTINATIONS if d["category"] in mood_cats[mood] and d["price"] <= budget_limit]
if st.button("Find My Destination →", use_container_width=True):
    if matches:
        names = ", ".join(d["name"] for d in matches[:3])
        st.success(f"Destination ideas for your trip: {names}. Prices are illustrative starting estimates per person.")
    else:
        st.warning("No exact match in this sample set. Try a higher budget or another travel style.")

st.markdown("""
<div class="footer">
  <div class="brand"><span class="brand-mark">✦</span>WanderWise</div>
  <p><b>Discover more. Travel further.</b></p>
  <p>Your travel companion for discovering India’s most breathtaking destinations.</p>
  <p style="font-size:.75rem;margin-top:1rem">© 2026 WanderWise. Made for curious travelers.</p>
</div>
""", unsafe_allow_html=True)
