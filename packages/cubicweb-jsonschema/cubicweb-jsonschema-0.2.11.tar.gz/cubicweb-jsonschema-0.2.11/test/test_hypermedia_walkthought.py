"""cubicweb-jsonschema unit tests for Pyramid JSON API."""

import base64
from datetime import date
from unittest import skip

import jsonschema
from mock import patch

from cubicweb import Binary, ValidationError
from cubicweb.pyramid.test import PyramidCWTest, TestApp
from pyramid.config import Configurator

from cubicweb_jsonschema import VIEW_ROLE
from cubicweb_jsonschema.entities.ijsonschema import (
    jsonschema_adapter,
)


class TestAppNoCSRF(TestApp):
    """Overloads TestApp to avoid csrf verification
    not implemented in FranceArchives so far.
    """

    def post(
        self,
        route,
        params=None,
        do_not_grab_the_crsf_token=True,
        do_not_inject_origin=True,
        **kwargs,
    ):
        return super(TestAppNoCSRF, self).post(
            route, params, do_not_grab_the_crsf_token, do_not_inject_origin, **kwargs
        )


class BaseTC(PyramidCWTest):

    settings = {
        'cubicweb.bwcompat': False,
        'pyramid.debug_notfound': True,
        'cubicweb.auth.authtkt.session.secret': 'x',
        'cubicweb.auth.authtkt.persistent.secret': 'x',
        'cubicweb.session.secret': 'x',
    }

    def setUp(self):
        super(PyramidCWTest, self).setUp()
        pyramid_config = Configurator(settings=self.settings)

        pyramid_config.registry["cubicweb.repository"] = self.repo
        pyramid_config.include("cubicweb.pyramid")

        self.includeme(pyramid_config)

        self.webapp = TestAppNoCSRF(
            pyramid_config.make_wsgi_app(),
            extra_environ={"wsgi.url_scheme": "https"},
        )

    def includeme(self, config):
        config.include('cubicweb_jsonschema.api')


class HypermediaWalkthoughtTC(BaseTC):

    def test_get_root(self):
        self.login()
        import pdb; pdb.set_trace()
        resp = self.webapp.get("/", headers={'Accept': 'application/json'})
        print(resp)
        assert True


if __name__ == '__main__':
    import unittest
    unittest.main()
