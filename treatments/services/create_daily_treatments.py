from django.utils import timezone
from treatments.models import DailyTreatment

def create_daily_treatments(treatment):
    start_date = treatment.start_date
    end_date = treatment.end_date
    daily_treatments = []

    current_date = start_date
    while current_date <= end_date:
        daily_treatment = DailyTreatment.objects.create(
            id_treatment=treatment,
            date=current_date
        )
        daily_treatments.append(daily_treatment)
        current_date += timezone.timedelta(days=1)

    return daily_treatments
