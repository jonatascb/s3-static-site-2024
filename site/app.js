const visitorCounterDigits = 6;

const init = () => {
    const updatedVisitCounter = getUpdatedVisitCounter();
    const spanElements = getSpanElements(updatedVisitCounter);
    const counterElement = document.querySelector('.counter');
    if (counterElement) {
        counterElement.innerHTML = spanElements;
    }
};

const getUpdatedVisitCounter = () => {
    const visitCounter = Number(localStorage.getItem('visitCounter')) + 1;
    localStorage.setItem('visitCounter', visitCounter);
    return visitCounter;
}

const getSpanElements = (visitCounter) => {
    const visitCountStr = visitCounter.toString().padStart(visitorCounterDigits, '0');
    const spanElements = visitCountStr.split('').map(digit => `<span>${digit}</span>`).join(' ');
    return spanElements;
}

init();