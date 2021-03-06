from django.db import models


# TODO: Handle addresses as separate model.

class Organization(models.Model):
    """
    Macro Organization class, from which agencies will inherit.   
    """
    org_name = models.CharField("Organization Name",
                                max_length=128)
    org_url = models.URLField("Main Organization URL",
                              blank=True,
                              default='')

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

    cgac_code = models.CharField("CGAC Code", max_length=3)
    federal_hierarchy_level = models.CharField(
        "Federal Hierarchy Level",
        max_length=10,
        choices=HIERARCHY,
        default='department'
    )

    class Meta:
        verbose_name_plural = 'Federal Agencies'


class StateAgency(Organization):
    """
    TODO: Establish parent-agency hierarchy.
    TODO: Establish agency type (exec, quasi, etc.)
    """

    agency_code = models.CharField("RIFANS Agency Code",
                                   max_length=2,
                                   blank=True,
                                   default='')
    duns_number = models.CharField("DUNS Number",
                                   max_length=14,
                                   blank=True,
                                   default='')

    class Meta:
        verbose_name_plural = 'State Agencies'


class SubRecipient(Organization):
    """
    A recipient of State grant money. 
    """
    duns_number = models.CharField("DUNS Number",
                                   max_length=14,
                                   blank=True,
                                   default='')

    class Meta:
        verbose_name_plural = 'Sub-Recipients'


class LineSequence(models.Model):
    """

    """
    state_agency = models.ForeignKeyField('StateAgency',
                                          required=True,
                                          on_delete=models.CASCADE)
    line_sequence_number = models.CharField()


class IndirectRate(models.Model):
    """

    """
    state_agency = models.ForeignKeyField('StateAgency',
                                          required=True,
                                          on_delete=models.CASCADE)
    rate_percentage = models.DecimalField(
        "Indirect Rate",
        max_digits=4,
        decimal_places=3
    )
    rate_start_date = models.DateField("Rate Start Date")
    rate_end_date = models.DateField("Rate End Date")
    rate_type = models.CharField(
        "Rate Type",
        max_length=32
    )
