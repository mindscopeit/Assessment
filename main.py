import importlib
import streamlit as st
from scoring import calculate_ai_readiness_advanced, generate_recommendations
from fpdf import FPDF
import datetime
import io
import os
from PIL import Image, ImageDraw, ImageFont

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="AI Readiness Assessment", layout="centered")

# ================= LOGO HANDLING (ONLY FOR WEB PAGE) =================
logo_path = "photo.jpg"  # Replace with your actual logo file if you have one

def create_text_logo_image():
    """Generate a simple image with company name and tagline – always returns a valid PIL Image."""
    try:
        width, height = 200, 100
        img = Image.new('RGB', (width, height), color=(44, 62, 80))
        draw = ImageDraw.Draw(img)
        # Try system fonts, fallback to default
        try:
            font_main = ImageFont.truetype("arial.ttf", 20)
            font_tagline = ImageFont.truetype("arial.ttf", 12)
        except:
            font_main = ImageFont.load_default()
            font_tagline = ImageFont.load_default()
        draw.text((10, 25), "Mind Scope IT", fill=(255,255,255), font=font_main)
        draw.text((10, 55), "Expanding Your Digital Horizon", fill=(255,255,255), font=font_tagline)
        return img
    except Exception:
        # Ultimate fallback – never returns None
        img = Image.new('RGB', (200, 100), color=(100, 100, 100))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.load_default()
            draw.text((10, 40), "LOGO", fill=(255,255,255), font=font)
        except:
            pass
        return img

def get_logo_image():
    """Return a PIL Image – guaranteed to never return None."""
    if os.path.exists(logo_path):
        try:
            return Image.open(logo_path)
        except Exception:
            return create_text_logo_image()
    else:
        return create_text_logo_image()

# Get the logo image once – used for web display only
LOGO_IMAGE = get_logo_image()

# Display logo on the web page
col1, col2 = st.columns([1, 4])
with col1:
    st.image(LOGO_IMAGE, width=140)
with col2:
    st.title("AI Readiness Assessment")
    st.write("Evaluate your organization's readiness for AI adoption across key dimensions.")

# ================= CACHING =================
@st.cache_data
def load_domain_questions(domain_name):
    """Cache domain questions to avoid re-importing"""
    domain_module = importlib.import_module(domain_name)
    Question_Bank = domain_module.Question_Bank
    
    all_questions = []
    for dim, questions in Question_Bank["sections"].items():
        for q in questions:
            if "dimension" not in q:
                q["dimension"] = dim
            all_questions.append(q)
    return all_questions

# ---------------- DOMAIN FILES ----------------
DOMAIN_FILES = {
    "Financial Services": "finance_questions",
    "Healthcare": "heathcare",
    "Retail": "retail",
    "Insurance": "insurance",
    "Pharma & Biotech": "pharma_biotec",
    "Media & Entertainment": "media",
    "IT Services": "itservice",
    "Government & Public Sector": "goverance_question"
}

# Mandatory dimensions
MANDATORY_DIMENSIONS = ["Infrastructure & Security", "Compliance & Regulatory"]

# ---------------- SESSION STATE ----------------
defaults = {
    "step": 1,
    "domain": None,
    "scope": None,
    "selected_dimensions": [],
    "filtered_questions": [],
    "answers": {},
    "q_index": 0
}

# Initialize session state once
if "_initialized" not in st.session_state:
    for k, v in defaults.items():
        st.session_state[k] = v
    st.session_state._initialized = True

# ================= STEP 1 =================
if st.session_state.step == 1:
    st.subheader("Welcome")
    st.write("""
    This assessment evaluates AI readiness across:
    - Security & Infrastructure
    - Compliance & Regulatory
    - Cloud & Data Governance
    - AI Adoption & Use Cases
    - Workforce & Culture
    - ROI & Scaling
    """)
    # Ask for client/user name
    if "client_name" not in st.session_state:
        st.session_state.client_name = ""

    st.session_state.client_name = st.text_input(
        "Please enter your name or client ID:",
        value=st.session_state.client_name
    )

    if st.button("Start Assessment"):
        st.session_state.step = 2
        st.experimental_rerun()

# ================= STEP 2 =================
elif st.session_state.step == 2:
    st.subheader("Select Industry Domain")
    domain = st.selectbox(
        "Choose your industry:",
        ["-- Select --"] + list(DOMAIN_FILES.keys())
    )
    if domain != "-- Select --":
        st.session_state.domain = domain

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 1
            st.experimental_rerun()
    with col2:
        if st.button("Continue"):
            if not st.session_state.domain or st.session_state.domain == "-- Select --":
                st.warning("Please select a domain to continue.")
            else:
                st.session_state.step = 3
                st.experimental_rerun()

# ================= STEP 3 =================
elif st.session_state.step == 3:
    st.subheader("Customize Assessment Scope")

    all_questions = load_domain_questions(DOMAIN_FILES[st.session_state.domain])
    st.session_state.all_questions = all_questions

    scope = st.radio("Select assessment scope:", ["All Questions", "Specific Dimensions"])
    st.session_state.scope = scope

    selected_dimensions = []
    if scope == "Specific Dimensions":
        dimensions = sorted({q["dimension"] for q in all_questions if q["dimension"] not in MANDATORY_DIMENSIONS})
        selected_dimensions = st.multiselect("Select one or more dimensions:", dimensions)
        st.session_state.selected_dimensions = selected_dimensions

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 2
            st.experimental_rerun()
    with col2:
        if st.button("Start Assessment"):
            # Include mandatory questions
            mandatory_questions = [q for q in all_questions if q["dimension"] in MANDATORY_DIMENSIONS]

            if scope == "All Questions":
                filtered = all_questions
            else:
                if not selected_dimensions:
                    st.warning("Please select at least one dimension.")
                    st.stop()
                filtered = [q for q in all_questions if q["dimension"] in selected_dimensions] + mandatory_questions

            # Remove duplicates
            unique_questions = []
            seen_ids = set()
            for q in filtered:
                if q["id"] not in seen_ids:
                    unique_questions.append(q)
                    seen_ids.add(q["id"])

            st.session_state.filtered_questions = unique_questions
            st.session_state.answers = {}
            st.session_state.q_index = 0
            st.session_state.step = 4
            st.experimental_rerun()

# ================= STEP 4 =================
elif st.session_state.step == 4:
    qs = st.session_state.filtered_questions
    i = st.session_state.q_index

    st.subheader("Answer the Questions")

    if i >= len(qs):
        st.success("✅ You have completed all questions!")
        if st.button("View AI Readiness Report"):
            st.session_state.step = 5
            st.experimental_rerun()
    else:
        q = qs[i]
        st.caption(f"Question {i+1} of {len(qs)}")
        st.progress((i+1)/len(qs))
        st.divider()

        if q["dimension"] in MANDATORY_DIMENSIONS:
            st.markdown("🔒 **Mandatory Security / Compliance Question**")

        st.markdown(f"### {q['question']}")
        selection_type = q.get("selection_type", "single")

        if selection_type == "multi":
            selected_labels = st.multiselect(
                "Select all that apply:",
                [o["label"] for o in q["options"]],
                key=f"multi_{q['id']}"
            )
            selected_options = [o for o in q["options"] if o["label"] in selected_labels]
            total_score = sum(o["score"] for o in selected_options)
            max_score = sum(o["score"] for o in q["options"])
            risk_levels = [o.get("risk_level", "Medium") for o in selected_options]
            scores_list = [o["score"] for o in selected_options]
        else:  # single
            labels = [o["label"] for o in q["options"]]
            prev_index = 0
            if q["id"] in st.session_state.answers:
                prev_score = st.session_state.answers[q["id"]]["score"]
                prev_score_val = prev_score[0] if isinstance(prev_score, list) else prev_score
                for idx, o in enumerate(q["options"]):
                    if o["score"] == prev_score_val:
                        prev_index = idx
                        break
            choice = st.radio(
                "Choose one option:",
                labels,
                index=prev_index,
                key=f"q_{q['id']}"
            )
            selected_option = next(o for o in q["options"] if o["label"] == choice)
            total_score = selected_option["score"]
            max_score = max(o["score"] for o in q["options"])
            risk_levels = selected_option.get("risk_level", "Medium")
            scores_list = [total_score]

        st.session_state.answers[q["id"]] = {
            "dimension": q["dimension"],
            "score": scores_list,
            "max_score": max_score,
            "risk_level": risk_levels,
            "selection_type": selection_type,
            "risk_weight": q.get("risk_weight", 1)
        }

        # Navigation buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back") and i > 0:
                st.session_state.q_index -= 1
                st.experimental_rerun()
        with col2:
            if st.button("Next"):
                st.session_state.q_index += 1
                st.experimental_rerun()

# ================= STEP 5 =================
elif st.session_state.step == 5:

    import datetime
    import matplotlib.pyplot as plt
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    import textwrap

    st.subheader("AI Readiness Assessment Report")
    st.write("Thank you for completing the assessment. You can download the full report below.")

    # ================= GET RESULTS =================
    result = calculate_ai_readiness_advanced(
        st.session_state.answers,
        st.session_state.domain
    )

    # ================= RECOMMENDATIONS FUNCTION =================
    def generate_recommendations(summary, adjusted_score):
        recommendations = []
        for dim, info in summary.items():
            label = info["label"]
            if label == "Poor":
                recommendations.append(f"{dim}: Focus on improving this dimension to accelerate AI readiness.")
            elif label == "Moderate":
                recommendations.append(f"{dim}: Some progress, consider targeted initiatives to strengthen this area.")
            else:
                recommendations.append(f"{dim}: Strong performance, maintain current practices.")

        if adjusted_score < 40:
            recommendations.append("Overall: Begin foundational AI initiatives and training programs.")
        elif adjusted_score < 60:
            recommendations.append("Overall: Explore pilot AI projects to demonstrate value.")
        elif adjusted_score < 75:
            recommendations.append("Overall: Scale successful AI initiatives across the organization.")
        else:
            recommendations.append("Overall: Organization is AI-Native; continue innovation and advanced use cases.")
        return recommendations

    recommendations = generate_recommendations(result["Dimension Summary"], result["Final Score"])

    final_score = result["Final Score"]
    base_score = result["Base Score Before Risk"]
    dimension_summary = result["Dimension Summary"]
    total_risk_penalty = result["Total Risk Penalty"]
    risk_profile = result["Risk Profile"]
    stability_index = result["Stability Index"]
    maturity = result["AI Maturity"]
    deployment_verdict = result["Deployment Verdict"]

    # ================= PDF FUNCTION (NO LOGO) =================
    def generate_pdf(final_score, base_score, dimension_summary, total_risk_penalty,
                     risk_profile, stability_index, maturity, deployment_verdict, recommendations):

        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        y = height - 2*cm

        # ---------- TITLE (directly, no logo) ----------
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(width/2, y, "AI Readiness Assessment Report")
        y -= 2*cm

        # ---------- CLIENT INFO ----------
        pdf.setFont("Helvetica", 12)
        client_name = st.session_state.get("client_name", "[Client Name]")
        pdf.drawString(2*cm, y, f"Client: {client_name}")
        pdf.drawString(12*cm, y, f"Date: {datetime.datetime.today().strftime('%Y-%m-%d')}")
        y -= 1*cm
        pdf.drawString(2*cm, y, "Prepared by: MindScope IT")
        y -= 1.5*cm

        # ---------- EXECUTIVE SUMMARY ----------
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(2*cm, y, "Executive Summary")
        y -= 1*cm

        pdf.setFont("Helvetica", 12)
        pdf.drawString(2*cm, y, f"Final Score: {final_score} / 100")
        y -= 0.7*cm
        pdf.drawString(2*cm, y, f"AI Maturity: {maturity}")
        y -= 0.7*cm
        pdf.drawString(2*cm, y, f"Deployment Verdict: {deployment_verdict}")
        y -= 0.7*cm
        pdf.drawString(2*cm, y, f"Base Score (Before Risk): {base_score}")
        y -= 0.7*cm
        pdf.drawString(2*cm, y, f"Risk Profile: {risk_profile}")
        y -= 0.7*cm
        pdf.drawString(2*cm, y, f"Stability Index: {stability_index}")
        y -= 1.5*cm

        # ---------- FILTER OUT "NOT ASSESSED" DIMENSIONS ----------
        assessed_dims = {dim: info for dim, info in dimension_summary.items() if info["label"] != "Not Assessed"}

        # ---------- DIMENSION TABLE (only assessed) ----------
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(2*cm, y, "Dimension-wise Readiness")
        y -= 1*cm

        pdf.setFont("Helvetica", 12)
        for dim, info in assessed_dims.items():
            line = f"{dim}: {info['label']} ({info['percent']}%)"
            wrapped = textwrap.wrap(line, width=60)
            for w in wrapped:
                pdf.drawString(2*cm, y, w)
                y -= 0.6*cm
        y -= 1*cm

        # ---------- GRAPH (only assessed) ----------
        if assessed_dims:
            dims = list(assessed_dims.keys())
            percents = [info["percent"] for info in assessed_dims.values()]
            wrapped_dims = ["\n".join(textwrap.wrap(d, width=12)) for d in dims]

            plt.figure(figsize=(10, 4))
            bars = plt.bar(wrapped_dims, percents)
            plt.ylim(0, 100)
            plt.ylabel("Readiness %")
            plt.title("AI Readiness by Dimension")
            plt.xticks(rotation=45, ha="right")
            for bar, perc in zip(bars, percents):
                plt.text(
                    bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 1,
                    f"{perc:.1f}%",
                    ha='center',
                    va='bottom'
                )
            plt.tight_layout()
            graph_buffer = io.BytesIO()
            plt.savefig(graph_buffer, format="PNG", bbox_inches='tight')
            plt.close()
            graph_buffer.seek(0)
            pil_img = Image.open(graph_buffer)

            graph_height = 8*cm
            if y - graph_height < 3*cm:
                pdf.showPage()
                y = height - 2*cm

            pdf.drawInlineImage(
                pil_img,
                2*cm,
                y - graph_height,
                width=16*cm,
                height=graph_height
            )
            y -= graph_height + 1*cm
        else:
            pdf.drawString(2*cm, y, "No dimension data available.")
            y -= 1*cm

        # ---------- RISK ANALYSIS ----------
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(2*cm, y, "Risk Analysis")
        y -= 1*cm

        pdf.setFont("Helvetica", 12)
        pdf.drawString(2*cm, y, f"Total Risk Penalty: {total_risk_penalty}")
        y -= 1.5*cm

        # ---------- RECOMMENDATIONS ----------
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(2*cm, y, "Recommendations")
        y -= 1*cm
        pdf.setFont("Helvetica", 12)
        for rec in recommendations:
            wrapped = textwrap.wrap(rec, width=100)
            for line in wrapped:
                if y < 3*cm:
                    pdf.showPage()
                    y = height - 2*cm
                pdf.drawString(2*cm, y, line)
                y -= 0.6*cm
            y -= 0.5*cm

        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        return buffer

    # ================= DOWNLOAD BUTTON =================
    st.download_button(
        label="Download Full AI Readiness Report",
        data=generate_pdf(final_score, base_score, dimension_summary, total_risk_penalty,
                          risk_profile, stability_index, maturity, deployment_verdict, recommendations),
        file_name="AI_Readiness_Report.pdf",
        mime="application/pdf"
    )

# ================= CONTACT INFO =================
st.markdown("### Contact for Further Discussion")
st.markdown(
    """
    📞 **Contact for Further Discussion:**  

    **Email:** [contact@mindscopeit.com](https://mail.google.com/mail/?view=cm&fs=1&to=contact@mindscopeit.com&su=AI%20Readiness%20Inquiry)

    **Phone:** [Call +91 98765 43210](tel:+919876543210)  
    """,
    unsafe_allow_html=True
)