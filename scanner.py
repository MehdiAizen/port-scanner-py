import nmap

# Création du scanner
scanner = nmap.PortScanner()

# Interface utilisateur
print("🔎 Scanner de Ports Python - Étape 2 (avec services)")
ip = input("👉 Adresse IP à scanner : ")
port_range = input("👉 Plage de ports à scanner (ex: 1-1000) : ")

print(f"\n📡 Scan de {ip} sur les ports {port_range}...\n")

# Lancer le scan avec détection de services (-sV)
scanner.scan(hosts=ip, ports=port_range, arguments='-sV')

# Parcourir les résultats
for host in scanner.all_hosts():
    print(f"📍 Hôte détecté : {host}")
    print(f"🟢 État : {scanner[host].state()}\n")

    for proto in scanner[host].all_protocols():
        print(f"📦 Protocole : {proto}")
        ports = scanner[host][proto].keys()

        for port in sorted(ports):
            état = scanner[host][proto][port]['state']
            service = scanner[host][proto][port].get('name', 'inconnu')
            version = scanner[host][proto][port].get('version', '')
            print(f"➡️ Port {port} : {état} | Service : {service} {version}")
