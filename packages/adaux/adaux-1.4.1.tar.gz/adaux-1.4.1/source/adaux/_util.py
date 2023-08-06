# Copyright (c) 2021-2023 Mario S. Könz; License: MIT
import dataclasses as dc
import json
import typing as tp

import requests


@dc.dataclass
class ApiRequestCommunicator:
    base_url: str = dc.field(init=False)
    headers: tp.Dict[str, str] = dc.field(init=False)

    def url(self, *args: str) -> str:
        root = (self.base_url,)
        return "/".join(map(str, root + args))

    def api(self, *args: tp.Any) -> str:
        return self.url("api", "v4", *args)

    def api_request(self, *args: tp.Any, mode: str = "get", **kwgs: tp.Any) -> tp.Any:
        url = self.api(*args)
        if mode == "get":
            assert not kwgs
            return self.get_request(url)
        if mode == "put":
            return self.put_request(url, json=kwgs)
        if mode == "post":
            return self.post_request(url, json=kwgs)
        if mode == "delete":
            return self.delete_request(url)

        raise NotImplementedError(mode)

    def graphql(self, *args: tp.Any) -> str:
        # https://gitlab.com/-/graphql-explorer
        return self.url("api", "graphql", *args)

    def graphql_request(
        self, mode: str = "get", **kwgs: tp.Any
    ) -> tp.Dict[str, tp.Any]:
        url = self.graphql()
        if mode == "get":
            return self.get_request(url, json=kwgs)
        raise NotImplementedError(mode)

    def get_request(self, url: str, **kwgs: tp.Any) -> tp.Dict[str, tp.Any]:
        req = requests.get(url, headers=self.headers, timeout=1, **kwgs)
        if req.status_code != 200:
            raise RuntimeError(f"{req} {req.text}")
        return json.loads(req.text)  # type: ignore

    def put_request(self, url: str, **kwgs: tp.Any) -> tp.Dict[str, tp.Any]:
        req = requests.put(url, headers=self.headers, timeout=1, **kwgs)
        self.assert_with_debug(req, 200)
        return json.loads(req.text)  # type: ignore

    def post_request(self, url: str, **kwgs: tp.Any) -> tp.Dict[str, tp.Any]:
        req = requests.post(url, headers=self.headers, timeout=3, **kwgs)
        self.assert_with_debug(req, 201)
        return json.loads(req.text)  # type: ignore

    def delete_request(self, url: str, **kwgs: tp.Any) -> tp.Dict[str, tp.Any]:
        req = requests.delete(url, headers=self.headers, timeout=1, **kwgs)
        self.assert_with_debug(req, 204)
        return {}

    @classmethod
    def assert_with_debug(cls, req: tp.Any, code: int) -> None:
        if req.status_code != code:
            print(req, req.text)
            assert req.status_code == code
