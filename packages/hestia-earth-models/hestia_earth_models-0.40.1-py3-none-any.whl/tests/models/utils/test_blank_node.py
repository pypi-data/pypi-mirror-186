from hestia_earth.schema import SiteSiteType

from hestia_earth.models.utils.blank_node import _run_required, _run_model_required


def test_run_required():
    term = {
        '@id': 'ch4ToAirAquacultureSystems',
        'termType': 'emission'
    }
    assert not _run_required('model', term, {
        'site': {'siteType': SiteSiteType.CROPLAND.value}
    })
    assert _run_required('model', term, {
        'site': {'siteType': SiteSiteType.POND.value}
    }) is True

    term = {
        '@id': 'landTransformationFromCropland20YearAverageDuringCycle',
        'termType': 'resourceUse'
    }
    assert not _run_required('hyde32', term, {
        'site': {'siteType': SiteSiteType.CROPLAND.value}
    })


def test_run_model_required_emission():
    term = {
        '@id': 'n2OToAirExcretaDirect',
        'termType': 'emission'
    }
    assert not _run_model_required('pooreNemecek2018', term, {
        'site': {'siteType': SiteSiteType.POND.value}
    })
    assert _run_model_required('pooreNemecek2018', term, {
        'site': {'siteType': SiteSiteType.CROPLAND.value}
    }) is True


def test_run_model_required_measurement():
    term = {
        '@id': 'netPrimaryProduction',
        'termType': 'measurement'
    }
    assert _run_model_required('pooreNemecek2018', term, {
        'site': {'siteType': SiteSiteType.POND.value}
    }) is True
    assert not _run_model_required('pooreNemecek2018', term, {
        'site': {'siteType': SiteSiteType.CROPLAND.value}
    })
