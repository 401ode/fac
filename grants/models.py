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

    project_period_start_date = models.DateField(
        'Project Period Start Date',
        required=True
    )

    project_period_end_date = models.DateField(
        'Project Period End Date',
    )


class Award(models.Model):
    """

    """
    grant = models.ForeignKeyField(
        'Grant'
    )

    budget_period_start_date = models.DateField(
        'Budget Period Start Date'
    )

    budget_period_end_date = models.DateField(
        'Budget Period End Date'
    )


class Task(models.Model):
    """

    """
    award = models.ForeignKeyField(
        'Award'
    )
