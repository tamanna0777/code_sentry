import re

def scan_vulnerabilities(code: str):
    findings = []

    if "eval(" in code:
        findings.append({
            "category": "Unsafe eval",
            "severity": "High"
        })

    return {"findings": findings}