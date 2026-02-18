import requests

def search_cve(keyword):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}"
    
    try:
        response = requests.get(url)
        data = response.json()
        results = []

        for vuln in data.get("vulnerabilities", [])[:3]:
            cve_id = vuln["cve"]["id"]
            metrics = vuln["cve"].get("metrics", {})
            severity = "Unknown"

            if "cvssMetricV31" in metrics:
                severity = metrics["cvssMetricV31"][0]["cvssData"]["baseSeverity"]

            results.append({
                "cve_id": cve_id,
                "severity": severity
            })

        return results

    except:
        return []
