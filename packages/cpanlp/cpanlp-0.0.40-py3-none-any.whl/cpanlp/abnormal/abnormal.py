import numpy as np

def winner_curse(acquisition_cost, expected_return, num_simulations):
    """
    Simulates the "winner's curse" for a company's acquisition.
    :param acquisition_cost: The cost of the acquisition.
    :param expected_return: The expected return on investment for the acquisition.
    :param num_simulations: The number of simulations to run.
    :return: The average return on investment for the acquisition across all simulations.
    """
    # Assume a normal distribution of returns with a mean of expected_return and standard deviation of 10%
    returns = np.random.normal(expected_return, 0.1, num_simulations)
    investment_returns = (returns * acquisition_cost) - acquisition_cost
    avg_return = np.mean(investment_returns)
    return avg_return
def main():
    print(11)
    a=winner_curse(100,2,10)
    print(a)
if __name__ == '__main__':
    main()