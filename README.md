# secrets-test
Repo for testing handling of secretes i Python, R and with GitHub Actions.

## Usage
Create a `.env` file in the same directory as the secrets-test.py script and
with some content like:
```dotenv
SECRET_KEY=v%)9n7kg^65(4-uir6!pa@oqqsdn8agv9h8
DOMAIN=tester.org
EMAIL=admin@${DOMAIN}
```

Run the script:
```shell
secrets-test.py
```
