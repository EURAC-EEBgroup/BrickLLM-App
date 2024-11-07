function calculateVhSubtraction() {
    const screenHeight = window.innerHeight;
    let vhSubtract;

    if (screenHeight >= 800 && screenHeight < 850) {
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
    } else {
        // Default subtraction if below 800
        vhSubtract = 64;
    }

    // Apply the calculated vh subtraction to a CSS variable
    document.documentElement.style.setProperty('--vh-subtract', `${vhSubtract}vh`);
}

// Run the function initially
calculateVhSubtraction();

// Update the value when the window is resized
window.addEventListener('resize', calculateVhSubtraction);


// if (!window.dash_clientside) {
//     window.dash_clientside = {};
// }

// window.dash_clientside.clientside = {
//     display_text: function(n_clicks, text, is_generating) {
//         const elementId = 'log_output_text';
//         const textarea = document.getElementById(elementId);

//         if (!text || n_clicks === 0) {
//             return textarea.value;
//         }

//         // Define a variable to store the interval ID
//         if (!window.textInterval) {
//             window.textInterval = null;
//         }

//         // Start generating text if it is not currently generating
//         if (is_generating && !window.textInterval) {
//             textarea.value = '';  // Clear the textarea before starting
//             let i = 0;
//             window.textInterval = setInterval(function() {
//                 if (i < text.length) {
//                     textarea.value += text.charAt(i);
//                     i++;
//                 } else {
//                     clearInterval(window.textInterval);
//                     window.textInterval = null;  // Clear the interval ID once completed
//                 }
//             }, 100);  // Adjust time to control the speed of the display
//         } 
//         // Stop generating text if already generating
//         else if (!is_generating && window.textInterval) {
//             clearInterval(window.textInterval);
//             window.textInterval = null;
//         }

//         return textarea.value;
//     }
// }
