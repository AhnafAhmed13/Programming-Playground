// Binary to Hexadecimal

// Import input prompt
const readline = require("readline");
const prompt = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// let binary = "01000110101000101011100100111101";
console.log("Enter a binary number: ");
prompt.addListener("line", isValid);

// Check if valid binary
function isValid(binary) {
    for (let i = 0, n = binary.length; i < n; i++) {
        if (binary[i] != "0" && binary[i] != "1") {
            console.log("Please enter a valid binary number!");
            return;
        }
    }
    // Forward to conversion
    convert(binary);
}

function convert(binary) {
    let hexadecimal = "";
    
    // Analyze each quartet
    let binary_quartet = "";
    let i = binary.length - 1;
    let remaining = 4;
    
    while (i >= 0) {
        // Populate quartet
        binary_quartet = binary[i] + binary_quartet;

        // Decrement counters
        i--;
        remaining--;
    
        // If a quartet is completed or end of bits
        if (i < 0 || binary_quartet.length == 4) {
            let hexVal = 0;
    
            // If the first quartet is shorter than 4 bits
            if (remaining > 0) {
                for (let r = 0; r < remaining; r++) {
                    binary_quartet = "0" + binary_quartet;
                }
            }
    
            // Convert to hexadecimal value
            if (binary_quartet[0] == "1") hexVal += 8;
            if (binary_quartet[1] == "1") hexVal += 4;
            if (binary_quartet[2] == "1") hexVal += 2;
            if (binary_quartet[3] == "1") hexVal += 1;
    
            // Convert to hexadecimal symbol
            let hexSymbol = hexVal.toString();
            if (hexSymbol == "10") hexSymbol = "A";
            if (hexSymbol == "11") hexSymbol = "B";
            if (hexSymbol == "12") hexSymbol = "C";
            if (hexSymbol == "13") hexSymbol = "D";
            if (hexSymbol == "14") hexSymbol = "E";
            if (hexSymbol == "15") hexSymbol = "F";
    
            // Add to hexadecimal and reset quartet
            hexadecimal = hexSymbol + hexadecimal;
            binary_quartet = "";
            remaining = 4;
        }
    }
    
    // Output formatted hexadecimal
    hexadecimal = "0x" + hexadecimal;
    console.log(hexadecimal);
}