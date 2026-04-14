import math

def calculate_passing_probability(total_q, pass_req, known_q, num_students, options_per_q=2):
    """
    Scalable function to calculate the probability that EXACTLY ONE student 
    passes a multiple choice test.
    """
    # Step 1: Figure out what is left to guess
    questions_to_guess = total_q - known_q
    
    # If they already know enough to pass, they need 0 correct guesses
    guesses_needed = max(0, pass_req - known_q) 
    
    # Probability of getting a single guess right (1/2 for T/F)
    p_correct = 1 / options_per_q
    
    # Step 2: Calculate probability of a SINGLE student passing
    # We sum the binomial probabilities for all passing scenarios 
    # (e.g., getting 1 right, 2 right, or 3 right)
    p_student_passes = 0
    for k in range(guesses_needed, questions_to_guess + 1):
        # Binomial Formula: nCk * p^k * (1-p)^(n-k)
        combinations = math.comb(questions_to_guess, k)
        prob = combinations * (p_correct**k) * ((1 - p_correct)**(questions_to_guess - k))
        p_student_passes += prob
        
    # Step 3: Calculate probability that EXACTLY ONE student passes out of the group
    # This is another binomial distribution! k=1 success out of n=num_students trials.
    p_exactly_one_passes = math.comb(num_students, 1) * (p_student_passes**1) * ((1 - p_student_passes)**(num_students - 1))
    
    return p_student_passes, p_exactly_one_passes

# ==========================================
# 1. Testing our specific assignment question
# ==========================================
p_single, p_final = calculate_passing_probability(
    total_q=5, pass_req=3, known_q=2, num_students=2, options_per_q=2
)

print("--- Original Problem ---")
print(f"Single student passing probability: {p_single} (which is 7/8)")
print(f"Probability exactly ONE passes: {p_final} (which is 7/32)")

# ==========================================
# 2. Scaling it up to a massive exam
# ==========================================
# What if it's a 100-question test, need 60 to pass, they know 40, and there are 5 students?
p_single_huge, p_final_huge = calculate_passing_probability(
    total_q=100, pass_req=60, known_q=40, num_students=5, options_per_q=2
)

print("\n--- Massive Scaled Exam ---")
print(f"Single student passing probability: {p_single_huge:.6f}")
print(f"Probability exactly ONE passes: {p_final_huge:.6f}")