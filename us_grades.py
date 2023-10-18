def grade(x):
    if x >= 0.97:
        return 'A⁺'
    elif 0.97 > x >= 0.93:
        return 'A'
    elif 0.93 > x >= 0.90:
        return 'A⁻'
    elif 0.90 > x >= 0.87:
        return 'B⁺'
    elif 0.87 > x >= 0.83:
        return 'B'
    elif 0.83 > x >= 0.80:
        return 'B⁻'
    elif 0.80 > x >= 0.77:
        return 'C⁺'
    elif 0.77 > x >= 0.73:
        return 'C'
    elif 0.73 > x >= 0.70:
        return 'C⁻'
    elif 0.70 > x >= 0.67:
        return 'D⁺'
    elif 0.67 > x >= 0.63:
        return 'D'
    elif 0.63 > x >= 0.60:
        return 'D⁻'
    else: 
        return 'F'
