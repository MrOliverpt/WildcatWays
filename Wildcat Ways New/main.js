document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");

    const calculateButton = document.getElementById('calculateButton');
    const startingPointInput = document.getElementById('startingPoint');
    const addDestinationButton = document.getElementById('addDestinationButton');
    const destinationInput = document.getElementById('destination');
    const dropdownContainers = document.querySelectorAll('.dropdown');

    let clickCount = 0;
    let startingPointFilled = false;
    let destinationFilled = false;

    function enableCalculateButton() {
        const startingPoint = startingPointInput.value.trim();
        const destination = destinationInput.value.trim();
        if (startingPoint && (destination || clickCount > 0)) {
            calculateButton.disabled = false;
            calculateButton.classList.add('enabled');
        } else {
            calculateButton.disabled = true;
            calculateButton.classList.remove('enabled');
        }
    }

    function addDestination() {
        console.log("Add destination button clicked");
        clickCount++;
        if (clickCount >= 1) { // Hide the button after one click
            addDestinationButton.style.display = 'none';
            destinationInput.placeholder = 'Please Enter Your Stop Point'; // Change the placeholder text
        }
        if (clickCount < 2) { // Check if less than two destination input fields
            const newDestinationInput = document.createElement('input');
            newDestinationInput.type = 'text';
            newDestinationInput.placeholder = 'Please Enter Your Destination';
            newDestinationInput.classList.add('destination-input');
            newDestinationInput.id = 'destination' + clickCount;
            startingPointInput.parentNode.insertBefore(newDestinationInput, addDestinationButton);
        }
        enableCalculateButton();
    }

    addDestinationButton.addEventListener('click', addDestination);

    dropdownContainers.forEach(container => {
        container.addEventListener('click', function(event) {
            const clickedItem = event.target.closest('.dropdown-content a');
            if (!clickedItem) return; // If the click is not on a dropdown item, do nothing

            event.preventDefault();
            const selectedText = clickedItem.textContent;
            if (!startingPointFilled) { // If starting point hasn't been filled
                startingPointInput.value = selectedText;
                startingPointFilled = true;
            } else if (!destinationFilled) { // If destination hasn't been filled
                destinationInput.value = selectedText;
                destinationFilled = true;
            } else { // If both starting point and destination are filled, allow filling destination inputs again
                const stopInput = document.querySelector('.destination-input:not([value])');
                if (stopInput) {
                    stopInput.value = selectedText;
                }
            }
            enableCalculateButton();
        });
    });

    // Event listener to clear input value when clicked
    [startingPointInput, destinationInput].forEach(input => {
        input.addEventListener('click', function() {
            this.value = '';
            enableCalculateButton();
        });
        // Add input event listener to update button state when input changes
        input.addEventListener('input', enableCalculateButton);
    });

    // Event listener to prevent propagation when clicking inside the add destination button
    addDestinationButton.addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        addDestination();
    });

    // Event listener to prevent propagation when clicking inside the dropdown containers
    dropdownContainers.forEach(container => {
        container.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    });

    enableCalculateButton(); // Ensure button state is initialized
});
