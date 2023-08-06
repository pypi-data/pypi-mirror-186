# We test beaker functionality, although we have no beaker-related code
# anymore. All configuration is done in ZCML snippets in
# site.zcml/ftesting.zcml now.
# The dolmen.beaker package is developed on: https://github.com/trollfot/dolmen.beaker
from dolmen.beaker.interfaces import ISessionConfig
from zope.component import queryUtility
from zope.component.hooks import setSite
from zope.publisher.browser import TestRequest
from zope.session.interfaces import ISession
from waeup.kofa.testing import FunctionalLayer, FunctionalTestCase


class BeakerTests(FunctionalTestCase):
    # Beaker-related tests.

    layer = FunctionalLayer

    def test_beaker_session(self):
        # Make sure we get a beaker session when asking for ISession.
        try:
            import dolmen.beaker
        except ImportError:
            # no beaker installed, no test
            return
        setSite(self.getRootFolder()) # needed to start transaction
        request = TestRequest()
        session = ISession(request)  # this is a Zope session
        self.assertTrue(session.__module__.startswith('dolmen.beaker'))
        self.assertTrue(session.get("_path", None) is not None)
        return

    def test_beaker_session_values(self):
        # Ensure we get also a beaker session
        # (which is part of a Zope session)
        try:
            import dolmen.beaker
        except ImportError:
            # no beaker installed, no test
            return
        setSite(self.getRootFolder()) # needed to start transaction
        config = ISessionConfig
        request = TestRequest()
        session = ISession(request).session
        self.assertEqual(session.__module__, "beaker.session")
        self.assertTrue(session.get("_path", None) is not None)
        return

    def test_beaker_config_accessible(self):
        # The session config is set in site.zcml / ftesting.zcml
        # See beakerSession directive
        # See https://github.com/trollfot/dolmen.beaker/blob/master/src/dolmen/beaker/zcml.py
        # for options
        config = queryUtility(ISessionConfig)
        self.assertEqual(config.get("key"), "waeup.kofa.session.id")
        self.assertEqual(config.get("timeout"), 3600)
