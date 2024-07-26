/**
 * Initializes the visit counter on the webpage.
 */
const init = () => {
    const updatedVisitCounter = getUpdatedVisitCounter();
    const spanElements = getSpanElements(updatedVisitCounter);
    const counterElement = document.querySelector('.counter');
    counterElement.innerHTML = spanElements;
};

const getUpdatedVisitCounter = () => {
    const visitCounter = (Number(localStorage.getItem('visitCounter')) + 1) || 1;
    localStorage.setItem('visitCounter', visitCounter);
    return visitCounter;
}

const getSpanElements = (visitCounter) => {
    const visitCountStr = visitCounter.toString().padStart(6, '0');
    const spanElements = visitCountStr.split('').map(digit => `<span>${digit}</span>`).join(' ');
    return spanElements;
}

init();