# whereRequest
You can freely set the export IP for the request or use a proxy server to make the request.
## Function
- Send requests by binding to a specified IP address on the local machine (using the SourceAddressAdapter of requests+requests toolbelt).
- Send requests through SOCKS5 proxy (set through requests.Session(). proxies).
- Provide the 'EditRequests' class that can be directly imported and called, as well as an example CLI script' example. py '.

## Installation

Recommend using a virtual environment (venv):

PowerShell (Windows) Example:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt