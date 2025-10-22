import requests
import json

PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI5NWM1ODQ5NS0zYWJiLTRlMjgtYWFhNi05YWVlOWJiODBlMmQiLCJlbWFpbCI6ImVya3Vhbi53YW5nQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiJhOTk5NTJjNzZiMWZkMTU2N2ExZCIsInNjb3BlZEtleVNlY3JldCI6IjgzOTkwMzk3YWY1N2UyODZiZGViNTc1NTdmMDg2MGY5M2Q3Zjc3NGExOWFiZTQ1MjUwOTMxZTY0NzhlZmQ1MWUiLCJleHAiOjE3OTI3MTI0MTV9.n3DkvgzCvDNEQOuYfOi-YTwuTuyxAMlRwMgLgXkzz4k"
# Pinata API base URL
PINATA_BASE_URL = "https://api.pinata.cloud"

def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"

    # Convert dictionary to JSON string
    json_data = json.dumps(data)

    # Pinata JSON upload endpoint
    url = f"{PINATA_BASE_URL}/pinning/pinJSONToIPFS"

    headers = {
        "Authorization": f"Bearer {PINATA_JWT}",
        "Content-Type": "application/json"
    }

    # Send request
    response = requests.post(url, headers=headers, data=json_data)

    # Extract the IPFS CID
    cid = response.json()["IpfsHash"]
    return cid




def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"

    # Retrieve from public gateway (works for any CID)
    response = requests.get(f"https://gateway.pinata.cloud/ipfs/{cid}")

    data = response.json()
    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data
