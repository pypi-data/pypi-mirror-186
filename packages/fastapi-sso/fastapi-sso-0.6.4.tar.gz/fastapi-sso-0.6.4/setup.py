# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_sso', 'fastapi_sso.sso']

package_data = \
{'': ['*']}

install_requires = \
['fastapi<1',
 'httpx>=0.23.0,<0.24.0',
 'oauthlib>=3.1.0',
 'pydantic>=1.8.1',
 'starlette>=0.13.6']

setup_kwargs = {
    'name': 'fastapi-sso',
    'version': '0.6.4',
    'description': 'FastAPI plugin to enable SSO to most common providers (such as Facebook login, Google login and login via Microsoft Office 365 Account)',
    'long_description': '# FastAPI SSO\n\nFastAPI plugin to enable SSO to most common providers (such as Facebook login, Google login and login via Microsoft Office 365 account).\n\nThis allows you to implement the famous `Login with Google/Facebook/Microsoft` buttons functionality on your backend very easily.\n\n## Support this project\n\nIf you\'d like to support this project, consider [buying me a coffee ☕](https://www.buymeacoffee.com/tomas.votava).\nI tend to process Pull Requests faster when properly caffeinated 😉.\n\n<a href="https://www.buymeacoffee.com/tomas.votava" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>\n\n## Supported login providers\n\n### Official\n\n- Google\n- Microsoft\n- Facebook\n- Spotify\n- Fitbit\n- Github (credits to [Brandl](https://github.com/Brandl) for hint using `accept` header)\n- generic (see [docs](https://tomasvotava.github.io/fastapi-sso/sso/generic.html))\n\n### Contributed\n\n- Kakao (by Jae-Baek Song - [thdwoqor](https://github.com/thdwoqor))\n\nSee [Contributing](#contributing) for a guide on how to contribute your own login provider.\n\n## Installation\n\n### Install using `pip`\n\n```console\npip install fastapi-sso\n```\n\n### Install using `poetry`\n\n```console\npoetry add fastapi-sso\n```\n\n## Example\n\nFor more examples, see [`examples`](/examples/) directory.\n\n### `example.py`\n\n```python\n"""This is an example usage of fastapi-sso.\n"""\n\nfrom fastapi import FastAPI\nfrom starlette.requests import Request\nfrom fastapi_sso.sso.google import GoogleSSO\n\napp = FastAPI()\n\ngoogle_sso = GoogleSSO("my-client-id", "my-client-secret", "https://my.awesome-web.com/google/callback")\n\n@app.get("/google/login")\nasync def google_login():\n    """Generate login url and redirect"""\n    return await google_sso.get_login_redirect()\n\n\n@app.get("/google/callback")\nasync def google_callback(request: Request):\n    """Process login response from Google and return user info"""\n    user = await google_sso.verify_and_process(request)\n    return {\n        "id": user.id,\n        "picture": user.picture,\n        "display_name": user.display_name,\n        "email": user.email,\n        "provider": user.provider,\n    }\n```\n\nRun using `uvicorn example:app`.\n\n### Specify `redirect_uri` on request time\n\nIn scenarios you cannot provide the `redirect_uri` upon the SSO class initialization, you may simply omit\nthe parameter and provide it when calling `get_login_redirect` method.\n\n```python\n...\n\ngoogle_sso = GoogleSSO("my-client-id", "my-client-secret")\n\n@app.get("/google/login")\nasync def google_login(request: Request):\n    """Generate login url and redirect"""\n    return await google_sso.get_login_redirect(redirect_uri=request.url_for("google_callback"))\n\n@app.get("/google/callback")\nasync def google_callback(request: Request):\n    ...\n```\n\n### Specify scope\n\nSince `0.4.0` you may specify `scope` when initializing the SSO class.\n\n```python\nfrom fastapi_sso.sso.microsoft import MicrosoftSSO\n\nsso = MicrosoftSSO(client_id="client-id", client_secret="client-secret", scope=["openid", "email"])\n```\n\n### Additional query parameters\n\nSince `0.4.0` you may provide additional query parameters to be\nsent to the login screen.\n\nE.g. sometimes you want to specify `access_type=offline` or `prompt=consent` in order for\nGoogle to return `refresh_token`.\n\n```python\nasync def google_login(request: Request):\n    return await google_sso.get_login_redirect(\n        redirect_uri=request.url_for("google_callback"),\n        params={"prompt": "consent", "access_type": "offline"}\n        )\n\n```\n\n## HTTP and development\n\n**You should always use `https` in production**. But in case you need to test on `localhost` and do not want to\nuse self-signed certificate, make sure you set up redirect uri within your SSO provider to `http://localhost:{port}`\nand then add this to your environment:\n\n```bash\nOAUTHLIB_INSECURE_TRANSPORT=1\n```\n\nAnd make sure you pass `allow_insecure_http = True` to SSO class\' constructor, such as:\n\n```python\ngoogle_sso = GoogleSSO("client-id", "client-secret", allow_insecure_http=True)\n```\n\nSee [this issue](https://github.com/tomasvotava/fastapi-sso/issues/2) for more information.\n\n## State\n\nState is useful if you want the server to return something back to you to help you understand in what\ncontext the authentication was initiated. It is mostly used to store the url you want your user to be redirected\nto after successful login. You may use `.state` property to get the state returned from the server.\n\nExample:\n\n```python\nfrom fastapi import Request\nfrom fastapi.responses import RedirectResponse\n\n# E.g. https://example.com/auth/login?return_url=https://example.com/welcome\nasync def google_login(return_url: str):\n    google_sso = GoogleSOO("client-id", "client-secret")\n    # Send return_url to Google as a state so that Google knows to return it back to us\n    return await google_sso.get_login_redirect(redirect_uri=request.url_for("google_callback"), state=return_url)\n\nasync def google_callback(request: Request):\n    google_sso = GoogleSOO("client-id", "client-secret")\n    user = await google_sso.verify_and_process(request)\n    # google_sso.state now holds your return_url (https://example.com/welcome)\n    return RedirectResponse(google_sso.state)\n\n```\n\n**Deprecation Warning**: legacy `use_state` argument in `SSOBase` constructor is deprecated and will be removed.\n\n## Contributing\n\nIf you\'d like to contribute and add your specific login provider, please see [CONTRIBUTING.md](CONTRIBUTING.md) file.\n',
    'author': 'Tomas Votava',
    'author_email': 'info@tomasvotava.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tomasvotava.github.io/fastapi-sso/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
