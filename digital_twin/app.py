import plotly.graph_objects as go
import streamlit as st
from modules.metrics import calculate_kpis, get_recommendation
from modules.simulator import simulate_circadian_twin

# Page Setup
st.set_page_config(
    page_title="Cognitive Circadian Digital Twin",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Digital Twin: Cognitive & Circadian Energy Simulator")
st.caption("Happiest Health Hackathon | Real-Time 'What-If' Behavioral Modeling")
st.markdown("---")

# Sidebar Controls
st.sidebar.header("⚙️ Digital Twin Parameters")

st.sidebar.subheader("1. Baseline Inputs (Past 24h)")
sleep_hours = st.sidebar.slider("Sleep Duration (Hours)", 3.0, 10.0, 6.5, 0.5)
sleep_quality = st.sidebar.select_slider(
    "Sleep Quality", options=["Restless", "Fair", "Good", "Optimal"]
)

st.sidebar.subheader("2. Interventions ('What-If' Simulation)")
caffeine_time = st.sidebar.slider("Caffeine Intake Time (24h Clock)", 6, 22, 16)
caffeine_mg = st.sidebar.slider("Caffeine Dose (mg)", 0, 300, 150, 25)
screen_time_late = st.sidebar.slider("Late Screen Exposure (Mins after 9 PM)", 0, 180, 60, 15)

st.sidebar.subheader("3. Personal Baseline")
chronotype = st.sidebar.radio("Biological Chronotype", ["Morning Lark", "Intermediate / Neutral", "Night Owl"])
chronotype_shift = {"Morning Lark": -1.5, "Intermediate / Neutral": 0.0, "Night Owl": 2.0}[chronotype]
# Mapping Quality Factor
quality_map = {"Restless": 0.6, "Fair": 0.8, "Good": 1.0, "Optimal": 1.15}
q_factor = quality_map[sleep_quality]

# Run Simulation Engine
hours, energy, disruption = simulate_circadian_twin(
    sleep_hours, q_factor, caffeine_time, caffeine_mg, screen_time_late, chronotype_shift
)

# Derive KPIs
kpis = calculate_kpis(hours, energy, disruption)

# Display Key Performance Indicators
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Predicted 2 PM Clarity",
        f"{kpis['clarity_2pm']} / 100",
        delta=f"{kpis['clarity_delta']}% vs Target"
    )

with col2:
    st.metric(
        "Deep Sleep Inhibition Risk",
        f"{kpis['disruption']}%",
        delta="-High Risk" if kpis['disruption'] > 25 else "Low Risk",
        delta_color="inverse"
    )

with col3:
    st.metric("Peak Focus Window", f"{kpis['peak_energy_hour']:02d}:00 HRS")

with col4:
    st.metric("Digital Twin Readiness", f"{kpis['recovery_score']}/100")

# Trajectory Plotting
st.subheader("📊 24-Hour Digital Twin Cognitive Trajectory")

time_labels = [f"{(int(h) + 6) % 24:02d}:00" for h in hours[::2]]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=hours,
    y=energy,
    mode='lines',
    name='Cognitive Battery',
    line=dict(color='#00CC96', width=3)
))

# Run ideal scenario simulation
_, ideal_energy, _ = simulate_circadian_twin(
    sleep_h=8.0, q_fact=1.0, caf_time=10, caf_mg=100, screen_mins=0
)

# Add ideal trace to existing Plotly figure
fig.add_trace(go.Scatter(
    x=hours,
    y=ideal_energy,
    mode='lines',
    name='Ideal Optimized Twin Baseline',
    line=dict(color='#0066FF', width=2, dash='dot')
))

fig.add_vline(x=8, line_dash="dash", line_color="#FF6666", annotation_text="Target (2 PM)")

fig.update_layout(
    xaxis=dict(tickmode='array', tickvals=hours[::2], ticktext=time_labels, title="Time of Day"),
    yaxis=dict(title="Cognitive Energy Score (0-100)", range=[0, 105]),
    margin=dict(l=20, r=20, t=30, b=20),
    template="plotly_white",
    height=400
)

st.plotly_chart(fig, width="stretch")

# Recommendation Section
st.subheader("💡 Digital Twin Recommendations")
rec_type, rec_text = get_recommendation(caffeine_time, caffeine_mg, sleep_hours, disruption)

if rec_type == "warning":
    st.warning(rec_text)
elif rec_type == "info":
    st.info(rec_text)
else:
    st.success(rec_text)