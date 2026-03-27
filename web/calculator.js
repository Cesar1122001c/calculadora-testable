// Lógica de calculadora corregida - Testable con Selenium
let display = document.getElementById('display');
let currentInput = '0';
let operator = null;
let previousInput = null;

function appendToDisplay(value) {
    if (currentInput === '0' && value !== '.') {
        currentInput = value;
    } else {
        currentInput += value;
    }
    display.textContent = currentInput;
}

function handleOperator(nextOperator) {
    if (previousInput === null) {
        previousInput = currentInput;
    } else if (operator) {
        calculate();  // Chain ops
    }
    operator = nextOperator;
    currentInput = '0';
}

function clearDisplay() {
    currentInput = '0';
    operator = null;
    previousInput = null;
    display.textContent = '0';
}

function calculate() {
    if (previousInput === null || operator === null) {
        return;
    }
    let prev = parseFloat(previousInput);
    let curr = parseFloat(currentInput);
    let result;
    switch (operator) {
        case '+': result = prev + curr; break;
        case '-': result = prev - curr; break;
        case '*': result = prev * curr; break;
        case '/': 
            result = (curr === 0) ? 'Error' : prev / curr; 
            break;
        default: return;
    }
    display.textContent = result;
    previousInput = result.toString();
    operator = null;
    currentInput = '0';
}

// Asignar onclicks dinámicos para ops
document.addEventListener('DOMContentLoaded', function() {
    const opButtons = document.querySelectorAll('.btn:not(.btn-clear):not(.btn-equals)');
    opButtons.forEach(btn => {
        btn.onclick = () => {
            const value = btn.textContent.trim();
            if (['+', '-', '*', '/'].includes(value)) {
                handleOperator(value);
            } else {
                appendToDisplay(value);
            }
        };
    });
});

// Para Selenium: IDs fijos, texto buttons predecible

