import pytest

def calc(i, current_i=3, w_prev2=0.3, w_prev1=-1.5):
    if i == 1: return 0.3
    if i == 2: return -1.5
    
    km1 = current_i - 1
    kp1 = current_i + 1
    w_current = w_prev1 * w_prev2 * (km1 * km1) / (kp1 * kp1 * kp1)
    
    if current_i == i:
        return w_current
    return calc(i, current_i + 1, w_prev1, w_current)

def test_calc():
    assert calc(1) == 0.3
    assert calc(2) == -1.5
    assert pytest.approx(calc(3)) == -0.028125

if __name__ == "__main__":
    print(calc(5))