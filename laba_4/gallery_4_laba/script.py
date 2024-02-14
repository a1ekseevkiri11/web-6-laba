import random
import string
from .models import Captcha
from .forms import CaptchaForm


def generate_math_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    match operator:
        case '+':
            answer = num1 + num2
        
        case '-':
            answer = num1 - num2

        case '*':
            answer = num1 * num2

    expression = f'{num1} {operator} {num2}'
    return expression, str(answer)


def generate_captcha_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def generation_captcha():
    expression, answer = generate_math_captcha()
    key = generate_captcha_key()
    Captcha.objects.create(key=key, answer=answer)
    captcha_form = CaptchaForm(initial={'key': key})
    return expression, captcha_form