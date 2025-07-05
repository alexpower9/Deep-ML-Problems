import math

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	# Your code here
	term1 = pow(math.e, (-1 * lam))
	term2 = pow(lam, k)
	term3 = math.factorial(k)
	val = (term1 * term2) / term3

	return round(val, 5)