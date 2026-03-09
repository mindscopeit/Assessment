import numpy as np
import math

# --- Base weights for scoring ---
BASE_DIMENSIONS = {
    "AI Adoption & Use Cases": 0.20,
    "Workforce & Culture": 0.10,
    "Infrastructure & Security": 0.15,
    "Compliance & Regulatory": 0.20,
    "ROI & Scaling": 0.15
}

# Domain multipliers (raw, non‑normalized)
DOMAIN_MULTIPLIERS = {
    "Healthcare": {"Compliance & Regulatory": 1.4, "Infrastructure & Security": 1.3},
    "Insurance": {"Compliance & Regulatory": 1.3, "Infrastructure & Security": 1.2},
    "Retail": {"AI Adoption & Use Cases": 1.3},
    "Media": {"AI Adoption & Use Cases": 1.4},
    "Pharma & Biotech": {"Compliance & Regulatory": 1.5, "Infrastructure & Security": 1.4},
    "IT Services": {"Infrastructure & Security": 1.3}
}

# Map raw question dimensions to the five report dimensions
QUESTION_DIMENSION_MAPPING = {
    # AI Adoption & Use Cases
    "AI Use Cases": "AI Adoption & Use Cases",
    "Generative AI": "AI Adoption & Use Cases",
    "Computer Vision": "AI Adoption & Use Cases",
    "Audio AI": "AI Adoption & Use Cases",
    "Experience": "AI Adoption & Use Cases",
    "NLP": "AI Adoption & Use Cases",
    "AR/VR": "AI Adoption & Use Cases",
    "Synthetic Media": "AI Adoption & Use Cases",
    "Predictive Analytics": "AI Adoption & Use Cases",
    "Advanced AI Capabilities": "AI Adoption & Use Cases",
    "Analytics": "AI Adoption & Use Cases",               # from media
    # Workforce & Culture
    "Adoption": "Workforce & Culture",
    "Leadership": "Workforce & Culture",
    "Training": "Workforce & Culture",
    "Culture": "Workforce & Culture",
    # Infrastructure & Security
    "Edge Computing": "Infrastructure & Security",
    "AI Operations": "Infrastructure & Security",
    "Cloud": "Infrastructure & Security",
    "Data": "Infrastructure & Security",
    "Metadata": "Infrastructure & Security",
    "Cloud & Data Governance": "Infrastructure & Security",
    "Infrastructure": "Infrastructure & Security",        # from media
    "Security": "Infrastructure & Security",              # from media
    # Compliance & Regulatory
    "Rights Management": "Compliance & Regulatory",
    "Bias & Fairness": "Compliance & Regulatory",
    "Copyright Compliance": "Compliance & Regulatory",
    "IP Ownership": "Compliance & Regulatory",
    "Ethics": "Compliance & Regulatory",
    "Compliance": "Compliance & Regulatory",              # from media
    "Deepfake Detection": "Compliance & Regulatory",      # from media
    # ROI & Scaling
    "Scaling Barriers": "ROI & Scaling",
    "Cost Tracking": "ROI & Scaling",
    "AI Content Share": "ROI & Scaling",
    "Scaling Readiness": "ROI & Scaling",
    "ROI": "ROI & Scaling",                               # from media
}

RISK_LEVEL_PENALTY = {
    "Critical": 10,
    "High": 5,
    "Medium": 2,
    "Low": 0,
    "Very Low": 0
}

def get_raw_dimension_weights(domain):
    """
    Return raw (non‑normalized) weights after applying domain multipliers.
    Used for dimension‑weighted risk penalties.
    """
    weights = BASE_DIMENSIONS.copy()
    if domain in DOMAIN_MULTIPLIERS:
        for dim, mult in DOMAIN_MULTIPLIERS[domain].items():
            if dim in weights:
                weights[dim] *= mult
    return weights

def normalize_weights(raw_weights):
    """Normalize a dict of weights to sum to 1."""
    total = sum(raw_weights.values())
    if total == 0:
        return raw_weights
    return {dim: w/total for dim, w in raw_weights.items()}

def dimension_label(p):
    if p < 40:
        return "Poor"
    elif p < 70:
        return "Moderate"
    else:
        return "Strong"

def get_maturity(score):
    if score < 40:
        return "Beginner"
    elif score < 60:
        return "Emerging"
    elif score < 75:
        return "Scaled"
    else:
        return "AI-Native"

def get_deployment_verdict(score):
    if score >= 75:
        return "Production Ready"
    elif score >= 55:
        return "Pilot Deployment"
    else:
        return "Not Ready"

def logistic_transform(percent, k=0.1, midpoint=50):
    """
    Apply an S‑shaped curve to a percentage to increase discrimination.
    """
    return 100 / (1 + math.exp(-k * (percent - midpoint)))

def percentile_of_score(score, scores_list):
    """Return the percentile rank of a score relative to a list of scores."""
    if not scores_list:
        return None
    less = sum(1 for s in scores_list if s < score)
    equal = sum(1 for s in scores_list if s == score)
    # Using (less + 0.5*equal)/len *100 gives a smooth percentile
    return round((less + 0.5 * equal) / len(scores_list) * 100, 1)

def calculate_ai_readiness_advanced(answers, domain, use_logistic=False, industry_scores=None):
    """
    Enhanced AI readiness scoring.

    Parameters
    ----------
    answers : dict
        Keys are question IDs, values are dicts with keys:
            'dimension' (raw dimension name),
            'score' (int or list for multi-select),
            'max_score' (int or list),
            'risk_level' (str or list),
            'risk_weight' (float, default 1),
            'weight' (float, per-question importance, default 1),
            'selection_type' (optional, 'single' or 'multi')
    domain : str
        Industry domain (e.g., 'Healthcare', 'Retail').
    use_logistic : bool, optional
        If True, apply a logistic transformation to dimension percentages.
    industry_scores : list, optional
        List of final scores from previous assessments in the same domain,
        used to compute percentile rank.

    Returns
    -------
    dict
        Comprehensive scoring results.
    """
    # 1. Get raw (pre‑normalization) weights for risk weighting
    raw_weights = get_raw_dimension_weights(domain)

    # 2. Initialize accumulators
    dim_score = {}      # weighted sum of scores per dimension
    dim_max = {}        # weighted sum of max scores per dimension
    risk_penalty_weighted = 0.0

    # 3. Process each answer
    for qid, resp in answers.items():
        # Map question dimension to report dimension
        raw_dim = resp["dimension"]
        dim = QUESTION_DIMENSION_MAPPING.get(raw_dim, raw_dim)

        # Extract values with defaults
        score = resp["score"]
        max_score = resp.get("max_score", 3)
        risk = resp.get("risk_level", "Low")
        risk_weight = resp.get("risk_weight", 1)
        q_weight = resp.get("weight", 1)          # per-question importance (default 1)
        qtype = resp.get("selection_type", "single")

        # Handle multi-select scoring (log transform to dampen)
        if isinstance(score, list):
            score = sum(score)
        if isinstance(max_score, list):
            max_score = sum(max_score)
        if qtype == "multi":
            score = math.log(1 + score)
            max_score = math.log(1 + max_score)

        # Apply per-question weight
        score *= q_weight
        max_score *= q_weight

        # Accumulate dimension totals
        dim_score[dim] = dim_score.get(dim, 0) + score
        dim_max[dim] = dim_max.get(dim, 0) + max_score

        # --- Risk penalty (weighted by dimension importance) ---
        if isinstance(risk, list):
            # Use the maximum risk level among selected options
            effective_risk = max([RISK_LEVEL_PENALTY.get(r, 0) for r in risk])
        else:
            effective_risk = RISK_LEVEL_PENALTY.get(risk, 0)

        # Multiply by risk_weight and the dimension's raw weight
        risk_penalty_weighted += effective_risk * risk_weight * raw_weights.get(dim, 0)

    # 4. Ensure all base dimensions are included in the summary
    all_dims = set(BASE_DIMENSIONS.keys()) | set(dim_score.keys())
    summary = {}

    for dim in all_dims:
        if dim in dim_score and dim_max[dim] > 0:
            percent = (dim_score[dim] / dim_max[dim]) * 100
        else:
            percent = 0.0
            # Mark as not assessed only if it's a base dimension with no data
            if dim in BASE_DIMENSIONS and dim not in dim_score:
                label = "Not Assessed"
            else:
                label = dimension_label(percent)

        if use_logistic and percent > 0 and dim in dim_score:
            percent = logistic_transform(percent)

        # If we already computed a label above for "Not Assessed", keep it
        if dim in BASE_DIMENSIONS and dim not in dim_score:
            label = "Not Assessed"
        else:
            label = dimension_label(percent)

        summary[dim] = {
            "percent": round(percent, 2),
            "label": label
        }

    # 5. Identify dimensions that actually have data
    present_dims = [d for d in summary if summary[d]["label"] != "Not Assessed"]

    if not present_dims:
        # No data at all – return zeros
        return {
            "Final Score": 0,
            "Base Score Before Risk": 0,
            "Dimension Summary": summary,
            "Total Risk Penalty": round(risk_penalty_weighted, 2),
            "Risk Profile": "Unknown",
            "AI Maturity": "Beginner",
            "Stability Index": 0,
            "Deployment Verdict": "Not Ready"
        }

    # 6. Normalize weights over present dimensions only
    present_raw_weights = {d: raw_weights[d] for d in present_dims}
    norm_weights = normalize_weights(present_raw_weights)

    # 7. Compute weighted base score
    weighted_score = 0.0
    for dim in present_dims:
        percent = summary[dim]["percent"] / 100.0
        weighted_score += percent * norm_weights[dim]

    base_score = weighted_score * 100  # back to percentage scale

    # 8. Apply risk penalty (exponential decay)
    adjusted_score = base_score * math.exp(-risk_penalty_weighted / 100)

    # 9. Stability index (std dev of present dimension percentages)
    present_percents = [summary[d]["percent"] for d in present_dims]
    stability_index = round(100 - np.std(present_percents), 2)

    # 10. Risk profile
    if risk_penalty_weighted >= 40:
        risk_profile = "Severe"
    elif risk_penalty_weighted >= 20:
        risk_profile = "Elevated"
    else:
        risk_profile = "Managed"

    # 11. Maturity and deployment verdict
    maturity = get_maturity(adjusted_score)
    deployment_verdict = get_deployment_verdict(adjusted_score)

    # 12. Industry percentile (if benchmark data provided)
    percentile = None
    if industry_scores:
        percentile = percentile_of_score(adjusted_score, industry_scores)

    # 13. Assemble result
    result = {
        "Final Score": round(adjusted_score, 2),
        "Base Score Before Risk": round(base_score, 2),
        "Dimension Summary": summary,
        "Total Risk Penalty": round(risk_penalty_weighted, 2),
        "Risk Profile": risk_profile,
        "AI Maturity": maturity,
        "Stability Index": stability_index,
        "Deployment Verdict": deployment_verdict
    }
    if percentile is not None:
        result["Industry Percentile"] = percentile

    return result

def generate_recommendations(summary, adjusted_score):
    """
    Original recommendation function (kept for compatibility).
    """
    recommendations = []

    for dim, info in summary.items():
        label = info["label"]
        if label == "Poor":
            recommendations.append(f"{dim}: Focus on improving this dimension to accelerate AI readiness.")
        elif label == "Moderate":
            recommendations.append(f"{dim}: Some progress, consider targeted initiatives to strengthen this area.")
        else:
            recommendations.append(f"{dim}: Strong performance, maintain current practices.")

    # Overall recommendation based on AI maturity
    if adjusted_score < 40:
        recommendations.append("Overall: Begin foundational AI initiatives and training programs.")
    elif adjusted_score < 60:
        recommendations.append("Overall: Explore pilot AI projects to demonstrate value.")
    elif adjusted_score < 75:
        recommendations.append("Overall: Scale successful AI initiatives across the organization.")
    else:
        recommendations.append("Overall: Organization is AI-Native; continue innovation and advanced use cases.")

    return recommendations