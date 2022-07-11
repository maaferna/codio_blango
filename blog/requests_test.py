import requests

# put your real credentials here
EMAIL_ADDRESS = "ben@example.com"
PASSWORD = "password"
BASE_URL = "http://127.0.0.1:8000/"

anon_post_resp = requests.get(BASE_URL + "api/v1/posts/")
anon_post_resp.raise_for_status()

anon_post_count = anon_post_resp.json()["count"]
print(f"Anon users have {anon_post_count} post{'' if anon_post_count == 1 else 's'}")

auth_resp = requests.post(
    BASE_URL + "api/v1/token-auth/",
    json={"username": EMAIL_ADDRESS, "password": PASSWORD},
)
auth_resp.raise_for_status()
token = auth_resp.json()["token"]

# Use the token in a request
authed_post_resp = requests.get(
    BASE_URL + "api/v1/posts/", headers={"Authorization": f"Token {token}"}
)
authed_post_count = authed_post_resp.json()["count"]

print(
    f"Authenticated user has {authed_post_count} post{'' if authed_post_count == 1 else 's'}"
)

# Since requests doesn't remember headers between requests, this next request is unauthenticated again
anon_post_resp = requests.get(BASE_URL + "api/v1/posts/")