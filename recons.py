import requests
import socket
import ssl
import re
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {"domain": domain, "ip": ip}
    except:
        return {"domain": domain, "ip": None}

def get_headers(url):
    try:
        r = requests.get(url, timeout=10)
        return dict(r.headers)
    except:
        return {}

def detect_tech(headers, body):
    tech = []
    if "x-powered-by" in headers:
        tech.append(headers["x-powered-by"])
    if "server" in headers:
        tech.append(headers["server"])
    if "wp-content" in body:
        tech.append("WordPress")
    if "react" in body.lower():
        tech.append("React")
    if "vue" in body.lower():
        tech.append("Vue")
    return list(set(tech))

def fetch_html(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return ""

def extract_js_files(url, html):
    js_files = re.findall(r'<script[^>]+src=["\'](.*?)["\']', html)
    full = []
    for js in js_files:
        full.append(urljoin(url, js))
    return list(set(full))

def analyze_js(js_url):
    findings = []
    try:
        r = requests.get(js_url, timeout=10)
        data = r.text
        endpoints = re.findall(r'https?://[^\s"\']+', data)
        secrets = re.findall(r'api[_-]?key|token|secret', data, re.IGNORECASE)
        if endpoints:
            findings.append({"type": "endpoint", "data": list(set(endpoints))})
        if secrets:
            findings.append({"type": "suspicious_keywords", "data": list(set(secrets))})
    except:
        pass
    return {js_url: findings}

def get_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(5)
            s.connect((domain, 443))
            cert = s.getpeercert()
            return cert
    except:
        return {}

def check_ports(ip, ports=[80,443,8080,8443,21,22,3306,3307,8000,3308,9999]):
    open_ports = []
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((ip, port))
            open_ports.append(port)
            s.close()
        except:
            pass
    return open_ports

def parse_robots(url):
    try:
        r = requests.get(urljoin(url, "/robots.txt"), timeout=5)
        return r.text.splitlines()
    except:
        return []

def parse_sitemap(url):
    try:
        r = requests.get(urljoin(url, "/sitemap.xml"), timeout=5)
        urls = re.findall(r'<loc>(.*?)</loc>', r.text)
        return urls
    except:
        return []

def subdomain_scan(domain, wordlist):
    found = []
    def check(sub):
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            found.append(subdomain)
        except:
            pass
    with ThreadPoolExecutor(max_workers=20) as ex:
        ex.map(check, wordlist)
    return found

def save_result(result, filename="result_recon.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in result.items():
            f.write(f"=== {key.upper()} ===\n")
            if isinstance(value, dict):
                for k, v in value.items():
                    f.write(f"{k}: {v}\n")
            elif isinstance(value, list):
                for item in value:
                    f.write(f"- {item}\n")
            else:
                f.write(str(value))
            f.write("\n\n")

def run_recon(target):
    if not target.startswith("http"):
        url = "http://" + target
    else:
        url = target

    parsed = urlparse(url)
    domain = parsed.netloc

    result = {}

    dns = resolve_domain(domain)
    result["dns"] = dns

    headers = get_headers(url)
    result["headers"] = headers

    html = fetch_html(url)

    tech = detect_tech(headers, html)
    result["technologies"] = tech

    js_files = extract_js_files(url, html)
    result["js_files"] = js_files

    js_results = []
    for js in js_files:
        js_results.append(analyze_js(js))
    result["js_analysis"] = js_results

    ssl_info = get_ssl_info(domain)
    result["ssl"] = ssl_info

    if dns["ip"]:
        ports = check_ports(dns["ip"])
        result["open_ports"] = ports

    robots = parse_robots(url)
    result["robots"] = robots

    sitemap = parse_sitemap(url)
    result["sitemap"] = sitemap

    wordlist = ["www","mail","dev","test","api","admin"]
    subs = subdomain_scan(domain, wordlist)
    result["subdomains"] = subs

    save_result(result, f"{domain}_recon.txt")

    return result