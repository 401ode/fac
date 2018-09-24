from django.db import models


# TODO: Handle addresses as separate model.

class Organization(models.Model):
    """
    Macro Organization class, from which agencies will inherit.   
    """
    org_name = models.CharField(max_length=128)

    class Meta():
        abstract = True

    def __str__(self):
        return self.org_name[:50]


class FederalAgency(Organization):
    """
    TODO: Establish parent-agency hierarchy, logically based on federal_hierarchy_level.
    Fields:
        cgac_code = "Common Government-wide Accounting Classification" code.
        federal_hierarchy_level = Federal Hierarchy Level, as determined by beta.SAM.gov.
    """
    HIERARCHY = (
        ('department', 'Department/Ind. Agency'),
        ('sub_tier', 'Sub-tier')
    )

    cgac_code = models.CharField(max_length=3)
    federal_hierarchy_level = models.CharField(
        max_length=10,
        choices=HIERARCHY
    )


class StateAgency(Organization):
    """
    TODO: Establish parent-agency hierarchy.
    """

    agency_code = models.CharField(max_length=2)


class SubRecipient(Organization):
    """

    """
