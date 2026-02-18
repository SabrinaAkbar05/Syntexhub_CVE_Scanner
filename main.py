from scanner import scan_target
from cve_lookup import search_cve
from report import generate_report

def main():
    target = input("Enter target host (e.g. scanme.nmap.org): ")

    services = scan_target(target)

    for service in services:
        if service["banner"]:
            cves = search_cve(service["banner"])
            service["cves"] = cves

    generate_report(target, services)

if __name__ == "__main__":
    main()
