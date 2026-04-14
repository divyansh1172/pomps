from scipy.stats import binom
from fractions import Fraction

def calculate_only_one_passes(total_questions, required_to_pass, known_answers, options_per_question):

    questions_to_guess = max(0, total_questions - known_answers)
    prob_correct_guess = 1.0 / options_per_question
    
    needed_to_pass = max(0, required_to_pass - known_answers)
    
    if needed_to_pass > questions_to_guess:
        p_pass = 0.0
    elif needed_to_pass == 0:
        p_pass = 1.0
    else:
        p_pass = binom.sf(needed_to_pass - 1, questions_to_guess, prob_correct_guess)
        
    p_fail = 1.0 - p_pass
    p_exactly_one_passes = 2 * p_pass * p_fail
    
    fractional_form = Fraction(p_exactly_one_passes).limit_denominator(1000000)
    
    return p_exactly_one_passes, fractional_form

# EXAMPLE 1: The original problem from the PDF
prob_decimal, prob_fraction = calculate_only_one_passes(
    total_questions = 5,
    required_to_pass = 3,
    known_answers = 2,
    options_per_question = 2
)
print("--- ORIGINAL PROBLEM ---")
print(f"Decimal Probability: {prob_decimal}")
print(f"Fraction Probability: {prob_fraction}")

# EXAMPLE 2: A harder standard multiple-choice test
prob_decimal_2, prob_fraction_2 = calculate_only_one_passes(
    total_questions = 10,
    required_to_pass = 6,
    known_answers = 3,
    options_per_question = 4
)
print("\n--- NEW SCENARIO (MCQ) ---")
print(f"Decimal Probability: {prob_decimal_2:.4f}")
print(f"Fraction Probability: {prob_fraction_2}")