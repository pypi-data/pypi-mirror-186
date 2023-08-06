def test_package_import():
    import botcity.plugins.csv as plugin
    assert plugin.__file__ != ""
