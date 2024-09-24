const init = async () => {
    const updatedVisitCounter = await getUpdatedVisitCounter();
    const spanElements = getSpanElements(updatedVisitCounter);
    const counterElement = document.querySelector('.counter');
    counterElement.innerHTML = spanElements;
};

const getUpdatedVisitCounter = async () => {
    const response = await fetch(`https://api.recipes.jonatascb.com/recipes/${recipeID}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'x-api-key': `${apiKey}`
        },
    });
    const data = await response.json();
    return data.value.VisitsCounter;
};

const getSpanElements = (visitCounter) => {
    const visitorCounterDigits = 6;
    const formattedVisitCounter = visitCounter.toString().padStart(visitorCounterDigits, '0');
    const spanElements = formattedVisitCounter.split('').map(digit => `<span>${digit}</span>`).join(' ');
    return spanElements;
}

init();