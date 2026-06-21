import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def main():

    # ---- Load Dataset ----
    csv_filename = "raw_skills.csv"
    if not os.path.exists(csv_filename):
        print(f"Error: '{csv_filename}' not found.")
        return

    df = pd.read_csv(csv_filename)

    if 'role' not in df.columns or 'skills' not in df.columns:
        print("Error: CSV must have 'role' and 'skills' columns.")
        return

    # Layman-friendly display names
    display_names = {
        "System Administrator": "Cloud & Infrastructure Engineer",
        "MLOps Engineer":       "AI Deployment Engineer",
        "Data Engineer":        "Data Platform Engineer",
    }

    # Career direction labels per role
    career_directions = {
        "Data Scientist":            "Data Science & Research",
        "DevOps Engineer":           "Cloud & DevOps",
        "Backend Developer":         "Software Development",
        "Frontend Developer":        "Web Development",
        "Cloud Engineer":            "Cloud Computing",
        "Machine Learning Engineer": "Machine Learning",
        "Data Analyst":              "Data & Business Analytics",
        "AI Engineer":               "AI Development",
        "Software Engineer":         "Software Development",
        "System Administrator":      "Cloud & Infrastructure",
        "Database Engineer":         "Database Management",
        "Full Stack Developer":      "Full Stack Development",
        "Cyber Security Analyst":    "Cybersecurity",
        "Cloud Architect":           "Cloud Architecture",
        "Data Engineer":             "Data Engineering",
        "Mobile App Developer":      "Mobile Development",
        "MLOps Engineer":            "AI Operations & Deployment",
        "AI Research Engineer":      "AI Research",
        "Business Analyst":          "Business & Analytics",
        "Software Tester":           "Quality Assurance",
        "Blockchain Developer":      "Blockchain & Web3",
        "Computer Vision Engineer":  "Computer Vision & AI",
        "Prompt Engineer":           "AI & LLM Engineering",
        "UI UX Designer":            "Design",
        "Embedded Systems Engineer": "Embedded & IoT",
        "Big Data Engineer":         "Big Data & Analytics",
    }

    # ---- Normalize Input ----
    # Synonym map for common abbreviations
    synonyms = {
        "ml":               "machinelearning",
        "machine learning": "machinelearning",
        "ai":               "artificialintelligence",
        "artificial intelligence": "artificialintelligence",
        "dl":               "deeplearning",
        "deep learning":    "deeplearning",
        "cloud":            "cloud aws azure",
        "api":              "rest api",
        "apis":             "rest api",
    }

    def normalize(skill_string):
        tokens = [s.strip().lower() for s in skill_string.replace(",", " ").split() if s.strip()]
        result = []
        seen = set()
        for token in tokens:
            for sub in synonyms.get(token, token).split():
                if sub not in seen:
                    seen.add(sub)
                    result.append(sub)
        return " ".join(result)

    df['skills_normalized'] = df['skills'].apply(normalize)

    print("\nUSER INPUT")
    user_input = input("Enter your skills (comma-separated):\n")

    user_skills = list(dict.fromkeys(normalize(user_input).split()))

    if not user_skills:
        print("No valid skills entered. Exiting.")
        return

    print("\nNORMALIZED SKILLS")
    print(", ".join(user_skills))

    # ---- Calculate Similarity ----
    vectorizer   = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['skills_normalized'])
    user_vector  = vectorizer.transform([" ".join(user_skills)])

    cosine_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    user_set = set(user_skills)
    coverage_scores = []
    matched_counts  = []

    for _, row in df.iterrows():
        role_skills = set(row['skills_normalized'].split())
        matched = role_skills & user_set
        coverage = len(matched) / len(role_skills) if role_skills else 0
        coverage_scores.append(coverage)
        matched_counts.append(len(matched))

    df['cosine_score']   = cosine_scores
    df['coverage_score'] = coverage_scores
    df['matched_count']  = matched_counts
    df['final_score']    = 0.7 * df['cosine_score'] + 0.3 * df['coverage_score']

    df_sorted = df.sort_values(by='final_score', ascending=False).reset_index(drop=True)
    df_sorted['display_name'] = df_sorted['role'].apply(lambda r: display_names.get(r, r))

    top_5 = df_sorted.head(5).copy()

    # ---- Generate Recommendations ----
    print("\nTOP 5 RECOMMENDATIONS")

    for i, row in top_5.iterrows():
        role_display = row['display_name']
        role_name    = row['role']
        direction    = career_directions.get(role_name, "Technology")

        # Match original skill names for display
        role_skills_orig = [s.strip() for s in row['skills'].split(",") if s.strip()]
        matching = [s for s in role_skills_orig if set(normalize(s).split()).issubset(user_set)]
        missing  = [s for s in role_skills_orig if s not in matching]

        print(f"\nRecommended Role  →  {role_display}")
        print(f"Match Score       →  {row['final_score'] * 100:.1f}%")
        print(f"Matched Skills    →  {len(matching)}/{len(role_skills_orig)}")

        print("\nYou Already Know:")
        if matching:
            for s in matching:
                display_s = "Machine Learning" if s == "MachineLearning" else s
                print(f"  {display_s}")
        else:
            print("  (None)")

        print("\nNext Skills To Learn:")
        if missing:
            for idx, s in enumerate(missing, start=1):
                display_s = "Machine Learning" if s == "MachineLearning" else s
                print(f"  {idx}. {display_s}")
        else:
            print("  (None — all skills matched!)")

        print(f"\nCareer Direction:")
        print(f"  {direction}")

    # ---- Final Recommendation Summary ----
    best = top_5.iloc[0]
    best_role  = best['display_name']
    best_role_name = best['role']
    best_score = best['final_score']
    best_direction = career_directions.get(best_role_name, "Technology")

    best_role_skills_orig = [s.strip() for s in best['skills'].split(",") if s.strip()]
    best_matching = [s for s in best_role_skills_orig if set(normalize(s).split()).issubset(user_set)]
    best_missing  = [s for s in best_role_skills_orig if s not in best_matching]

    # Most valuable skills = user skills that matched the best role
    valuable_skills = best_matching if best_matching else user_skills

    print("\nFINAL SUGGESTION")
    print(f"\nBest Match:")
    print(f"  {best_role}")
    print(f"\nReason:")
    if best_matching:
        print(f"  Your current skills align strongly with this role.")
        display_matching = ["Machine Learning" if s == "MachineLearning" else s for s in best_matching]
        print(f"  You already know: {', '.join(display_matching)}.")
    else:
        print(f"  This role has the highest overall compatibility score.")
    
    print(f"\nSuggested Learning Roadmap:")
    if best_missing:
        missing_display = ["Machine Learning" if s == "MachineLearning" else s for s in best_missing]
        print(f"  {missing_display[0]}")
        for s in missing_display[1:4]: # limit to a few next steps
            print(f"  → {s}")
    else:
        print(f"  All skills already matched")

    print(f"\nEstimated Readiness:")
    readiness_pct = best_score * 100
    if readiness_pct < 35:
        readiness_label = "Beginner"
    elif readiness_pct < 65:
        readiness_label = "Intermediate"
    else:
        readiness_label = "Strong Match"
    print(f"  {readiness_label} ({readiness_pct:.1f}%)")

    print(f"\nMost Valuable Skills:")
    for s in valuable_skills:
        display_s = "Machine Learning" if s == "MachineLearning" else s
        print(f"  {display_s}")

    # ---- Generate Graphs ----
    os.makedirs("graphs", exist_ok=True)

    # GRAPH 1: Top 5 Career Recommendations (horizontal bar) → career_scores.png
    top_5_rev = top_5.iloc[::-1].copy()
    scores    = (top_5_rev['final_score'] * 100).round(1)
    labels    = [f"{s:.1f}%" for s in scores]

    plt.figure(figsize=(9, 5))
    bars = plt.barh(top_5_rev['display_name'], scores)
    for bar, label in zip(bars, labels):
        plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                 label, va='center', fontsize=10)
    plt.title("Top Career Recommendations")
    plt.xlabel("Match Score (%)")
    plt.xlim(0, 115)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("graphs/career_scores.png", dpi=200)
    plt.close()

    # GRAPH 2: Skill Match Matrix (heatmap) → skills_match.png
    all_skills = sorted(set(
        s for _, row in top_5.iterrows()
        for s in row['skills_normalized'].split()
    ))

    matrix_data = []
    for _, row in top_5.iterrows():
        role_skill_set = set(row['skills_normalized'].split())
        matrix_data.append([1 if s in role_skill_set and s in user_set else 0 for s in all_skills])

    matrix_df = pd.DataFrame(matrix_data, index=top_5['display_name'].tolist(), columns=all_skills)

    plt.figure(figsize=(12, 5))
    sns.heatmap(matrix_df, annot=True, fmt='d', linewidths=0.5, cbar=False)
    plt.title("Skill Match Matrix")
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(rotation=0, fontsize=10)
    plt.tight_layout()
    plt.savefig("graphs/skills_match.png", dpi=200)
    plt.close()

    # GRAPH 3: Skills Gap Chart (grouped horizontal bars) → skills_gap.png
    gap_roles    = top_5['display_name'].tolist()[::-1]
    matched_vals = []
    learn_vals   = []

    for _, row in top_5.iloc[::-1].iterrows():
        role_skills_orig = [s.strip() for s in row['skills'].split(",") if s.strip()]
        m  = sum(1 for s in role_skills_orig if set(normalize(s).split()).issubset(user_set))
        ms = len(role_skills_orig) - m
        matched_vals.append(m)
        learn_vals.append(ms)

    y      = np.arange(len(gap_roles))
    height = 0.35

    plt.figure(figsize=(9, 5))
    plt.barh(y - height / 2, matched_vals, height, label='Matched Skills')
    plt.barh(y + height / 2, learn_vals,   height, label='Skills To Learn')
    plt.yticks(y, gap_roles)
    plt.xlabel("Number of Skills")
    plt.title("Skills Gap Analysis")
    plt.legend()
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("graphs/skills_gap.png", dpi=200)
    plt.close()

    # ---- Graph Summary ----
    print("\nGRAPH OUTPUT")
    print("  1. graphs/career_scores.png")
    print("  2. graphs/skills_match.png")
    print("  3. graphs/skills_gap.png")
    print("\nProject completed successfully.")

if __name__ == "__main__":
    main()
