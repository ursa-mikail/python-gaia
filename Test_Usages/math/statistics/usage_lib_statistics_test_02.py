
from usage_lib_statistics_support import *

def test_02 (lib_statistics_object):
    chi_square_statistic = lib_statistics_object.compute_chi_square_statistic(observed_data_00)
    print(chi_square_statistic)
    degrees_of_freedom = len(observed_data_00) - 1

    # Step 1: Take the chi-square statistic. Find p-value
    p_value = 1 - stats.chi2.cdf(chi_square_statistic, degrees_of_freedom)
    print(p_value)  # large p-value (92.65%) means that null hypothesis should not be rejected.

    national_table = pd.crosstab(index=national[0], columns="count")
    minnesota_table = pd.crosstab(index=minnesota[0], columns="count")

    print("National")
    national_table_data = np.array((national_table.values).reshape(1, len(national_table.values)))
    national_table_data = national_table_data[0]
    print(national_table_data) #
    print(" ")
    print("Minnesota")
    minnesota_table_data = np.array((minnesota_table.values).reshape(1, len(minnesota_table.values)))
    minnesota_table_data = minnesota_table_data[0]
    print(minnesota_table)
    observed_data = minnesota_table_data
    chi_square_statistic = lib_statistics_object.compute_chi_square_statistic(observed_data)
    print(chi_square_statistic)
    data_population = national_table_data

    chi_square_statistic = lib_statistics_object.compute_chi_square_statistic_given_population_data(observed_data, data_population)
    print("chi_square_statistic: ", chi_square_statistic)

    degrees_of_freedom = len(categories) - 1

    critical_value = stats.chi2.ppf(q=0.95,  # Find the critical value for 95% confidence*
                                df = degrees_of_freedom)  # Df = number of variable categories - 1

    print("Critical value: ", critical_value)
    p_value = 1 - stats.chi2.cdf(x=chi_square_statistic,  # Find the p-value
                             df = degrees_of_freedom)
    print("P value: ", p_value)

    national_ratios = national_table / len(national)  # Get population ratios
    expected = national_ratios * len(minnesota)
    print (stats.chisquare(f_obs = minnesota_table, f_exp = expected))  # Array of observed counts, Array of expected counts

    # ref: http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-25-chi.html
    # Chi-Squared Test of Independence
    np.random.seed(10)

    # Sample data randomly at fixed probabilities
    voter_race = np.random.choice(a=["asian", "black", "hispanic", "other", "white"],
                              p=[0.05, 0.15, 0.25, 0.05, 0.5],
                              size=1000)

    # Sample data randomly at fixed probabilities
    voter_party = np.random.choice(a=["democrat", "independent", "republican"],
                               p=[0.4, 0.2, 0.4],
                               size=1000)

    voters = pd.DataFrame({"race": voter_race,  # axis 1
                       "party": voter_party})   # axis 2

    voter_tab = pd.crosstab(voters.race, voters.party, margins=True)
    voter_tab.columns = ["democrat", "independent", "republican", "row_totals"]
    voter_tab.index = ["asian", "black", "hispanic", "other", "white", "col_totals"]

    observed = voter_tab.ix[0:(len(voter_tab.index ) -1), 0:(len(voter_tab.columns ) -1)]  # Get table without totals for later use
    print(voter_tab)

    expected = np.outer(voter_tab["row_totals"][0:(len(voter_tab.index ) -1)],
                    voter_tab.ix["col_totals"][0:(len(voter_tab.columns ) -1)]) / 1000

    expected = pd.DataFrame(expected)

    expected.columns = ["democrat", "independent", "republican"]
    expected.index = ["asian", "black", "hispanic", "other", "white"]
    print(expected)

    chi_squared_stat = (((observed - expected) ** 2) / expected).sum().sum()
    print(chi_squared_stat)
    degrees_of_freedom = 8
    crit = stats.chi2.ppf(q=0.95,  # Find the critical value for 95% confidence*
                      df = degrees_of_freedom)  # *

    print("Critical value")
    print(crit)

    p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,  # Find the p-value
                             df = degrees_of_freedom)
    print("P value")
    print \
        (p_value)  # given the high p-value, the test result does not detect a significant relationship between the variables.
    results = stats.chi2_contingency(observed=observed)
    print(results)
    # small p-value ( ≤ 0.05) indicates strong evidence against H_0, so reject H_0.
    # large p-value (> 0.05) indicates weak evidence against H_0, so fail to reject H_0.
    if (p_value <= 0.05):
        print("indicates strong evidence against H_0, so reject H_0")
        print("detects a significant relationship between the variables")
    else:
        print("indicates weak evidence against H_0, so fail to reject H_0")
        print("does not detect a significant relationship between the variables")

    return None