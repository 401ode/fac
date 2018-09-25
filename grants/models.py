from django.db import models


class Grant(models.Model):
    """

    """
    state_agency = models.ForeignKeyField(
        'StateAgency',
        required=True,
        on_delete=models.CASCADE
    )
    awarding_federal_agency = models.ForeignKeyField(
        'FederalAgency',
        required=True,
        on_delete=models.CASCADE
    )


class Award(models.Model):
    """

    """
    grant = models.ForeignKeyField(
        'Grant'
    )
    project_period_start_date = models.DateField(
        'Project Period Start Date',
    )


class Task(models.Model):
    """

    """
    award
