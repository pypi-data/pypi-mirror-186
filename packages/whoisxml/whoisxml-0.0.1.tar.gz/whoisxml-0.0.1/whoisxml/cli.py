from .whoisxml import whoisxmlapi
import argparse

def main():
  parser = argparse.ArgumentParser(description='A wrapper for whoisxml.')
  parser.add_argument("--api", help="Add a whoisxml API", required=True)
  parser.add_argument("--ip", help="Target IP", default="127.0.0.1", required=True)
  args = parser.parse_args()
  whoisxmlapi(ip=args.ip, apiKey=args.api, file_location=f"{args.ip}.txt")

if __name__ == "__main__":
  main()
  