import requests 
def ratelimit():
  r = requests.head(url="https://discord.com/api/v1")
  try:
      print(f"[🔴] Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
  except:
      print('[🟢] No ratelimit')

global reports
reports=""
def report(text,type=None):
  types = ['suc','fa','att','inf']
  prefix=''
  if type:
    if type in types:
      if type == 'suc':
        prefix="[🟢]"
      elif type== 'fa':
        prefix="[🟠]"
      elif type== "inf":
        prefix="[🔵]"
      else:
        prefix ="[🔴]"
  report = f"{prefix} {text}"
  reports.add(report)
def show_report():
  return reports

theme_color = 0x3EADCF
  