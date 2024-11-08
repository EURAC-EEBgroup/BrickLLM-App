// Function to calculate and set the VH subtraction based on screen dimensions
function calculateVhSubtraction() {
    const screenHeight = window.innerHeight;
    const screenWidth = window.innerWidth;
    let vhSubtract;

    if (screenWidth > 1400) {
        if (screenHeight >= 450 && screenHeight < 500) {
            vhSubtract = 89;
        } else if (screenHeight >= 500 && screenHeight < 530) {
            vhSubtract = 82;
        } else if (screenHeight >= 530 && screenHeight < 560) {
            vhSubtract = 79;
        } else if (screenHeight >= 560 && screenHeight < 600) {
            vhSubtract = 76;
        } else if (screenHeight >= 600 && screenHeight < 650) {
            vhSubtract = 72;
        } else if (screenHeight >=  650 && screenHeight < 700) {
            vhSubtract = 67;
        } else if (screenHeight >=  700 && screenHeight < 750) {
            vhSubtract = 64;
        } else if (screenHeight >=  750 && screenHeight < 800) {
            vhSubtract = 61;
        } else if (screenHeight >= 800 && screenHeight < 850) {
            vhSubtract = 59;
        } else if (screenHeight >= 850 && screenHeight < 900) {
            vhSubtract = 57;
        } else if (screenHeight >= 900 && screenHeight < 950) {
            vhSubtract = 55;
        } else if (screenHeight >= 950 && screenHeight < 1000) {
            vhSubtract = 53;
        } else if (screenHeight >= 1000 && screenHeight < 1100) {
            vhSubtract = 51;
        } else if (screenHeight >= 1100 && screenHeight < 1200) {
            vhSubtract = 49;
        } else if (screenHeight >= 1200 && screenHeight < 1250) {
            vhSubtract = 47;
        } else if (screenHeight >= 1250 && screenHeight < 1300) {
            vhSubtract = 43;
        } else if (screenHeight >= 1300 && screenHeight < 1350) {
            vhSubtract = 41;
        } else if (screenHeight >= 1350 && screenHeight < 1400) {
            vhSubtract = 39;
        } else if (screenHeight >= 1400 && screenHeight < 1450) {
            vhSubtract = 37;
        } else if (screenHeight >= 1450 && screenHeight < 1550) {
            vhSubtract = 35;
        } else if (screenHeight >= 1550 && screenHeight < 1650) {
            vhSubtract = 33;
        } else if (screenHeight >= 1650) {
            vhSubtract = 31;
        }
    } else if (screenWidth <= 1400) {
        if (screenHeight >= 1100 && screenHeight < 1250) {
            vhSubtract = 30;
        } else if (screenHeight >= 1250 && screenHeight < 1300) {
            vhSubtract = 28;
        } else if (screenHeight >= 1300 && screenHeight < 1350) {
            vhSubtract = 27;
        } else if (screenHeight >= 1350 && screenHeight < 1400) {
            vhSubtract = 25;
        } else if (screenHeight >= 1650) {
            vhSubtract = 23;
        } else {

        }
    }

    // Apply the calculated vh subtraction to a CSS variable
    document.documentElement.style.setProperty('--vh-subtract', `${vhSubtract}vh`);
}

// Run the function initially
calculateVhSubtraction();

// Update the value when the window is resized
window.addEventListener('resize', calculateVhSubtraction);

// typewriter.js
// typewriter.js

function typeWriterEffect(text, elementId, speed = 0.5) {
    const element = document.getElementById(elementId);
    if (!element) return;

    let i = 0;
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    element.innerHTML = ""; // Clear previous content
    type();
}

// Listen for the custom event 'startTypewriter'
document.addEventListener('startTypewriter', function (e) {
    const element = document.getElementById(e.detail.elementId);
    if (e.detail.text === "") {
        // Hide the element if no text is provided
        element.style.display = "none";
    } else {
        // Show the element and start the typewriter effect
        element.style.display = "block";
        typeWriterEffect(e.detail.text, e.detail.elementId, e.detail.speed);
    }
});

