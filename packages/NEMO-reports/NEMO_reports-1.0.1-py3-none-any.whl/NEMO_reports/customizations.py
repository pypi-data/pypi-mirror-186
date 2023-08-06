from NEMO.decorators import customization
from NEMO.views.customization import CustomizationBase


@customization(title="Reports", key="reports")
class ReportsCustomization(CustomizationBase):
    variables = {"reports_first_day_of_week": "1", "reports_default_daterange": ""}
