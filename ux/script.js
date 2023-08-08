function updateResultLabel(result) {
    document.getElementById("resultLabel").innerText = "Result: " + result;
}

function add() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (document.getElementById("useAPI").checked) {
        fetch('/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                num1: num1,
                num2: num2
            })
        })
        .then(response => response.json())
        .then(data => updateResultLabel(data.result))
        .catch(error => console.error('Error:', error));
    } else {
        const result = num1 + num2;
        updateResultLabel(result);
    }
}

function subtract() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (document.getElementById("useAPI").checked) {
        fetch('/subtract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                num1: num1,
                num2: num2
            })
        })
        .then(response => response.json())
        .then(data => updateResultLabel(data.result))
        .catch(error => console.error('Error:', error));
    } else {
        const result = num1 - num2;
        updateResultLabel(result);
    }
}

function multiply() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (document.getElementById("useAPI").checked) {
        fetch('/multiply', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                num1: num1,
                num2: num2
            })
        })
        .then(response => response.json())
        .then(data => updateResultLabel(data.result))
        .catch(error => console.error('Error:', error));
    } else {
        const result = num1 * num2;
        updateResultLabel(result);
    }
}

function divide() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (document.getElementById("useAPI").checked) {
        fetch('/divide', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                num1: num1,
                num2: num2
            })
        })
        .then(response => response.json())
        .then(data => updateResultLabel(data.result))
        .catch(error => console.error('Error:', error));
    } else {
        const result = num1 / num2;
        updateResultLabel(result);
    }
}
