import matplotlib.pyplot as plt

def plot_dimension_bar_chart(dimension_summary):
    dimensions = list(dimension_summary.keys())
    scores = [v["percent"] for v in dimension_summary.values()]

    fig, ax = plt.subplots(figsize=(7, 4))

    bars = ax.bar(dimensions, scores)

    # ---- COLOR LOGIC ----
    for bar, score in zip(bars, scores):
        if score < 40:
            bar.set_color("#d62728")  # Red
        elif score < 70:
            bar.set_color("#ff7f0e")  # Orange
        else:
            bar.set_color("#2ca02c")  # Green

    ax.set_ylim(0, 100)
    ax.set_ylabel("Readiness (%)")
    ax.set_title("AI Readiness by Dimension")

    # Value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 2,
            f"{int(height)}%",
            ha="center",
            fontsize=9
        )

    return fig
