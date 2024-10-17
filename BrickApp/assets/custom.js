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
