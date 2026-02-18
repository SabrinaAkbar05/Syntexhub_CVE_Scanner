def generate_report(host, services):
    print("\n===== Vulnerability Scan Report =====")
    print(f"Target: {host}\n")

    for service in services:
        print(f"Port: {service['port']}")
        print(f"Banner: {service['banner']}")
        print("Possible CVEs:")

        for cve in service.get("cves", []):
            print(f" - {cve['cve_id']} ({cve['severity']})")

        print("-----------------------------------")
