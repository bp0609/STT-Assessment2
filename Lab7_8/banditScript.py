import subprocess
import os
import json
from datetime import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt

# List of repositories to analyze
REPOS = [
    "https://github.com/django/django",
    "https://github.com/pallets/flask",
    "https://github.com/open-telemetry/opentelemetry-python-contrib"
]

WORK_DIR = os.path.expanduser("~/Downloads/Lab7_8/bandit_lab")
REPO_DIR = os.path.join(WORK_DIR, "repos")
RESULTS_DIR = os.path.join(WORK_DIR, "results")
os.makedirs(REPO_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

def setup_environment():
    """Install required tools in a virtual environment"""
    venv_path = os.path.join(WORK_DIR, "bandit-env")
    if not os.path.exists(venv_path):
        subprocess.run(["python", "-m", "venv", venv_path], check=True)
        subprocess.run([os.path.join(venv_path, "bin", "pip"), "install", "bandit"], check=True)

def clone_repository(repo_url):
    """Clone repository if not already exists"""
    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join(REPO_DIR, repo_name)
    if not os.path.exists(repo_path):
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    return repo_path

def get_commits(repo_path, num_commits=100):
    """Get last n non-merge commits with dates"""
    os.chdir(repo_path)
    try:
        subprocess.run(["git", "checkout", "main"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run(["git", "checkout", "master"], check=True)
    
    log_format = "%H||%cd"
    commits = subprocess.check_output(
        ["git", "log", "--no-merges", f"-n{num_commits}", f"--pretty=format:{log_format}", "--date=iso"]
    ).decode().splitlines()
    
    return [{
        "hash": c.split("||")[0],
        "date": datetime.strptime(c.split("||")[1], "%Y-%m-%d %H:%M:%S %z")
    } for c in commits]

def analyze_commit(repo_path, commit):
    """Run Bandit on a specific commit"""
    os.chdir(repo_path)
    subprocess.run(["git", "checkout", "-f", commit["hash"]], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    try:
        result = subprocess.run(
            ["bandit", "-r", ".", "-f", "json", "-q"],
            capture_output=True,
            text=True,
            timeout=300  # 5 minutes per commit
        )
        print(f"Bandit analysis of {commit['hash']} completed")
        # Save the json file
        with open(f"{commit['hash']}.json", "w") as f:
            f.write(result.stdout)
        return json.loads(result.stdout) if result.stdout else {}
    except json.JSONDecodeError:
        return {}
    except subprocess.TimeoutExpired:
        print(f"Timeout analyzing {commit['hash']}")
        return {}

def process_repository(repo_url):
    """Process all commits in a repository"""
    repo_path = clone_repository(repo_url)
    repo_name = repo_url.split("/")[-1]
    output_file = os.path.join(RESULTS_DIR, f"{repo_name}_results.csv")
    
    if os.path.exists(output_file):
        return
    
    commits = get_commits(repo_path)
    results = []
    
    for commit in commits:
        report = analyze_commit(repo_path, commit)
        if not report:
            continue
        metrics = {
            "commit_hash": commit["hash"],
            "commit_date": commit["date"].isoformat(),
            "high_confidence": 0,
            "medium_confidence": 0,
            "low_confidence": 0,
            "high_severity": 0,
            "medium_severity": 0,
            "low_severity": 0,
            "cwes": set()
        }
        
        for finding in report.get("results", []):
            # Confidence metrics
            if finding["issue_confidence"] == "HIGH":
                metrics["high_confidence"] += 1
            elif finding["issue_confidence"] == "MEDIUM":
                metrics["medium_confidence"] += 1
            else:
                metrics["low_confidence"] += 1
            
            # Severity metrics
            if finding["issue_severity"] == "HIGH":
                metrics["high_severity"] += 1
            elif finding["issue_severity"] == "MEDIUM":
                metrics["medium_severity"] += 1
            else:
                metrics["low_severity"] += 1
            
            # CWE tracking
            if finding.get("issue_cwe"):
                metrics["cwes"].add(finding["issue_cwe"]["id"])
        
        metrics["cwes"] = ";".join(map(str, metrics["cwes"]))
        results.append(metrics)
        print(results[-1])

    with open(output_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

def generate_reports():
    """Generate aggregated reports and visualizations"""
    all_data = []
    
    # Combine all repository data
    for result_file in os.listdir(RESULTS_DIR):
        if result_file.endswith("_results.csv"):
            df = pd.read_csv(os.path.join(RESULTS_DIR, result_file))
            df["repo"] = result_file.replace("_results.csv", "")
            all_data.append(df)
    
    combined_df = pd.concat(all_data)
    combined_df["commit_date"] = pd.to_datetime(combined_df["commit_date"])
    
    # RQ1: High severity over time
    plt.figure(figsize=(12, 6))
    for repo, group in combined_df.groupby("repo"):
        group = group.sort_values("commit_date")
        plt.plot(group["commit_date"], group["high_severity"], label=repo)
    plt.title("RQ1: High Severity Vulnerabilities Over Time")
    plt.xlabel("Commit Date")
    plt.ylabel("High Severity Count")
    plt.legend()
    plt.savefig(os.path.join(RESULTS_DIR, "rq1_high_severity_trend.png"))
    
    # RQ3: CWE frequency
    cwe_counts = combined_df["cwes"].str.split(";", expand=True).stack().value_counts()
    cwe_counts.head(10).plot(kind="bar", figsize=(12, 6))
    plt.title("RQ3: Top 10 Most Frequent CWEs")
    plt.xlabel("CWE ID")
    plt.ylabel("Count")
    plt.savefig(os.path.join(RESULTS_DIR, "rq3_top_cwes.png"))
    
    # Save aggregated data
    combined_df.to_csv(os.path.join(RESULTS_DIR, "combined_results.csv"), index=False)

if __name__ == "__main__":
    setup_environment()
    for repo in REPOS:
        print(f"Processing {repo}")
        process_repository(repo)
    generate_reports()
    print("Analysis complete. Results saved to:", RESULTS_DIR)