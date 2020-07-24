
from covid import Covid
covid = Covid(source='worldometers')
data = covid.get_data()
countries = covid.get_status_by_country_name('india')
totalDeaths = countries['deaths']
activeCases = covid.get_total_active_cases()
confirmedCases = covid.get_total_confirmed_cases()

    