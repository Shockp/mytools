#!/usr/bin/env python3

import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

NS = dr.Resolver()

subdomains = []

def AXFR(domain, nameserver):
    try:
        axfr = dz.from_xfr(dq.xfr(domain, nameserver))

        if axfr:
            print("[*] Successful zone transfer {}".format(nameserver))

            for record in axfr:
                    subdomains.append('{}.{}'.format(record.to_text(), domain))

    except Exception as error:
        print(error)
        pass

if __name__=="__main__":

    parser = argparse.ArgumentParser(prog="dns-axfr.py", epilog="DNS Zone Transfer Script", usage="dns-axfr.py [options] -d <DOMAIN>", prefix_chars="-", add_help=True)

    parser.add_argument("-d", action="store", metavar="domain", type=str, help='Target Domain.\tExample: test.com')
    parser.add_argument("-n", action="store", metavar="nameserver", type=str, help="Nameservers separated by a comma.\tExample: ns1.test.com,ns2.test.com")
    parser.add_argument("-v", action="version", version="axfr v1.0", help="Print the version of dns-axfr.py")

    args = parser.parse_args()

    domain = args.d
    NS.nameservers = args.n.split(",")

    if not args.d:
         print("[!] You must specify a target domain.\n")
         print(parser.print_help())
         exit()

    if not args.n:
         print("[!] You must specify the nameservers.\n")
         print(parser.print_help())
         exit()
         

    for nameserver in NS.nameservers:
         
         AXFR(domain, nameserver)

    if subdomains is not None:
         print('-------- Found Subdomains:')

         for subdomain in subdomains:
              print('{}'.format(subdomain))

    else:
         print("No subdomains found.")
