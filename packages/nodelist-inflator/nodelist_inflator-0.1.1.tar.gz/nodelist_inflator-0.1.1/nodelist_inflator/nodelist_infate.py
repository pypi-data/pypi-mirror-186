# Use a regular expression to match the hostnames
import argparse
import re

# Output the full hostnames

def expand_hostnames(hostnames):
    pattern = re.compile(r'([a-zA-Z0-9-]+((\[[\d,-]+\])|(\d+))[,]?)')
    matches = pattern.findall(hostnames)
    expanded = []
    for match in matches:
        hostname = match[0]
        if '[' in hostname:
            hostname = hostname.split('[')[0]
            range_parts = match[1].strip('[]').split(',')
            for part in range_parts:
                if '-' in part:
                    start_range, end_range = map(int,part.split('-'))
                    for i in range(start_range, end_range + 1):
                        expanded.append(f"{hostname}{i}")
                else:
                    expanded.append(f"{hostname}{part}")
        else:
            expanded.append(hostname.rstrip(","))

    return expanded

def cli():
    parser = argparse.ArgumentParser(description='Expand hostnames')
    parser.add_argument("--nodelist", type=str, default="ip-26-0-129-85,ip-26-0-130-171,ip-26-0-137-[14-15,22]", help="List of nodes", required=True)
    parser.add_argument("--write", action="store_true", help="Write expanded hostnames to a hostname file")

    args = parser.parse_args()

    expanded = expand_hostnames(args.nodelist)
    
    if args.write:
        lines = [f"{host} slots=8\n" for host in expanded]
        with open("hostnames", "w") as f:
            f.writelines(lines)
        
if __name__ == "__main__":
    cli()
