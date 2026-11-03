

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DATA_FILE = Path(__file__).resolve().parent / "netflix_titles.csv"
OUTPUT_FILE = Path(__file__).resolve().parent / "netflix_visualizations.png"
CHART_OUTPUTS = {
    "type": Path(__file__).resolve().parent / "content_distribution_by_type.png",
    "growth": Path(__file__).resolve().parent / "content_growth_over_years.png",
    "countries": Path(__file__).resolve().parent / "top_content_producing_countries.png",
    "correlation": Path(__file__).resolve().parent / "numerical_attributes_correlation_heatmap.png",
}
REQUIRED_COLUMNS = {"type", "release_year", "country", "duration"}


def load_titles(csv_path: Path) -> pd.DataFrame:
    """Load the CSV and validate the columns used by the dashboard."""
    if not csv_path.is_file():
        raise FileNotFoundError(f"Netflix dataset was not found: {csv_path}")

    titles = pd.read_csv(csv_path)
    missing_columns = REQUIRED_COLUMNS.difference(titles.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Dataset is missing required columns: {missing}")
    if titles.empty:
        raise ValueError(f"Netflix dataset contains no records: {csv_path}")

    titles["release_year"] = pd.to_numeric(titles["release_year"], errors="coerce")
    titles["duration_value"] = pd.to_numeric(
        titles["duration"].astype("string").str.extract(r"(\d+)")[0],
        errors="coerce",
    )
    titles["movie_duration_minutes"] = titles["duration_value"].where(
        titles["type"].eq("Movie")
    )
    titles["tv_seasons"] = titles["duration_value"].where(
        titles["type"].eq("TV Show")
    )
    return titles


def plot_individual_charts(titles: pd.DataFrame) -> None:
    """Create and save each requested visualization as a separate image."""
    type_counts = titles["type"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        type_counts.index,
        type_counts.values,
        color=["#2f6b9a" if name == "Movie" else "#e66b4e" for name in type_counts.index],
    )
    ax.set(title="Content Distribution by Type", xlabel="Content type", ylabel="Number of titles")
    ax.bar_label(bars, fmt="%d", padding=3)
    fig.tight_layout()
    fig.savefig(CHART_OUTPUTS["type"], dpi=200, bbox_inches="tight")
    plt.close(fig)

    yearly_counts = (
        titles.dropna(subset=["release_year"])
        .groupby("release_year")
        .size()
        .sort_index()
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(yearly_counts.index, yearly_counts.values, color="#2f6b9a", linewidth=2)
    ax.set(
        title="Content Growth Over Release Years",
        xlabel="Release year",
        ylabel="Number of titles",
    )
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(CHART_OUTPUTS["growth"], dpi=200, bbox_inches="tight")
    plt.close(fig)

    country_counts = (
        titles["country"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .loc[lambda countries: countries.ne("")]
        .value_counts()
        .head(10)
        .sort_values()
    )
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(country_counts.index, country_counts.values, color="#58a27c")
    ax.set(
        title="Top 10 Content-Producing Countries",
        xlabel="Number of titles",
        ylabel="Country",
    )
    fig.tight_layout()
    fig.savefig(CHART_OUTPUTS["countries"], dpi=200, bbox_inches="tight")
    plt.close(fig)

    numeric_attributes = titles[
        ["release_year", "movie_duration_minutes", "tv_seasons"]
    ]
    correlations = numeric_attributes.corr()
    values = correlations.to_numpy()
    labels = ["Release year", "Movie minutes", "TV seasons"]
    fig, ax = plt.subplots(figsize=(7, 6))
    image = ax.imshow(np.ma.masked_invalid(values), cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(labels)), labels=labels, rotation=25, ha="right")
    ax.set_yticks(range(len(labels)), labels=labels)
    ax.set_title("Correlation of Numeric Attributes")
    for row in range(len(labels)):
        for column in range(len(labels)):
            value = values[row, column]
            annotation = f"{value:.2f}" if np.isfinite(value) else "N/A"
            ax.text(column, row, annotation, ha="center", va="center", color="black")
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04, label="Correlation")
    fig.tight_layout()
    fig.savefig(CHART_OUTPUTS["correlation"], dpi=200, bbox_inches="tight")
    plt.close(fig)

    for chart_path in CHART_OUTPUTS.values():
        print(f"Chart saved to: {chart_path}")


def plot_dashboard(titles: pd.DataFrame, output_path: Path) -> None:
    """Draw and save the four requested Netflix visualizations."""
    colors = {"Movie": "#2f6b9a", "TV Show": "#e66b4e"}
    fig, axes = plt.subplots(2, 2, figsize=(16, 11))
    fig.suptitle("Netflix Titles: Content Overview", fontsize=20, fontweight="bold")

    # Content distribution by type
    type_counts = titles["type"].value_counts()
    axes[0, 0].bar(
        type_counts.index,
        type_counts.values,
        color=[colors.get(content_type, "#777777") for content_type in type_counts.index],
    )
    axes[0, 0].set_title("Content Distribution by Type")
    axes[0, 0].set_xlabel("Content type")
    axes[0, 0].set_ylabel("Number of titles")
    axes[0, 0].bar_label(axes[0, 0].containers[0], fmt="%d", padding=3)

    # Titles are grouped by their release year, not by their Netflix addition date.
    yearly_counts = (
        titles.dropna(subset=["release_year"])
        .groupby("release_year")
        .size()
        .sort_index()
    )
    axes[0, 1].plot(
        yearly_counts.index,
        yearly_counts.values,
        color="#2f6b9a",
        linewidth=2,
    )
    axes[0, 1].set_title("Content Growth Over Release Years")
    axes[0, 1].set_xlabel("Release year")
    axes[0, 1].set_ylabel("Number of titles")
    axes[0, 1].grid(axis="y", alpha=0.3)

    # Split multi-country entries so each listed country receives one title count.
    country_counts = (
        titles["country"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
        .loc[lambda countries: countries.ne("")]
        .value_counts()
        .head(10)
        .sort_values()
    )
    axes[1, 0].barh(country_counts.index, country_counts.values, color="#58a27c")
    axes[1, 0].set_title("Top 10 Content-Producing Countries")
    axes[1, 0].set_xlabel("Number of titles")
    axes[1, 0].set_ylabel("Country")

    # Keep movie minutes and TV seasons separate because they are different units.
    numeric_attributes = titles[
        ["release_year", "movie_duration_minutes", "tv_seasons"]
    ]
    correlations = numeric_attributes.corr()
    correlation_values = correlations.to_numpy()
    masked_correlations = np.ma.masked_invalid(correlation_values)
    image = axes[1, 1].imshow(
        masked_correlations,
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
    )
    labels = ["Release year", "Movie minutes", "TV seasons"]
    axes[1, 1].set_xticks(range(len(labels)), labels=labels, rotation=25, ha="right")
    axes[1, 1].set_yticks(range(len(labels)), labels=labels)
    axes[1, 1].set_title("Correlation of Numeric Attributes")
    for row in range(len(labels)):
        for column in range(len(labels)):
            value = correlation_values[row, column]
            annotation = f"{value:.2f}" if np.isfinite(value) else "N/A"
            axes[1, 1].text(
                column,
                row,
                annotation,
                ha="center",
                va="center",
                color="black",
            )
    fig.colorbar(image, ax=axes[1, 1], fraction=0.046, pad=0.04, label="Correlation")

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    print(f"Dashboard saved to: {output_path}")
    plt.show()


def main() -> None:
    titles = load_titles(DATA_FILE)
    plot_individual_charts(titles)
    plot_dashboard(titles, OUTPUT_FILE)


if __name__ == "__main__":
    main()