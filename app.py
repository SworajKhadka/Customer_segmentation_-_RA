import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide",
)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("data/rfm_final.csv")
    return df

df = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title("🔍 Filters")
segments = ["All"] + sorted(df["SegmentName"].unique().tolist())
selected = st.sidebar.selectbox("Customer Segment", segments)

if selected != "All":
    filtered = df[df["SegmentName"] == selected]
else:
    filtered = df

# ── Header ────────────────────────────────────────────────────────────────────
st.title("📊 Customer Segmentation & Retention Analysis")
st.markdown(
    "End-to-end customer analytics using **RFM scoring**, **KMeans clustering**, "
    "and **Logistic Regression churn prediction** on the UCI Online Retail II dataset."
)
st.divider()

# ── KPI row ───────────────────────────────────────────────────────────────────
total     = len(filtered)
avg_churn = filtered["ChurnProbability"].mean() * 100
avg_spend = filtered["Monetary"].mean()
avg_freq  = filtered["Frequency"].mean()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Customers",       f"{total:,}")
k2.metric("Avg Churn Probability", f"{avg_churn:.1f}%")
k3.metric("Avg Total Spend (£)",   f"£{avg_spend:,.0f}")
k4.metric("Avg Purchase Frequency",f"{avg_freq:.1f}")

st.divider()

# ── Row 1: Segment Distribution + Churn Risk ──────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Segment Distribution")
    seg_counts = filtered["SegmentName"].value_counts().reset_index()
    seg_counts.columns = ["Segment", "Count"]
    fig1 = px.pie(
        seg_counts, values="Count", names="Segment",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4,
    )
    fig1.update_traces(textposition="inside", textinfo="percent+label")
    fig1.update_layout(showlegend=True, margin=dict(t=20, b=20))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Average Churn Risk by Segment")
    churn_seg = (
        filtered.groupby("SegmentName")["ChurnProbability"]
        .mean()
        .mul(100)
        .reset_index()
        .sort_values("ChurnProbability", ascending=True)
    )
    churn_seg.columns = ["Segment", "Churn %"]
    fig2 = px.bar(
        churn_seg, x="Churn %", y="Segment", orientation="h",
        color="Churn %", color_continuous_scale="RdYlGn_r",
        text=churn_seg["Churn %"].apply(lambda x: f"{x:.1f}%"),
    )
    fig2.update_traces(textposition="outside")
    fig2.update_layout(coloraxis_showscale=False, margin=dict(t=20, b=20))
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: RFM Scatter + Revenue by Segment ───────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.subheader("RFM Behaviour Map")
    fig3 = px.scatter(
        filtered, x="Recency", y="Frequency",
        color="SegmentName", size="Monetary",
        size_max=20,
        color_discrete_sequence=px.colors.qualitative.Set2,
        labels={"Recency": "Recency (days)", "Frequency": "Purchase Frequency"},
        opacity=0.7,
    )
    fig3.update_layout(legend_title="Segment", margin=dict(t=20, b=20))
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Revenue Contribution by Segment")
    rev_seg = (
        filtered.groupby("SegmentName")["Monetary"]
        .sum()
        .reset_index()
        .sort_values("Monetary", ascending=False)
    )
    rev_seg.columns = ["Segment", "Total Revenue (£)"]
    fig4 = px.bar(
        rev_seg, x="Segment", y="Total Revenue (£)",
        color="Segment",
        color_discrete_sequence=px.colors.qualitative.Set2,
        text=rev_seg["Total Revenue (£)"].apply(lambda x: f"£{x:,.0f}"),
    )
    fig4.update_traces(textposition="outside")
    fig4.update_layout(showlegend=False, margin=dict(t=20, b=20))
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3: Purchase Interval Distribution ─────────────────────────────────────
st.subheader("Purchase Interval Distribution by Segment")
fig5 = px.box(
    filtered, x="SegmentName", y="PurchaseInterval",
    color="SegmentName",
    color_discrete_sequence=px.colors.qualitative.Set2,
    labels={"PurchaseInterval": "Days Between Purchases", "SegmentName": "Segment"},
)
fig5.update_layout(showlegend=False, margin=dict(t=20, b=20))
st.plotly_chart(fig5, use_container_width=True)

# ── Raw data toggle ───────────────────────────────────────────────────────────
with st.expander("View Raw Data"):
    st.dataframe(filtered.reset_index(drop=True), use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built by Sworaj Khadka · UCI Online Retail II Dataset · Python, Pandas, Scikit-learn, Plotly, Streamlit")