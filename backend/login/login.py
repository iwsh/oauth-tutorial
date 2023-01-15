from fastapi import HTTPException, Response, APIRouter
from pydantic import BaseModel
import jwt
import os
import requests


class LoginOauthRequest(BaseModel):
    code: str

class GithubOauth:
    router = APIRouter()
    client_id = os.getenv("GITHUB_CLIENT_ID")
    client_secret = os.getenv("GITHUB_CLIENT_SECRET")

    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.router.add_api_route("/login/oauth/github", self.login, methods=["POST"])

    def login(self, request: LoginOauthRequest, response: Response):
        code = request.code
        print(code)
        print(self.client_id)
        print(self.client_secret)
        # 認証が成功した場合は、JWTトークンを生成して返却します。
        try:
            token = self.getGithubToken(code)
            print(token)
            user = self.getGithubUser(token)
            username, avatar_url = user["login"], user["avatar_url"]
            print(username)
            
            payload = {"username": username}
            token = jwt.encode(payload, self.secret_key, algorithm='HS256')

            # JWTトークンをcookieとして設定します。
            response.set_cookie(key="access_token", value=token)
            return {
                "message": "login successfully",
                "username": username,
                "avatar_url": avatar_url,
            }
        except Exception as e:
            print(e)
            raise HTTPException(status_code=401, detail="Invalid code")

    def getGithubToken(self, code: str) -> str:
        url = "https://github.com/login/oauth/access_token"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code
        }

        response = requests.post(url, headers=headers, json=data).json()
        print(response)
        return response["access_token"]

    def getGithubUser(self, token: str) -> str:
        url = "https://api.github.com/user"
        headers = {
            "Authorization": "Bearer {}".format(token),
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        response = requests.get(url, headers=headers).json()
        print(response)
        return response

