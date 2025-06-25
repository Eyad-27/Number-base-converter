#include <iostream>
#include <string>
#include <cctype>
#include <cmath>
using namespace std;

// Function to convert a digit to uppercase (for hexadecimal)
char to_upper(char digit) {
    if (digit >= 'a' && digit <= 'z') {
        return toupper(digit);
    }
    return digit;
}

// Validation functions for different number systems
bool is_valid_decimal(const string& num) {
    for (char digit : num) {
        if (!isdigit(digit)) {
            return false;
        }
    }
    return true;
}

bool is_valid_binary(const string& num) {
    for (char bit : num) {
        if (bit != '0' && bit != '1') {
            return false;
        }
    }
    return true;
}

bool is_valid_octal(const string& num) {
    for (char digit : num) {
        if (digit < '0' || digit > '7') {
            return false;
        }
    }
    return true;
}

bool is_valid_hexadecimal(const string& num) {
    for (char digit : num) {
        char upper_digit = to_upper(digit);
        if (!(isdigit(upper_digit) || (upper_digit >= 'A' && upper_digit <= 'F'))) {
            return false;
        }
    }
    return true;
}

// Convert decimal to any base
string decimal_to_any(int decimal, int base) {
    string final;
    const string hexaDigits = "ABCDEF";

    if (decimal == 0) {
        return "0";
    }

    while (decimal > 0) {
        int remainder = decimal % base;
        if (base == 16 && remainder > 9) {
            final = hexaDigits[remainder - 10] + final;
        } else {
            final = to_string(remainder) + final;
        }
        decimal /= base;
    }
    return final;
}

// Convert any base to decimal
int any_to_decimal(const string& num, int base) {
    const string hexaDigits = "ABCDEF";
    int length = num.length();
    int decimal = 0;

    for (int i = 1; i <= length; i++) {
        char current_char = to_upper(num[length - i]);
        int value;

        if (base == 16 && hexaDigits.find(current_char) != string::npos) {
            value = current_char - 'A' + 10;
        } else {
            value = current_char - '0';
        }

        decimal += value * pow(base, i - 1);
    }
    return decimal;
}

// Main conversion function
string converter(const string& num, int frombase, int tobase) {
    if (frombase == 10) {
        int decimal_num = stoi(num);
        return decimal_to_any(decimal_num, tobase);
    } else {
        int decimal = any_to_decimal(num, frombase);
        return decimal_to_any(decimal, tobase);
    }
}

int main() {
    while (true) {
        // Menu 1
        cout << "* numbering system converter *" << endl;
        cout << "A) insert a new number" << endl;
        cout << "B) Exit program" << endl;
        cout << "Enter your choice: ";

        string choice_menu1;
        getline(cin, choice_menu1);

        if (toupper(choice_menu1[0]) == 'A') {
            cout << "Please insert a number: ";
            string num;
            getline(cin, num);

            while (true) {
                // Menu 2
                cout << "* Please select the base you want to convert a number from *" << endl;
                cout << "A) Decimal" << endl;
                cout << "B) Binary" << endl;
                cout << "C) Octal" << endl;
                cout << "D) Hexadecimal" << endl;
                cout << "Enter your choice: ";

                string choice_menu2;
                getline(cin, choice_menu2);

                int frombase = 0;
                bool valid = true;

                if (choice_menu2 == "A") {
                    if (!is_valid_decimal(num)) {
                        cout << "**please insert a valid decimal number**" << endl;
                        valid = false;
                    } else {
                        frombase = 10;
                    }
                } else if (choice_menu2 == "B") {
                    if (!is_valid_binary(num)) {
                        cout << "**please insert a valid binary number**" << endl;
                        valid = false;
                    } else {
                        frombase = 2;
                    }
                } else if (choice_menu2 == "C") {
                    if (!is_valid_octal(num)) {
                        cout << "**please insert a valid octal number**" << endl;
                        valid = false;
                    } else {
                        frombase = 8;
                    }
                } else if (choice_menu2 == "D") {
                    if (!is_valid_hexadecimal(num)) {
                        cout << "**please insert a valid hexadecimal number**" << endl;
                        valid = false;
                    } else {
                        frombase = 16;
                    }
                } else {
                    cout << "Please select a valid choice" << endl;
                    valid = false;
                }

                if (!valid) {
                    break;
                }

                // Menu 3
                string choice_menu3;
                while (true) {
                    cout << "* Please select the base you want to convert a number to *" << endl;
                    cout << "A) Decimal" << endl;
                    cout << "B) Binary" << endl;
                    cout << "C) Octal" << endl;
                    cout << "D) Hexadecimal" << endl;
                    cout << "Enter your choice: ";
                    getline(cin, choice_menu3);

                    if (choice_menu3 == "A" || choice_menu3 == "B" ||
                        choice_menu3 == "C" || choice_menu3 == "D") {
                        break;
                    } else {
                        cout << "Please select a valid choice" << endl;
                    }
                }

                int tobase = 0;
                if (choice_menu3 == "A") {
                    tobase = 10;
                } else if (choice_menu3 == "B") {
                    tobase = 2;
                } else if (choice_menu3 == "C") {
                    tobase = 8;
                } else if (choice_menu3 == "D") {
                    tobase = 16;
                }

                cout << converter(num, frombase, tobase) << endl;
                break;
            }
        } else if (toupper(choice_menu1[0]) == 'B') {
            exit(0);
        } else {
            cout << "please select a valid choice" << endl;
        }
    }
    return 0;
}