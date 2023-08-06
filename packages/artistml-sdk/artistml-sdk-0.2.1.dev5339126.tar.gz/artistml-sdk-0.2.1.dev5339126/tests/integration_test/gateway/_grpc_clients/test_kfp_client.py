import re

import requests
from kfp import compiler
from kfp import dsl

from artistml_sdk.gateway import kfp_client
from artistml_sdk.lib import config

kfp_host = config.test.get_val(
    "kfp",
    "host",
)
kfp_port = config.test.get_val(
    "kfp",
    "port",
)

CLUSTER_IP = "kubeflow.platform.artistml.com"
AUTH_IP = "auth.platform.artistml.com"


def get_authservice_session_when_multiuser() -> str:
    response = requests.get(f"https://{CLUSTER_IP}")
    response_text = response.text
    # print("response_text", response_text)
    # //Extract the request token REQ_VALUE as done in step
    action_uri = re.search('action="/(login[^"]+)"', response_text).group(1)
    action_uri = action_uri.replace("&amp;", "&")
    state = action_uri.split("state=")[-1]
    # print("req_token", req_token)
    creds = {'username': 'artistml2022', 'password': 'Artistml@2022'}
    response = requests.post(
        f"https://{AUTH_IP}/{action_uri}",
        data=creds,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )
    code = response.history[-1].cookies.get("XSRF-TOKEN")
    print(
        "auth:", state, code,
        f"https://{CLUSTER_IP}/oauth2/idpresponse?code={code}&state={state}")
    response = requests.get(
        f"https://{CLUSTER_IP}/oauth2/idpresponse?code={code}&state={state}", )
    print("response.history", len(response.history))
    for i, h in enumerate(response.history):
        print("response.history.cookies", i, h.cookies)
    # // Cookie was set in the last redirection, hence we need to fetch that from response.history
    cookie = "authservice_session=" + response.history[-1].cookies.get(
        'authservice_session')
    return cookie


# cookies=get_authservice_session_when_multiuser(),
kfp_client.set_endpoint(endpoint=f"http://{kfp_host}:{kfp_port}", )


@dsl.component
def addition_component(num1: int, num2: int) -> int:
    return num1 + num2


@dsl.pipeline(name='addition-pipeline')
def my_pipeline(a: int, b: int, c: int = 10):
    add_task_1 = addition_component(num1=a, num2=b)
    add_task_2 = addition_component(num1=add_task_1.output, num2=c)


cmplr = compiler.Compiler()


def test_create_experiment():
    assert kfp_client.api_client.create_experiment(
        name="sylvan-test-1",
        namespace="artistml-2022",
    ).id is not None
    assert len(
        kfp_client.api_client.list_experiments(
            namespace="artistml-2022", ).experiments) > 0
